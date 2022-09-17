"""This module provides tests."""

import pytest
from {{cookiecutter.package_name}}.core import Model

# Add your tests here...


def test_set_data(self):
    model = Model()
    model.setData("Data")
    assert model.data() == "Data"
