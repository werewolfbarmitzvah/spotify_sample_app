#!/usr/bin/env python

from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='sampleapp',  # Required

    # Versions should comply with PEP 440:
    # https://www.python.org/dev/peps/pep-0440/
    version='1.0.0',
    description='A sample spotify app',
    packages=find_packages(exclude=['tests']),
    install_requires=['Flask',
                      'requests',
                      'python-dotenv',
                      'spotipy'],
)
