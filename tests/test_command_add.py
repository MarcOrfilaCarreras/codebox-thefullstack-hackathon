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


def test_add_empty_name():
    command = ["python3", "codeboxcli/__main__.py", "add", "--name"]
    result = subprocess.run(
        command, capture_output=True, text=True, check=True)

    expected_output = "Error: Missing value after --name."

    assert expected_output in result.stdout


def test_add_empty_description():
    command = ["python3", "codeboxcli/__main__.py", "add", "--description"]
    result = subprocess.run(
        command, capture_output=True, text=True, check=True)

    expected_output = "Error: Missing value after --description."

    assert expected_output in result.stdout


def test_add_empty_tags():
    command = ["python3", "codeboxcli/__main__.py", "add", "--tags"]
    result = subprocess.run(
        command, capture_output=True, text=True, check=True)

    expected_output = "Error: Missing value after --tags."

    assert expected_output in result.stdout


def test_add_successful_addition():
    command = ["python3", "codeboxcli/__main__.py", "add", "--name", "pytest",
               "--description", "This is an automatic test", "--tags", "Python3", "Cli"]
    result = subprocess.run(
        command, capture_output=True, text=True, check=True)

    assert result.returncode == 0
