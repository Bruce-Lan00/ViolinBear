import subprocess
import os

def run_audiveris(image_path, output_folder):
    audiveris_path = os.path.abspath("app-5.6.1/bin/Audiveris")
    output_path = output_folder  # 不再进入子目录

    cmd = [
        audiveris_path,
        "-batch", "-export",
        "-output", output_folder,
        image_path
    ]

    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if result.returncode != 0:
        raise RuntimeError("Audiveris failed: " + result.stderr.decode("utf-8"))

    # 取出图片名 test.png -> test.mxl
    base_name = os.path.splitext(os.path.basename(image_path))[0]
    mxl_path = os.path.join(output_path, f"{base_name}.mxl")

    if not os.path.exists(mxl_path):
        raise FileNotFoundError(f"MusicXML (.mxl) not found at {mxl_path}")

    return mxl_path