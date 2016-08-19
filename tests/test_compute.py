# coding: utf-8

from __future__ import absolute_import, print_function, unicode_literals


import numpy as np
import pytest

from cpbd.compute import marziliano_method, _calculate_sharpness_metric
from .helpers import parse_matlab_data


@pytest.fixture
def reference_input():
    return parse_matlab_data('tests/data/reference_img1_input.txt')


@pytest.fixture
def reference_canny():
    return parse_matlab_data('tests/data/reference_img1_canny.txt')


@pytest.fixture
def reference_sobel():
    return parse_matlab_data('tests/data/reference_img1_sobel.txt')


@pytest.fixture
def reference_marziliano():
    return parse_matlab_data('tests/data/reference_img1_marziliano.txt')


def test_marziliano_method(reference_input, reference_sobel, reference_marziliano):
    marziliano_widths = marziliano_method(reference_sobel, reference_input)

    assert np.all(marziliano_widths == reference_marziliano)


def test_calculate_sharpness_metric(reference_input, reference_canny, reference_marziliano):
    sharpness = _calculate_sharpness_metric(
        reference_input,
        reference_canny,
        reference_marziliano
    )

    assert round(sharpness, 4) == 0.1349
