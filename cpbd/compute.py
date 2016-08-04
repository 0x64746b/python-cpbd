# coding: utf-8

from __future__ import absolute_import, print_function, unicode_literals

from sys import argv

import numpy as np
from PIL import Image


MATLAB_GRAYSCALE_MATRIX = (0.2989, 0.5870, 0.1140, 0)


def imread(image_path):
    # type: (str) -> numpy.ndarray
    """
    Open the image at the given path.

    Convert it to grayscale and return an appropriately shaped array of
    intensities.
    """
    image = Image.open(image_path)

    # convert to gray scale if color image
    if image.mode != 'L':
        image = image.convert('L', MATLAB_GRAYSCALE_MATRIX)

    # convert the image to double for further processing
    return np.array(image.getdata(), dtype=np.float64).reshape(
        image.size[::-1]
    )


def compute(input_image):
    # type: (numpy.ndarray) -> float
    """Compute the sharpness metric for the given data."""
    print(input_image[0,0])

    width_jnb = np.concatenate([5*np.ones(51), 3*np.ones(205)])


if __name__ == '__main__':
    input_image = imread(argv[1])
    compute(input_image)