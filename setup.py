# -*- coding: utf-8 -*-
from setuptools import find_packages
from setuptools import setup

setup(
    name="codeboxcli",
    version="{{VERSION_PLACEHOLDER}}",
    packages=find_packages(),
    install_requires=[
        "sqlalchemy",
        "tabulate"
    ],
    entry_points={
        "console_scripts": [
            "codebox=codeboxcli.__main__:cli",
        ],
    },
)
