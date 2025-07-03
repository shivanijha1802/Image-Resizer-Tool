# imageResizer.py
# Author: Shivani Jha
# Date: 2025-06-03
# Description: This script resizes an image to a specified width and height.

import os
from PIL import Image

# Resizing image settings
inputImg_folder = "input_images"                 # Folder containing the input images
outputImg_folder = "resized_images"               # Folder to save the resized images
new_size = (1000, 500)
outputImg_format = "JPEG"

# Creates the output folder if it not exist
if not os.path.exists(outputImg_folder):
    os.makedirs(outputImg_folder)

# Resize & Convert Image logic:
for filename in os.listdir(inputImg_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff')):
        image_path = os.path.join(inputImg_folder, filename)

        # Opens the image uisng PIL(Pillow)
        with Image.open(image_path) as img:
            # Resize the image
            resized_img = img.resize(new_size)

            # Converts into RGB mode if not
            if resized_img.mode != "RGB":
                resized_img = resized_img.convert("RGB")

            # Prepares a new filename with format
            real_name = os.path.splitext(filename)[0]
            new_fileName = f"{real_name}.{outputImg_format.lower()}"
            output_path = os.path.join(outputImg_folder, new_fileName)

            # Saves the resized image
            resized_img.save(output_path, outputImg_format)
            print(f"Image Saved: {output_path}")

print("All images resized and saved successfully!")