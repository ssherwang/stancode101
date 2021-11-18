"""
File: stanCodoshop.py
----------------------------------------------
SC101_Assignment3
Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.

-----------------------------------------------

TODO: to eliminate people in images. using a list of images, to compare all of pixels in images and skip the outlier.
so that we can find the "best" pixel and fill the best pixel in a new blank images.
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (float): color distance between red, green, and blue pixel values

    """
    color_distance = ((red-pixel.red)**2 + (green-pixel.green)**2 + (blue-pixel.blue)**2)**0.5
    return color_distance


def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]

    """
    # set initial values for calculating total pixels amount
    total_red_pixel = 0
    total_green_pixel = 0
    total_blue_pixel = 0

    for i in range(len(pixels)):
        # get each red, green and blues pixels in each pixel
        pixel_red = pixels[i].red
        pixel_green = pixels[i].green
        pixel_blue = pixels[i].blue

        # calculate total amount
        total_red_pixel += pixel_red
        total_green_pixel += pixel_green
        total_blue_pixel += pixel_blue

    # save results as a list in the order : red, green, blue
    red_green_blue = [int(total_red_pixel/len(pixels)), int(total_green_pixel/len(pixels)),
                      int(total_blue_pixel/len(pixels))]
    return red_green_blue


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    """
    # calculate reference pixel to be compared
    avg = get_average(pixels)

    # set initial max value ot pixel distance to find the minimum
    minimum_pixel_dist = float('inf')

    # set initial best pixel value
    best_pixel = pixels[0]

    # use for loop to find the minimum pixel distance as the best one pixel
    for i in range(len(pixels)):
        dist = get_pixel_dist(pixels[i], avg[0], avg[1], avg[2])
        if dist < minimum_pixel_dist:
            minimum_pixel_dist = dist
            best_pixel = pixels[i]
    return best_pixel


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    ######## YOUR CODE STARTS HERE #########
    # Write code to populate image and create the 'ghost' effect
    # using for loop to get the (x, y) coordinate of each pixel
    for x in range(result.width):
        for y in range(result.height):
            # make a list to save all of the (x, y) coordinate of each image
            lst = []
            for i in range(len(images)):
                pixel_x_y = images[i].get_pixel(x, y)
                lst.append(pixel_x_y)
                pixel = get_best_pixel(lst)
                # fill the best pixel in the blank canvas
                result.set_pixel(x, y, pixel)

    ######## YOUR CODE ENDS HERE ###########
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
