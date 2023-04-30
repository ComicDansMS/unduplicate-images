# Unduplicate Images

This Python script searches through a specified source folder (including subdirectories) and copies unique images to a destination folder, maintaining the original folder structure. Duplicate images are skipped, and a log file is created listing the paths of duplicate images.

The script is compatible with Python 3.6 and above.

## Features

- Iterates through a designated source folder (including subdirectories)
- Copies unique images to a destination folder, keeping the original folder structure
- Skips over duplicate images (comparing image content, not file names)
- Creates a log file listing the paths of all duplicate images
- Displays a progress bar in the terminal

## Supported Image Formats

The script supports the following image formats:

- JPEG (both `.jpg` and `.jpeg` extensions)
- PNG (`.png`)
- GIF (`.gif`)
- WebP (`.webp`)

## How to use

1. Make sure you have Python 3.6 or later installed on your system.
2. Install the required package: `tqdm` using `pip install tqdm` or `pip3 install tqdm` (depending on your Python version)
3. Download the script as `unduplicate.py`.
4. Open the `unduplicate.py` script in your preferred text editor.
5. In the script, set `source_folder` variable to the path of the folder containing the original images.
6. Set the `destination_folder` variable to the path of the folder where unique images should be copied.
7. Save the changes and run the script: `python unduplicate.py`

## Example

For example, if you have a folder named 'images' containing the original images and you want to copy the unique images to a folder named 'sorted-images':

```python
source_folder = "images"
destination_folder = "sorted-images"