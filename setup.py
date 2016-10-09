#!/usr/bin/env python
# coding=utf-8

import sys
from setuptools import setup, find_packages

if sys.version_info[0] != 2 or sys.version_info[1] < 6:
    sys.exit('Sorry, only python 2.6 or 2.7 is supported')

setup(name='qcloud_cos_v4',
      version='0.0.3',
      description='python sdk for tencent qcloud cos v4.0',
      license='MIT License',
      install_requires=['requests'],
      author='liuchang0812',
      author_email='liuchang0812@gmail.com.com',
      url='https://www.qcloud.com',
      packages=find_packages())
