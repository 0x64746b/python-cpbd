# coding: utf-8

from __future__ import absolute_import, print_function, unicode_literals

from sys import argv

import numpy as np
from scipy.ndimage import imread


def compute(input_image):
    # type: (numpy.ndarray) -> float
    """Compute the sharpness metric for the given data."""
    print(input_image[0,0])

    width_jnb = np.concatenate([5*np.ones(51), 3*np.ones(205)])


if __name__ == '__main__':
    input_image = imread(argv[1], mode='L')
    compute(input_image)