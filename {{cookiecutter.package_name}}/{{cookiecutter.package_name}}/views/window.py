"""This module provides {{ cookiecutter.app_name }} main window."""

from PyQt5.QtWidgets import QAction, QMainWindow, QMessageBox, QVBoxLayout, QWidget

from {{cookiecutter.package_name}}.model.model import Model


class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("{{ cookiecutter.app_name }}")
        self.setupUI()
        # Model to access and modify data
        self.mode = Model()

    # GUI (View)
    def setupUI(self):
        self._createCentralWidget()
        self._createActions()
        self._connectActions()
        self._createMainMenu()
        self._createStatusBar()

    def _createCentralWidget(self):
        # Add a central widget, the following is just a placeholder...
        self.centralWidget = QWidget()
        self.mainLayout = QVBoxLayout()
        self.centralWidget.setLayout(self.mainLayout)

    def _createActions(self):
        self.exitAction = QAction("&Exit", self)
        self.aboutAction = QAction("About...", self)

    def _connectActions(self):
        self.exitAction.triggered.connect(self.close)
        self.aboutAction.triggered.connect(self.about)
        # Connect more signals and slots here...

    def _createMainMenu(self):
        mainMenuBar = self.menuBar()
        # File menu
        fileMenu = mainMenuBar.addMenu("&File")
        fileMenu.addAction(self.exitAction)
        # Help menu
        helpMenu = mainMenuBar.addMenu("&Help")
        helpMenu.addAction(self.aboutAction)
        # Add more menus here...

    def _createStatusBar(self):
        self.statusbar = self.statusBar()
        # Temporary message
        self.statusbar.showMessage("Ready", 3000)

    # Slots (Controller)
    def about(self):
        QMessageBox.about(
            self,
            "About {{ cookiecutter.app_name }}",
            "{{ cookiecutter.app_name }} is...",
        )
