from PIL import Image, ImageOps
import os
import sys
import multiprocessing
from tqdm import tqdm

def add_border(image_path, border_percentage):
    original_image = Image.open(image_path)

    image = ImageOps.exif_transpose(original_image)
    width, height = image.size
    border_width = int(width * border_percentage / 100)
    new_size = max(width + 2 * border_width, height + 2 * border_width)
    new_image = Image.new("RGB", (new_size, new_size), "white")
    
    # Center the original image within the new image
    x_offset = int((new_size - width) / 2)
    y_offset = int((new_size - height) / 2)
    new_image.paste(image, (x_offset, y_offset))
    
    # Export the image to a new PNG file
    filename, ext = os.path.splitext(image_path)
    new_image.save(f"{filename}_1.png")
    
    return new_image 

def process_image(image_path):
    return add_border(image_path, 4)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <folder_path>")
        sys.exit(1)

    folder_path = sys.argv[1]

    # Get a list of all images in the folder
    images = [os.path.join(folder_path, filename) for filename in os.listdir(folder_path) if filename.endswith('.jpg') or filename.endswith('.png')]

    # Create a pool of processes
    with multiprocessing.Pool() as pool:
        # Use tqdm for progress bar
        for _ in tqdm(pool.imap_unordered(process_image, images), total=len(images)):
            pass

