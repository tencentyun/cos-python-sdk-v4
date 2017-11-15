#!/usr/bin/env python
# coding=utf-8

import sys
from setuptools import setup, find_packages

setup(name='qcloud_cos_v4',
      version='0.0.22',
      description='python sdk for tencent qcloud cos v4.0',
      long_description=open('README.rst', 'r').read(),
      license='MIT License',
      install_requires=['requests', 'six'],
      author='liuchang0812',
      author_email='liuchang0812@gmail.com',
      url='https://www.qcloud.com',
      packages=find_packages())
