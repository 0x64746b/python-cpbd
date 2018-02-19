About
=====

CPBD is a perceptual-based no-reference objective image sharpness metric
based on the cumulative probability of blur detection `developed at the
Image, Video and Usability Laboratory of Arizona State
University <https://ivulab.asu.edu/Quality/CPBD>`__.

    [The metric] is based on the study of human blur perception for
    varying contrast values. The metric utilizes a probabilistic model
    to estimate the probability of detecting blur at each edge in the
    image, and then the information is pooled by computing the
    cumulative probability of blur detection (CPBD).

This software is a Python port of the `reference MATLAB
implementation <http://lina.faculty.asu.edu/Software/CPBDM/CPBDM_Release_v1.0.zip>`__.
To approximate the behaviour of MATLAB's proprietary implementation of
the Sobel operator, it uses an implementation `inspired by GNU
Octave <https://sourceforge.net/p/octave/image/ci/default/tree/inst/edge.m#l196>`__.

References
==========

CPBD is described in detail in the following papers:

-  `N. D. Narvekar and L. J. Karam, "A No-Reference Image Blur Metric
   Based on the Cumulative Probability of Blur Detection (CPBD)," in
   IEEE Transactions on Image Processing, vol. 20, no. 9, pp. 2678-2683,
   Sept.
   2011. <http://ieeexplore.ieee.org/abstract/document/5739529/>`__
-  `N. D. Narvekar and L. J. Karam, "An Improved No-Reference Sharpness
   Metric Based on the Probability of Blur Detection," International
   Workshop on Video Processing and Quality Metrics for Consumer
   Electronics (VPQM), January 2010, http://www.vpqm.org
   (pdf) <http://events.engineering.asu.edu/vpqm/vpqm10/Proceedings_VPQM2010/vpqm_p27.pdf>`__
-  `N. D. Narvekar and L. J. Karam, "A no-reference perceptual image
   sharpness metric based on a cumulative probability of blur
   detection," 2009 International Workshop on Quality of Multimedia
   Experience, San Diego, CA, 2009, pp.
   87-91. <http://ieeexplore.ieee.org/abstract/document/5246972/>`__

Credits
=======

If you publish research results using this code, I kindly ask you to
reference the papers of the original authors of the metric as stated in
the previous section as well as their reference implementation in your
bibliography. See also the copyright statement of the reference
implementation in the `license
file <https://raw.githubusercontent.com/0x64746b/python-cpbd/master/LICENSE.txt>`__.
Thank you!

Installation
============

::

    $ pip install cpbd

Usage
=====

::

    In [1]: import cpbd

    In [2]: from scipy import ndimage

    In [3]: input_image = ndimage.imread('/tmp/LIVE_Images_GBlur/img4.bmp', mode='L')

    In [4]: cpbd.compute(input_image)
    Out[4]: 0.75343203230148048

Development
===========

::

    $ git clone git@github.com:0x64746b/python-cpbd.git
    Cloning into 'python-cpbd'...
    $ cd python-cpbd
    $ pip install -U '.[dev]'

To quickly run the tests with the invocation interpreter:

::

    $ python setup.py test

To test the library under different interpreters:

::

    $ tox

Performance
===========

The following graph visualizes the accuracy of this port in comparison
with the reference implementation when tested on the
`images <http://lina.faculty.asu.edu/Software/CPBDM/LIVE_Images_GBlur.zip>`__
of the `LIVE
database <http://live.ece.utexas.edu/research/quality/subjective.htm>`__:

.. image:: https://raw.githubusercontent.com/0x64746b/python-cpbd/master/tests/data/performance_LIVE.png
   :alt: Performance on LIVE database
