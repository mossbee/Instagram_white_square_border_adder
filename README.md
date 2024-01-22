# Instagram White Border Image Creator

This Python script adds a white border to images, creating a final square image suitable for Instagram upload. It automatically checks whether the image is in portrait or landscape orientation using the EXIF data and applies the necessary border to maintain the aspect ratio.

## Features

- Automatically detects portrait or landscape orientation using EXIF data.
- Adds a customizable white border around the image.
- Outputs the final square image in PNG format.

## Requirements

- Python 3.x
- Pillow library (can be installed using `pip install pillow`)

## Usage

1. Clone this repository or download the script `add_border.py`.

2. Place the images you want to process in a folder.

3. Open a terminal or command prompt and navigate to the directory containing the script and images.

4. Run the script using the following command:

   ```bash
   python add_border.py [Images folder name]
The script will process all `.jpg` and `.png` images in the specified folder.

5.  The output images with the white border will be saved in the same folder with the suffix `_1.png`.

## Customization

You can modify the `border_percentage` parameter in the script to adjust the width of the white border. The percentage value determines how much of the image's dimensions will be used for the border. For example, setting `border_percentage` to 4 will result in a border that is 4% of the image's width.

## Notes

-   Make sure you have the necessary permissions to access and modify the images in the specified folder.
-   This script assumes that the images are in JPEG or PNG format.
