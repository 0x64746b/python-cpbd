# coding: utf-8

from __future__ import absolute_import, print_function, unicode_literals

from sys import argv

import numpy as np
from scipy.ndimage import imread
from skimage.feature import canny
from skimage.filters import sobel_v


def compute(input_image):
    # type: (numpy.ndarray) -> float
    """Compute the sharpness metric for the given data."""
    print(input_image[0,0])

    width_jnb = np.concatenate([5*np.ones(51), 3*np.ones(205)])

    canny_edges = canny(input_image)
    sobel_edges = _simple_thinning(sobel_v(input_image))


def _simple_thinning(strength):
    # type: (numpy.ndarray) -> numpy.ndarray
    """
    Perform a very simple thinning.

    Inspired by the [Octave implementation](https://sourceforge.net/p/octave/image/ci/default/tree/inst/edge.m#l512).
    """
    num_rows, num_cols = strength.shape

    zero_column = np.zeros((num_rows, 1))
    zero_row = np.zeros((1, num_cols))

    x = (
        (strength > np.c_[zero_column, strength[:, :-1]]) &
        (strength > np.c_[strength[:, 1:], zero_column])
    )

    y = (
        (strength > np.r_[zero_row, strength[:-1, :]]) &
        (strength > np.r_[strength[1:, :], zero_row])
    )

    return x | y


if __name__ == '__main__':
    input_image = imread(argv[1], mode='L')
    compute(input_image)