# -*- coding: utf-8 -*-
from setuptools import find_packages
from setuptools import setup

setup(
    name="codebox",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "sqlalchemy",
        "tabulate"
    ],
    entry_points={
        "console_scripts": [
            "codebox = app.__main__:cli",
        ],
    },
)
