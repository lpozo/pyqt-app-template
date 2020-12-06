# -*- coding: utf-8 -*-

"""This module provides tests."""

from {{cookiecutter.package_name}}.model.model import Model

import pytest


class TestModel:
    # Add your tests here...

    def test_model(self):
        model = Model()
        model.setData("Data")
        assert model.data() == "Data"
