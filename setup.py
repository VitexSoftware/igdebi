# -*- coding: utf-8 -*-

from setuptools import find_packages
from setuptools import setup

setup (
       name='igdebi',
       version='0.1',
       packages=find_packages(),

       # Declare your packages' dependencies here, for eg:
       install_requires=['tqdm>=4.11', 'validators>=0.12'],

       # Fill in these to make your Egg ready for upload to
       # PyPI
       author='Vítězslav Dvořák',
       author_email='info@vitexsoftware.cz',

       url='https://github.com/VitexSoftware/igdebi',
       license='GPL',
       long_description='Download and install debian package',

       entry_points={'console_scripts': ['igdebi = igdebi.igdebi:main']}
       )
