#!python
# -*- coding:utf-8 -*-
from __future__ import print_function
from setuptools import setup, find_packages
import generator

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name="window_generator",
    version=1.0,
    author="zenkilan",
    author_email="434209210@qq.com",
    description="auto create window browser with config info",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/OuterCloud",
    packages=find_packages(),
    install_requires=["requests", "PyQt5"],
    classifiers=[
        "Programming Language :: Python :: 3.8",
    ],
)
