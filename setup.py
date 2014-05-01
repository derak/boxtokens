#!/usr/bin/env python

from distutils.core import setup


def read(filename):
    return open(filename).read()

setup(name="boxtokens",
      version="0.0.1",
      description="Basic module for interacting with the Box.com API",
      long_description=read("README.md"),
      author="Derak Berreyesa",
      author_email="derak.berreyesa@gmail.com",
      maintainer="Derak Berreyesa",
      maintainer_email="derak.berreyesa@gmail.com",
      url="https://github.com/derak/boxtokens",
      download_url="https://github.com/derak/boxtokens",
      classifiers=("Development Status :: 3 - Alpha",
                   "Intended Audience :: Developers",
                   "License :: OSI Approved :: MIT License",
                   "Operating System :: OS Independent",
                   "Programming Language :: Python",
                   "Programming Language :: Python :: 2.6",
                   "Programming Language :: Python :: 2.7"),
      license=read("LICENSE"),
      py_modules=['boxtokens'],
      )
