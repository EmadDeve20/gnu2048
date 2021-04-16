#!/bin/env python3

import setuptools

ffile = open("README.md", "r")
long_description = ffile.read()
ffile.close()

setuptools.setup(
    name="gnu2048",
    version="1.0.0",
    author="EmadDeve20",
    license='GPLv3+',
    author_email="emaddeve20@gmail.com",
    description="this is an open source 2048 game",
    long_description=long_description,
    install_requires="readchar=2.0.1",
    long_description_content_type="text/markdown",
    url="https://github.com/EmadDeve20/gnu2048",
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "gnu2048"},
    packages=setuptools.find_packages(where="gnu2048"),
    python_requires=">=3.6",
)

