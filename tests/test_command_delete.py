# -*- coding: utf-8 -*-
import os
import re
import subprocess

import pytest

os.environ['LANG'] = 'en'


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


def test_delete_wrong_id():
    command = ["python3", "codeboxcli/__main__.py", "delete", "0"]
    result = subprocess.run(
        command, capture_output=True, text=True, check=True)

    expected_output = "Error: Snippet with ID 0 not found."

    assert expected_output in result.stdout


def test_delete_successful_deletion():
    command = ["python3", "codeboxcli/__main__.py", "list"]
    result = subprocess.run(
        command, capture_output=True, text=True, check=True)

    # Define a regular expression pattern to match the ID column
    id_pattern = r"\|\s+(\d+)\s+\|"

    # Find all matches of the ID pattern in the output
    id_matches = re.findall(id_pattern, result.stdout)

    if len(id_matches) >= 1:
        command = ["python3", "codeboxcli/__main__.py", "delete",
                   id_matches[0].replace("|", "").replace(" ", "")]
        result = subprocess.run(
            command, capture_output=True, text=True, check=True)

        assert result.returncode == 0
    else:
        assert 1 == 2
