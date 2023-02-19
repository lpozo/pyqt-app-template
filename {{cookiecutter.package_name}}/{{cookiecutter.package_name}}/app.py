"""This module provides {{ cookiecutter.app_name }} application."""

import sys

from PyQt6.QtWidgets import QApplication

from {{ cookiecutter.app_name }}.gui.window import Window


def main():
    """Create the {{ cookiecutter.app_name }} app and run its main loop."""
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())
