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


def plot_sharpness(sharpness, output_file):
    rmse = np.sqrt(mean_squared_error(
        sharpness['CPBDM_Release_v1.0'],
        sharpness['python-cpbd']
    ))

    plt.style.use('ggplot')

    sharpness.plot()

    plt.title('Performance on LIVE database')
    error_box = AnchoredText('RMSE: {}'.format(rmse), loc=2)
    error_box.patch.set(
        boxstyle=plt.legend().get_frame().get_boxstyle(),
        facecolor=plt.legend().get_frame().get_facecolor(),
        edgecolor=plt.legend().get_frame().get_edgecolor(),
    )
    plt.gca().add_artist(error_box)
    plt.ylabel('sharpness')
    plt.ylim([-0.05, 1])

    plt.savefig(output_file)


def load_data(matlab_results, python_results):
    reference = pd.read_csv(matlab_results, index_col=0)
    port = pd.read_csv(python_results, index_col=0)

    # sort the files by their number instead of lexicographically
    reference = reference.loc[sorted(
        reference.index,
        key=lambda name: int(name[3:])
    )]
    port = port.loc[sorted(
        port.index,
        key=lambda name: int(name[3:])
    )]

    return pd.concat(
        [
            reference.sharpness.rename('CPBDM_Release_v1.0'),
            port.sharpness.rename('python-cpbd')
        ],
        axis=1
    )


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
       default='performance.svg',
       help='the name of the file the image should be written to'
    )

    args = parser.parse_args()

    data = load_data(args.matlab_results, args.python_results)

    plot_sharpness(data, args.output_file)
