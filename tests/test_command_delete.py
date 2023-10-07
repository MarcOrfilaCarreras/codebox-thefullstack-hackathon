# -*- coding: utf-8 -*-
import subprocess

import pytest


def test_delete():
    command = ["python3", "codeboxcli/__main__.py", "delete"]
    result = subprocess.run(
        command, capture_output=True, text=True, check=True)

    expected_output = "Usage: codebox delete [ARGS]"

    assert expected_output in result.stdout


def test_delete_help():
    command = ["python3", "codeboxcli/__main__.py", "delete", "--help"]
    result = subprocess.run(
        command, capture_output=True, text=True, check=True)

    expected_output = "Usage: codebox delete [ARGS]"

    assert expected_output in result.stdout
