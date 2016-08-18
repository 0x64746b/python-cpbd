# coding: utf-8

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals
)

from math import atan2, pi
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


def marziliano_method(edges, image):
    # type: (numpy.ndarray, numpy.ndarray) -> numpy.ndarray
    """
    Calculate the widths of the given edges.

    :return: A matrix with the same dimensions as the given image with 0's at
        non-edge locations and edge-widths at the edge locations.
    """
    edge_widths = np.zeros(image.shape)

    # TODO: Check weird order. Rename?
    gy, gx = np.gradient(image)

    img_height, img_width = image.shape

    edge_angles = np.zeros(image.shape)

    for m in range(img_height):
        for n in range(img_width):
            if gx[m, n] != 0:
                edge_angles[m, n] = atan2(gy[m, n], gx[m, n]) * (180 / pi)
            elif gx[m, n] == 0 and gy[m, n] == 0:
                edge_angles[m,n] = 0
            elif gx[m, n] == 0 and gy[m, n] == pi/2:
                edge_angles[m, n] = 90

    if np.any(edge_angles):
        quantized_angles = 45 * np.round(edge_angles / 45)

        for m in range(1, img_height - 1):
            for n in range(1, img_width - 1):
                if edges[m, n] == 1:

                    if quantized_angles[m, n] == 180 or quantized_angles[m, n] == -180:
                        for k in range(100 + 1):
                            pos_y1 = (n - 1) - k
                            pos_y2 = (n - 2) - k

                            if pos_y2 < 0 or (image[m, pos_y2] - image[m, pos_y1]) <= 0:
                                break

                        width_count_side_1 = k + 1

                        for k in range(100 + 1):
                            neg_y1 = (n + 1) + k
                            neg_y2 = (n + 2) + k

                            if neg_y2 >= img_height or (image[m, neg_y2] - image[m, neg_y1]) >= 0:
                                break

                        width_count_side_2 = k + 1

                        edge_widths[m, n] = width_count_side_1 + width_count_side_2

                    if quantized_angles[m, n] == 0:
                        for k in range(100 + 1):
                            pos_y1 = (n + 1) + k
                            pos_y2 = (n + 2) + k

                            if pos_y2 >= img_width or (image[m, pos_y2] - image[m, pos_y1]) <= 0:
                                break

                        width_count_side_1 = k + 1

                        for k in range(100 + 1):
                            neg_y1 = (n - 1) - k
                            neg_y2 = (n - 2) - k

                            if neg_y2 < 0 or (image[m, neg_y2] - image[m, neg_y1] >= 0):
                                break

                        width_count_side_2 = k + 1

                        edge_widths[m, n] = width_count_side_1 + width_count_side_2

    return edge_widths


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