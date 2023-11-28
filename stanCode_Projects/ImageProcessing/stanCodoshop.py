"""
File: stanCodoshop.py
Name: Paul
----------------------------------------------
SC101_Assignment3 Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns a value that refers to the "color distance" between a pixel and a mean RGB value.

    Input:
        pixel (Pixel): the pixel with RGB values to be compared
        red (int): the average red value of the pixels to be compared
        green (int): the average green value of the pixels to be compared
        blue (int): the average blue value of the pixels to be compared

    Returns:
        dist (float): the "color distance" of a pixel to the average RGB value of the pixels to be compared.
    """
    dist = ((red - pixel.red) ** 2 + (green - pixel.green) ** 2 + (blue - pixel.blue) ** 2) ** 0.5
    return dist


def get_average(pixels):
    """
    Given a list of pixels, finds their average red, blue, and green values.

    Input:
        pixels (List[Pixel]): a list of pixels to be averaged

    Returns:
        rgb (List[int]): a list of average red, green, and blue values of the pixels
                        (returns in order: [red, green, blue])
    """
    t_red = 0
    t_green = 0
    t_blue = 0
    num_pixels = len(pixels)
    for pixel in pixels:  # Loop over pixels and sum up their RGB values
        t_red += pixel.red
        t_green += pixel.green
        t_blue += pixel.blue
    # Calculate the average RGB values
    avg_r = t_red / num_pixels
    avg_g = t_green / num_pixels
    avg_b = t_blue / num_pixels
    return [int(avg_r), int(avg_g), int(avg_b)]


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest "color distance",
    which has the closest color to the average.


    Input:
        pixels (List[Pixel]): a list of pixels to be compared
    Returns:
        best (Pixel): the pixel which has the closest color to the average
    """
    avg_rgb = get_average(pixels)  # Get the average RGB values
    best_pixel = min(pixels, key=lambda pixel: get_pixel_dist(pixel, avg_rgb[0], avg_rgb[1], avg_rgb[2]))
    # Find the smallest distance
    return best_pixel


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these  images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    for x in range(width):  # Loop over all pixels in the image
        for y in range(height):
            # Create a list to hold the pixels for each image at this x,y location
            same_pixels = list(img.get_pixel(x, y) for img in images)
            # Create a list to keep the pixels for each image at this x,y location
            best_pixel = get_best_pixel(same_pixels)  # Find the best pixel among all
            result_pixel = result.get_pixel(x, y)  # Set the pixel at this x,y location in the result image
            result_pixel.red = best_pixel.red  # Set the best red pixel at result
            result_pixel.green = best_pixel.green  # Set the best green pixel at result
            result_pixel.blue = best_pixel.blue  # Set the best blue pixel at result

    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
