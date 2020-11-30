# -*- coding: utf-8 -*-

"""This module provides {{ cookiecutter.app_name }} application."""

import sys

from PyQt5.QtWidgets import QApplication

from .views.window import Window


def main():
    """{{ cookiecutter.app_name }} main function."""
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
