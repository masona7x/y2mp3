import os
import platform
import shutil
import subprocess
import sys
import tempfile
import urllib.request
import zipfile



def ensure_ffmpeg():
    def ffmpeg_installed():
        return shutil.which("ffmpeg") is not None

    if ffmpeg_installed():
        print("✅ ffmpeg found.")
        return

    system = platform.system()
    print(f"🔧 ffmpeg not found. Attempting to install on {system}...")

    try:
        if system == "Linux":
            subprocess.run(["sudo", "apt", "install", "-y", "ffmpeg"], check=True)

        elif system == "Darwin":  # macOS
            subprocess.run(["brew", "install", "ffmpeg"], check=True)

        elif system == "Windows":
            # Download a Windows ffmpeg zip, extract it, and add to PATH
            url = "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip"
            temp_dir = tempfile.mkdtemp()
            zip_path = os.path.join(temp_dir, "ffmpeg.zip")
            urllib.request.urlretrieve(url, zip_path)

            with zipfile.ZipFile(zip_path, "r") as zip_ref:
                zip_ref.extractall(temp_dir)

            ffmpeg_path = None
            for root, dirs, files in os.walk(temp_dir):
                if "ffmpeg.exe" in files:
                    ffmpeg_path = root
                    break

            if not ffmpeg_path:
                print("❌ Could not find ffmpeg.exe in zip.")
                sys.exit(1)

            ffmpeg_bin = os.path.abspath("ffmpeg_bin")
            os.makedirs(ffmpeg_bin, exist_ok=True)

            for file in ["ffmpeg.exe", "ffprobe.exe"]:
                shutil.copy(os.path.join(ffmpeg_path, file), ffmpeg_bin)

            os.environ["PATH"] += os.pathsep + ffmpeg_bin
            print(f"✅ ffmpeg installed locally at {ffmpeg_bin}")

        else:
            print(f"⚠️ Unsupported OS: {system}. Please install ffmpeg manually.")
            sys.exit(1)

        # Final check
        if not ffmpeg_installed():
            print("❌ Installation failed. Please install ffmpeg manually.")
            sys.exit(1)

    except Exception as e:
        print(f"❌ Error installing ffmpeg: {e}")
        sys.exit(1)