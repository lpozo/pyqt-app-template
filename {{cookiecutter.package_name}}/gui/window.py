"""This module provides {{ cookiecutter.app_name }} main window."""

from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMainWindow, QMessageBox, QVBoxLayout, QWidget
from {{cookiecutter.package_name}}.core import Model


class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("{{ cookiecutter.app_name }}")
        self.setupUI()
        self.mode = Model()

    # View
    def setupUI(self):
        self._createCentralWidget()
        self._createActions()
        self._connectActions()
        self._createMainMenu()
        self._createStatusBar()

    def _createCentralWidget(self):
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        self.mainLayout = QVBoxLayout()
        centralWidget.setLayout(self.mainLayout)
        # Add widgets to your gui here...

    def _createActions(self):
        self.exitAction = QAction("&Exit", self)
        self.aboutAction = QAction("About...", self)
        # Add more actions here...

    def _connectActions(self):
        self.exitAction.triggered.connect(self.close)
        self.aboutAction.triggered.connect(self.about)
        # Connect more signals and slots here...

    def _createMainMenu(self):
        mainMenuBar = self.menuBar()
        # File menu
        fileMenu = mainMenuBar.addMenu("&File")
        fileMenu.addAction(self.exitAction)
        # Add more menus here...
        # Help menu
        helpMenu = mainMenuBar.addMenu("&Help")
        helpMenu.addAction(self.aboutAction)

    def _createStatusBar(self):
        self.statusbar = self.statusBar()
        # Set up your status bar here...
        self.statusbar.showMessage("Ready", 3000)  # Placeholder message

    # Controller
    def about(self):
        QMessageBox.about(
            self,
            "About {{ cookiecutter.app_name }}",
            "{{ cookiecutter.app_name }} is...",
        )
