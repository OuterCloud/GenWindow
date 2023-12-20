#!python
# -*- coding:utf-8 -*-
from __future__ import print_function
from setuptools import setup, find_packages

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name="window_auto_generator",
    version=1.2,
    author="zenkilan",
    author_email="434209210@qq.com",
    description="Auto generate a window with text browser and buttons from config info",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/OuterCloud/GenWindow",
    packages=find_packages(),
    install_requires=["requests", "PyQt5"],
    classifiers=[
        "Programming Language :: Python :: 3.8",
    ],
)
