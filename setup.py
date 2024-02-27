'''
Copyright (c) 2024 MPI-M, Clara Bayley

----- GoodSciProjTemplate -----
File: setup.py
Project: goodsciprojtemplate
Created Date: Tuesday 27th February 2024
Author: Clara Bayley (CB)
Additional Contributors:
-----
Last Modified: Tuesday 27th February 2024
Modified By: CB
-----
License: BSD 3-Clause "New" or "Revised" License
https://opensource.org/licenses/BSD-3-Clause
-----
File Description:
setup for pre-commit tool
'''


from setuptools import setup, find_packages

setup(
    name='GoodSciProjTemplate',
    version='0.0.0',
    packages=find_packages(),
    install_requires=[
        'pytest',
        'sphinx',
    ],
)
