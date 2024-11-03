import torch
from diffusers import StableDiffusion3Pipeline
from huggingface_hub import login
from stabilityai.config import PIPELINE_MODEL_PATH
from stabilityai.config import HUGGINGFACE_TOKEN
def run_model(prompt: str, output_path: str):
    login(token=HUGGINGFACE_TOKEN)  # Config'de HUGGINGFACE_TOKEN tanımlı olmalı
    pipe = StableDiffusion3Pipeline.from_pretrained(PIPELINE_MODEL_PATH,
                                                    torch_dtype=torch.bfloat16,
                                                    use_auth_token=True)
    pipe = pipe.to("cuda")

    image = pipe(prompt,
                 num_inference_steps=28,
                 guidance_scale=3.5
                 ).images[0]

    image.save(output_path)
    print(f"Image saved at {output_path}")
