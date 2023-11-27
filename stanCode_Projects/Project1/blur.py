"""
File: blur.py
Name: Paul
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: The image to be blurred
    :return: A new image that is a blurred version from original image.
    """
    # img = SimpleImage(img)
    new_img = SimpleImage.blank(img.width, img.height)
    # Create a blank image with the same size as original one.
    for x in range(img.width):
        for y in range(img.height):
            # Find all pixels.
            r_sum = 0
            g_sum = 0
            b_sum = 0
            count = 0
            for i in range(-1, 2, 1):
                for j in range(-1, 2, 1):
                    # Locate the target pixel together with 8 pixels next to it.
                    pixel_x = x + i
                    pixel_y = y + j
                    if 0 <= pixel_x < img.width:
                        if 0 <= pixel_y < img.height:
                            # Set the conditions to exclude the edge pixels.
                            pixel = img.get_pixel(pixel_x, pixel_y)
                            r_sum += pixel.red
                            g_sum += pixel.green
                            b_sum += pixel.blue
                            count += 1
            new_pixel = new_img.get_pixel(x, y) # Get new pixels for new img
            new_pixel.red = r_sum / count # Put new r pixels in to new img
            new_pixel.green = g_sum / count # put new g pixels in to new img
            new_pixel.blue = b_sum / count # put new b pixels in to new img
    return new_img


def main():
    """
    Pre-conditions: Load image address.
    Post-conditions: The original and blurred images are displayed.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img) # Create a function to blur image
    for i in range(5):  # Repeat the blurring process BLUR_RATIO times to increase the blur effect
        blurred_img = blur(blurred_img)
    blurred_img.show()


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
