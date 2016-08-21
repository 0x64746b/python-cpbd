# coding: utf-8

from __future__ import absolute_import, print_function, unicode_literals

import numpy as np
from scipy import ndimage


def sobel(image):
    # type: (numpy.ndarray, int) -> numpy.ndarray
    """Find the edges in `image` using the Sobel approximation."""

    # http://stackoverflow.com/a/7186582/1666398
    dx = ndimage.sobel(image, 0)
    dy = ndimage.sobel(image, 1)
    mag = np.hypot(dx, dy)
    mag *= 255.0 / np.max(mag)

    # http://www.kerrywong.com/2009/05/07/canny-edge-detection-auto-thresholding/
    threshold = np.mean(mag)
    mag[mag <= threshold] = 0

    return _simple_thinning(mag)


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


