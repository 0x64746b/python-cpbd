# coding: utf-8

from __future__ import absolute_import, print_function, unicode_literals

import numpy as np
from scipy.signal import convolve2d


VSOBEL_WEIGHTS = np.array([
    [1, 0, -1],
    [2, 0, -2],
    [1, 0, -1]
])


def sobel(image, threshold):
    # type: (numpy.ndarray, int) -> numpy.ndarray
    """Find the edges in `image` using the Sobel approximation."""

    # Compute edge strength
    strength = abs(convolve2d(image, VSOBEL_WEIGHTS, mode='same'))

    ## Perform thresholding and simple thinning
    strength[strength <= threshold] = 0
    return _simple_thinning(strength)


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


