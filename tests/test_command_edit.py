# -*- coding: utf-8 -*-
import subprocess

import pytest


def test_edit():
    command = ["python3", "codeboxcli/__main__.py", "edit"]
    result = subprocess.run(
        command, capture_output=True, text=True, check=True)

    expected_output = "Usage: codebox edit [ARGS]"

    assert expected_output in result.stdout


def test_edit_help():
    command = ["python3", "codeboxcli/__main__.py", "edit", "--help"]
    result = subprocess.run(
        command, capture_output=True, text=True, check=True)

    expected_output = "Usage: codebox edit [ARGS]"

    assert expected_output in result.stdout
