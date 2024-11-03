import subprocess
import os
import glob
from IPython.display import HTML, display
from base64 import b64encode
import matplotlib.pyplot as plt
import ipywidgets as widgets

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running command: {command}")
        print(result.stderr)
    else:
        print(result.stdout)

# GPU sorgulama
run_command("nvidia-smi --query-gpu=name,memory.total,memory.free --format=csv,noheader")

# Python alternatifleri yükleme
run_command("sudo update-alternatives --install /usr/local/bin/python3 python3 /usr/bin/python3.8 2")
run_command("sudo update-alternatives --install /usr/local/bin/python3 python3 /usr/bin/python3.9 1")

# Python ve diğer gerekli paketleri yükleme
run_command("sudo apt install python3.8")
run_command("sudo apt-get install python3.8-distutils")
run_command("python --version")
run_command("apt-get update")
run_command("apt install software-properties-common")
run_command("sudo dpkg --remove --force-remove-reinstreq python3-pip python3-setuptools python3-wheel")
run_command("apt-get install python3-pip")

# Projeyi klonlama ve gereksinimleri yükleme
print('Git clone project and install requirements...')
run_command("git clone https://github.com/Winfredy/SadTalker")
os.chdir("SadTalker")
os.environ["PYTHONPATH"] = "/content/SadTalker:" + os.environ.get("PYTHONPATH", "")
run_command("python3.8 -m pip install torch==1.12.1+cu113 torchvision==0.13.1+cu113 torchaudio==0.12.1 --extra-index-url https://download.pytorch.org/whl/cu113")
run_command("apt update")
run_command("apt install ffmpeg")
run_command("python3.8 -m pip install -r requirements.txt")

# Önceden eğitilmiş modelleri indirme
print('Download pre-trained models...')
run_command("rm -rf checkpoints")
run_command("bash scripts/download_models.sh")

# Görsel arayüz ile resim seçme
print("Choose the image name to animate: (saved in folder 'examples/')")
img_list = sorted([item.split('.')[0] for item in glob.glob1('examples/source_image', '*.png')])
default_head_name = widgets.Dropdown(options=img_list, value='full3')

def on_change(change):
    if change['type'] == 'change' and change['name'] == 'value':
        plt.imshow(plt.imread(f'examples/source_image/{default_head_name.value}.png'))
        plt.axis('off')
        plt.show()

default_head_name.observe(on_change)
display(default_head_name)

plt.imshow(plt.imread(f'examples/source_image/{default_head_name.value}.png'))
plt.axis('off')
plt.show()

# Seçili ses dosyası ile görüntüyü işleme
img = 'source_image/images.jpeg'
print(img)
run_command(f"python3.8 inference.py --driven_audio ./examples/driven_audio/Müşteri-Hizmetleri.wav --source_image {img} --result_dir ./results --still --preprocess full --enhancer gfpgan")

# Animasyonu görüntüleme
print('Display animation:')
results = sorted(os.listdir('./results'))
mp4_name = glob.glob('./results/*.mp4')[0]

with open(mp4_name, 'rb') as mp4_file:
    mp4_data = mp4_file.read()
data_url = "data:video/mp4;base64," + b64encode(mp4_data).decode()

display(HTML(f"""
  <video width=256 controls>
        <source src="{data_url}" type="video/mp4">
  </video>
  """))
