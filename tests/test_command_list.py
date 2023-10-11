# -*- coding: utf-8 -*-
import os
import subprocess

import pytest

os.environ['LANG'] = 'en'


def test_list():
    command = ["python3", "codeboxcli/__main__.py", "list"]
    result = subprocess.run(
        command, capture_output=True, text=True, check=True)

    expected_output_id = "ID"
    expected_output_name = "NAME"
    expected_output_content = "CONTENT"
    expected_output_tags = "TAGS"

    assert expected_output_id in result.stdout
    assert expected_output_name in result.stdout
    assert expected_output_content in result.stdout
    assert expected_output_tags in result.stdout
