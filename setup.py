#!/usr/bin/env python

# ----------------------------------------------------------------------------
# Copyright (c) 2014--, streaz development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
# ----------------------------------------------------------------------------

PACKAGE = "streaz"
NAME = "streaz"
DESCRIPTION = "Python package for ncRNA annotation"
AUTHOR = "streaz development team"
AUTHOR_EMAIL = "zhenjiang.xu@gmail.com"
URL = "https://github.com/RNAer/streaz"
VERSION = __import__(PACKAGE).__version__

from setuptools import setup, find_packages  # Always prefer setuptools over distutils
from codecs import open  # To use a consistent encoding
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name = NAME,

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # http://packaging.python.org/en/latest/tutorial.html#version
    version = VERSION,

    # What does your project relate to?
    keywords=['RNA', 'Bioinformatics'],

    description = DESCRIPTION,

    long_description=long_description,

    # The project's main homepage.
    url = URL,

    # Author details
    author = AUTHOR,
    author_email = AUTHOR_EMAIL,

    # Choose your license
    license = 'BSD',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 2 - Pre-Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Intended Audience :: Bioinformatician',

        'Topic :: Software Development :: Libraries',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Bio-Informatics',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: BSD License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),

    # List run-time dependencies here.  These will be installed by pip when your
    # project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/technical.html#install-requires-vs-requirements-files
    install_requires=['numpy >= 1.7', 'matplotlib >= 1.1.0',
                      'scipy >= 0.13.0',
                      'scikit-bio', 'scikit-learn',
                      'pandas', 'future'],
    extras_require={'test': ["nose >= 0.10.1", "pep8", "flake8"],
                    'doc':  ["Sphinx >= 1.2.2", "sphinx-bootstrap-theme"]},

    # If there are data files included in your packages that need to be
    # installed, specify them here. If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    package_data={
        'streaz': ['models/*'],
    },

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
        'console_scripts': [
            'streaz=streaz.run:test',
        ],
    },

    test_suite='nose.collector'
)
