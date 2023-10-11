# -*- coding: utf-8 -*-
import os
import subprocess

import pytest

os.environ['LANG'] = 'en'


def test_share():
    command = ["python3", "codeboxcli/__main__.py", "share"]
    result = subprocess.run(
        command, capture_output=True, text=True, check=True)

    expected_output = "Usage: codebox share SNIPPET_ID [ARGS]"

    assert expected_output in result.stdout


def test_share_help():
    command = ["python3", "codeboxcli/__main__.py", "share", "--help"]
    result = subprocess.run(
        command, capture_output=True, text=True, check=True)

    expected_output = "Usage: codebox share SNIPPET_ID [ARGS]"

    assert expected_output in result.stdout
