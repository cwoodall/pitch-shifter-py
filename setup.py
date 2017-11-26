#!/usr/bin/env python
from setuptools import setup, find_packages, Command
from distutils.util import convert_path

main_ns = {}
ver_path = convert_path('pitchshifter/version.py')
with open(ver_path) as ver_file:
    exec(ver_file.read(), main_ns)

setup(
    name='pitchshifter',
    version=main_ns['__VERSION__'],
    packages=find_packages(),
    install_requires=[
        'click',
        'numpy',
        'scipy',
        'matplotlib'
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'coverage'],
    description='Pitchshifting with python',
    author='Christopher Woodall',
    author_email='chris@cwoodall.com',
    zip_safe=False,
    entry_points={
        "console_scripts": [
            "pitchshifter=pitchshifter.pitchshifter:cli",
        ]},
)
