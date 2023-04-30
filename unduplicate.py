import os
import shutil
import hashlib
from tqdm import tqdm
from datetime import datetime

source_folder = "images"
destination_folder = "sorted-images"
duplicates_log = "duplicates.log"

def get_image_hash(image_path):
    try:
        with open(image_path, "rb") as f:
            image_bytes = f.read()
        return hashlib.md5(image_bytes).hexdigest()
    except IOError as e:
        print(f"Error reading file: {image_path}, {e}")
        return None

def find_duplicates_and_copy(src, dest, duplicates_path):
    if not os.path.exists(src):
        raise FileNotFoundError(f"{src} not found.")

    if not os.path.exists(dest):
        os.makedirs(dest)

    img_hashes = set()

    num_files = sum([len(files) for r, d, files in os.walk(src)])
    progress_bar = tqdm(total=num_files, desc="Processing images")

    for root, _, files in os.walk(src):
        for file in files:
            if not file.lower().endswith((".jpg", ".png", ".gif", ".jpeg")):
                continue
            src_path = os.path.join(root, file)
            dest_path = os.path.join(dest, os.path.relpath(src_path, start=src))
            duplicates_path = os.path.join(dest, os.path.relpath(src_path, start=src))

            img_hash = get_image_hash(src_path)
            if img_hash in img_hashes:
                with open(duplicates_log, "a") as dups_log:
                    dups_log.write(f"{src_path}\n")
            else:
                img_hashes.add(img_hash)
                os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                shutil.copy2(src_path, dest_path)

            progress_bar.update(1)

    progress_bar.close()

if __name__ == "__main__":
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(duplicates_log, "a") as f:
        f.write(f"\nRUN TIMESTAMP: {timestamp}\n")
        f.write("DUPLICATE IMAGES:\n")
    find_duplicates_and_copy(source_folder, destination_folder, duplicates_log)