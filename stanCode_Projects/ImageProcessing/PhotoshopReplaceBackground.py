"""
File: PhotoshopReplaceBackground.py
Name: Paul
----------------------------------
This file creates a photoshopped image
that is going to compete for the Best
Photoshop Award for SC001.
Please put all the images you will use in the image_contest folder
and make sure to choose the right folder when loading your images.
"""
from simpleimage import SimpleImage

THRESHOLD = 1.27
BLACK = 120


def main():
    """
    Original image is my shadow on the ground, but if you change
    the background with scenery view. It looks like a silhouette effect,
    like a man standing in front of you but you can't see his face.
    It creates a spooky vibes.
    """
    # Load the original image and the background image.
    img = SimpleImage("best_photoshop_image_idea/Paul.jpeg")
    bg = SimpleImage("best_photoshop_image_idea/Paul_bg.jpeg")
    bg.make_as_big_as(img)  # Resize the background image to match the original one.
    img.show()  # Show the original image
    # bg.show()
    for x in range(img.width):  # Loop through each pixel
        for y in range(img.height):
            img_pixel = img.get_pixel(x, y)  # Get the pixel from the original image
            avg = (img_pixel.red + img_pixel.green + img_pixel.blue) // 3
            # Calculate the average values of RGB.
            total = img_pixel.red + img_pixel.green + img_pixel.blue
            # Calculate the total value of RGB.
            if img_pixel.green > avg * THRESHOLD and total > BLACK:
                # if G is significantly higher RB and total is above threshold, it could be G.
                bg_pixel = bg.get_pixel(x, y)  # Get pixel from background image.
                img_pixel.red = bg_pixel.red
                img_pixel.green = bg_pixel.green
                img_pixel.blue = bg_pixel.blue
    return img.show()

# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    main()
