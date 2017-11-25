#!/usr/bin/python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': '',
    'author': 'Christopher Woodall',
    'url': '',
    'download_url': '',
    'author_email': 'chris@cwoodall.com',
    'version': '0.2.0',
    'install_requires': ['numpy', 'scipy', 'matplotlib'],
    'packages': ['pitchshifter'],
    'scripts': ['bin/pitch-shifter.py'],
    'name': 'pitch-shifter',
    'test_suite': 'nose.collector'
}

setup(**config)
