#!/usr/bin/env python

from __future__ import absolute_import, print_function, unicode_literals

# Always prefer setuptools over distutils
import setuptools

# To use a consistent encoding
from codecs import open
from os import path


here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


setuptools.setup(
    name = 'cpbd',
    version = '1.0.7',
    description = 'Calculate the sharpness of an image with the CPBD metric',
    long_description = long_description,
    url = 'https://github.com/0x64746b/python-cpbd',
    author = 'D.',
    author_email = 'dtk@gmx.de',
    license='Other/Proprietary License',

    keywords = [
        'sharpness',
        'metric',
        'blur',
        'cumulative probability',
        'no-reference',
        'objective',
        'perceptual',
    ],

    classifiers = [
        'Development Status :: 5 - Production/Stable',

        # Indicate who your project is intended for
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering',

        # Pick your license as you wish (should match "license" above)
        'License :: Other/Proprietary License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    packages = ['cpbd'],
    setup_requires = [
        'pytest-runner',
        'pypandoc>=1.4',
    ],
    install_requires = [
        'matplotlib>=2.0.0',  # This should be a dependency of `scikit-image`
        'numpy>=1.11.1',
        'scikit-image>=0.12.3',
        'scipy>=0.18.1',
    ],
    tests_require = ['pytest'],
    extras_require = {
        'dev': [
            'pandas>=0.19.2',
            'pytest>=3.0.0',
            'scikit-learn>=0.18.1',
            'tox>=2.9.1',
        ],
    },
)
