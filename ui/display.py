from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLineEdit


class Display(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 0)

        self.result = QLineEdit("0")
        self.result.setReadOnly(True)
        self.result.setAlignment(Qt.AlignmentFlag.AlignRight)

        font = QFont()
        font.setPointSize(48)
        font.setWeight(font.Weight.DemiBold)
        self.result.setFont(font)

        self.result.setStyleSheet("""
            QLineEdit {
                border: none;
                background: transparent;
            }
        """)

        layout.addWidget(
            self.result,
            alignment=Qt.AlignmentFlag.AlignTop
            | Qt.AlignmentFlag.AlignRight
        )

        layout.addStretch()