#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Hao Luo at 2/11/20

"""setup.py
:description : script
:param : 
:returns: 
:rtype: 
"""
from __future__ import absolute_import

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="gemstool",
    version="0.0.2.1",
    author="Hao Luo",
    author_email="bioluohao@outlook.com",
    description="some small tools for my modeling work",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/HaoLuoChalmers/gemstool",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        # "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)