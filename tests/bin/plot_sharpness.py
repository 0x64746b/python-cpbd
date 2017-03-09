#!/usr/bin/env python3
# coding: utf-8

"""
Plot the sharpness values calculated by the MATLAB reference implementation vs
the ones calculated by the `python-cpbd` port.
"""

import argparse

from matplotlib import pyplot as plt
from matplotlib.offsetbox import AnchoredText
import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error


def plot_sharpness(reference, port, output_file):
    rmse = np.sqrt(mean_squared_error(reference.sharpness, port.sharpness))

    plt.style.use('ggplot')

    plt.plot(reference.sharpness.values, label='CPBDM_Release_v1.0')
    plt.plot(port.sharpness.values, label='python-cpbd')

    plt.title('Performance on LIVE database')
    plt.gca().add_artist(AnchoredText('RMSE: {}'.format(rmse), loc=2))
    plt.legend()
    plt.xlabel('img')
    plt.ylabel('sharpness')
    plt.ylim([-0.05, 1])

    plt.savefig(output_file)


def load_data(matlab_results, python_results):
    reference_sharpness = pd.read_csv(matlab_results, index_col=0)
    port_sharpness = pd.read_csv(python_results, index_col=0)

    # sort the files by their number instead of lexicographically
    reference_sharpness = reference_sharpness.loc[
        sorted(reference_sharpness.index, key=lambda name: int(name[3:]))
    ]
    port_sharpness = port_sharpness.loc[
        sorted(port_sharpness.index, key=lambda name: int(name[3:]))
    ]

    return reference_sharpness, port_sharpness


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
       'matlab_results',
       help='the .csv file containing the values calculated by the MATLAB'
            ' reference implemenation'
    )
    parser.add_argument(
       'python_results',
       help='the .csv file containing the values calculated by the `python-cpbd`'
            ' port'
    )
    parser.add_argument(
       '-o',
       '--output-file',
       default='performance.png',
       help='the name of the file the image should be written to'
    )

    args = parser.parse_args()

    data = load_data(args.matlab_results, args.python_results)

    plot_sharpness(*data, args.output_file)
