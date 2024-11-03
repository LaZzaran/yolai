import os
import subprocess
import sys
from pathlib import Path
from config.settings import Settings


class SadTalkerService:
    def __init__(self):
        self.sadtalker_dir = Settings.SADTALKER_DIR

    def setup(self):
        """SadTalker kurulumu"""
        if not os.path.exists(self.sadtalker_dir):
            try:
                # Doğru dizine git
                current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                os.chdir(current_dir)

                subprocess.run(
                    ["git", "clone", "https://github.com/OpenTalker/SadTalker.git"],
                    check=True
                )

                os.chdir(self.sadtalker_dir)
                subprocess.run(
                    [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"],
                    check=True
                )

                subprocess.run(
                    [sys.executable, "scripts/download_models.py"],
                    check=True
                )

            except subprocess.CalledProcessError as e:
                print(f"Kurulum hatası: {e}")
                raise
            except Exception as e:
                print(f"Beklenmeyen hata: {e}")
                raise
            finally:
                # Her durumda başlangıç dizinine geri dön
                os.chdir(current_dir)

    def generate_talking_head(self, audio_path: str, source_image: str, output_dir: str) -> str | None:
        try:
            result_dir = Path(output_dir) / "talking_heads"
            result_dir.mkdir(parents=True, exist_ok=True)

            audio_path = str(Path(audio_path).absolute())
            source_image = str(Path(source_image).absolute())
            result_dir = str(result_dir.absolute())

            os.chdir(self.sadtalker_dir)

            cmd = [
                sys.executable,
                "inference.py",
                "--driven_audio", audio_path,
                "--source_image", source_image,
                "--result_dir", result_dir,
                "--still",
                "--preprocess", "full",
                "--enhancer", "gfpgan"
            ]

            subprocess.run(cmd, check=True)

            video_files = list(Path(result_dir).glob("*.mp4"))
            if video_files:
                return str(max(video_files, key=os.path.getctime))

            return None

        except Exception as e:
            print(f"Video oluşturma hatası: {e}")
            return None
