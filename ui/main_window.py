from PyQt6.QtGui import QIcon 
from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout

from ui.display import Display
from ui.keypad import Keypad


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Kalkulator")
        self.setWindowIcon(QIcon("assets/icons/calculator.png"))
        self.resize(500, 600)

        menu = self.menuBar()
        file_menu = menu.addMenu("&Tab")
        file_menu.addAction("Tab 1")
        file_menu.addAction("Tab 2")

        central = QWidget()
        layout = QVBoxLayout()

        display = Display()
        layout.addWidget(display)

        keypad = Keypad()
        layout.addWidget(keypad)

        central.setLayout(layout)
        self.setCentralWidget(central)