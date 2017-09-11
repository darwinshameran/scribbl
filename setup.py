#!/usr/bin/env python3
#  vim: set ts=4 sw=4 tw=79 ft=python et :
"""scribbl setup"""

import sys
from codecs import open
from os import path
from setuptools import setup

__version__ = "1.0.1"
PACKAGE_NAME = "scribbl"
HERE = path.abspath(path.dirname(__file__))

if sys.version_info < (3, 5):
    raise SystemExit("Python 3.5 or later is required to run scribbl, exiting.")

with open(path.join(HERE, "README.rst"), encoding="utf-8") as f:
    README = f.read()

setup(name=PACKAGE_NAME,
      author="dxsh",
      author_email="dxsh@riseup.net",
      description="Download image-based documents from scribd.com.",
      classifiers=[
          "Environment :: Console",
          "Topic :: Utilities",
          "Programming Language :: Python :: 3.5",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: Implementation :: CPython"],
      install_requires=["requests==2.18.1", "img2pdf==0.2.4"],
      keywords="scribd",
      license="MIT",
      url="https://github.com/dxsh/scribbl",
      packages=["scribbl"],
      scripts=["scribbl/scribbl"],
      version=__version__)
