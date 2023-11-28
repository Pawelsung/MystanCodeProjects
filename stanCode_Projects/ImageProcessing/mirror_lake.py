"""
File: mirror_lake.py
Name: Paul
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename: The image file is going to be mirrored
    :return: A new image that is mirrored version.
    """
    img = SimpleImage(filename)  # Load the original image.
    b_img = SimpleImage.blank(img.width, img.height * 2)
    # Create a new blank image that is same width and twice the height of original image.
    for x in range(img.width):
        for y in range(img.height):
            # Loop through each pixel.
            img_pixel = img.get_pixel(x, y)  # Get pixel from original image.
            big_img_pixel1 = b_img.get_pixel(x, y)  # Get pixel from the top part of new image.
            big_img_pixel1.red = img_pixel.red  # Set original red pixel to new image.
            big_img_pixel1.green = img_pixel.green  # Set original green pixel to new image.
            big_img_pixel1.blue = img_pixel.blue  # Set original blue pixel to new image.
            big_img_pixel2 = b_img.get_pixel(x, b_img.height-1-y)  # Get pixel from the bottom part of new image.
            big_img_pixel2.red = img_pixel.red  # Set original red pixel to new image.
            big_img_pixel2.green = img_pixel.green  # Set original green pixel to new image.
            big_img_pixel2.blue = img_pixel.blue  # Set original blue pixel to new image.
    return b_img


def main():
    """
    Pre-conditions: Load image address.
    post-conditions: The original and reflected images are displayed.
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
