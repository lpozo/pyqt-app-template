"""This module provides {{ cookiecutter.app_name }} application."""

import sys

from PyQt6.QtWidgets import QApplication

from gui.window import Window


def main():
    """Create the {{ cookiecutter.app_name }} app and run its main loop."""
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
