"""
File: fire.py
Name: Paul
---------------------------------
This file contains a method called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation.
"""
from simpleimage import SimpleImage


HURDLE_FACTOR = 1.05


def highlight_fires(filename):
    """
    :param filename: The image file is to be processed.
    :return: A processed version of image that highlighted the fire area in red.
    """
    img = SimpleImage(filename)  # Load original image
    for pixel in img:  # Loop through each pixel in the image
        avg = (pixel.red + pixel. green + pixel.blue) // 3  # Calculate the average color of RGB.
        if pixel.red > avg * HURDLE_FACTOR:  # If the red color  is significantly higher than GB, it might be fire.
            pixel.red = 255  # Set significant area red.
            pixel.green = 0
            pixel.blue = 0
        else:
            # Set rest area to grayscale.
            pixel.red = avg
            pixel.green = avg
            pixel.blue = avg
    return img


def main():
    """
    Pre-conditions: Load image address.
    Post-conditions: The original and processed images are displayed.
    """
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    highlighted_fire.show()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
