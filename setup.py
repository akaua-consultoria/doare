# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 09:36:13 2023

@author: nfama
"""

from setuptools import setup, find_packages

setup(
    name="doare",
    version="0.1",
    description="Um pacote para acesso aos dados de doações da Doare",
    author="Nathália Martins",
    author_email="nathalia@akaua.com.br",
    packages=find_packages(),
		install_requires=[
        'pandas',
        'requests'
    ],
)