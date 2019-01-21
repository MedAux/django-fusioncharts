# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='django-fusioncharts',
    version='3.13.3-sr.1',
    include_package_data=True,
    packages=find_packages(),
    install_requires=[
        'Django',
    ],
    description='Fusion Charts v3.13.3-sr.1 and Django wrapper for it.'
)
