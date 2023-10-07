# -*- coding: utf-8 -*-
import subprocess

import pytest


def test_add():
    command = ["python3", "codeboxcli/__main__.py", "add"]
    result = subprocess.run(
        command, capture_output=True, text=True, check=True)

    expected_output = "Usage: codebox add [ARGS]"

    assert expected_output in result.stdout


def test_add_help():
    command = ["python3", "codeboxcli/__main__.py", "add", "--help"]
    result = subprocess.run(
        command, capture_output=True, text=True, check=True)

    expected_output = "Usage: codebox add [ARGS]"

    assert expected_output in result.stdout
