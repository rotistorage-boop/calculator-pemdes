from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt6.QtGui import QFont


class KeypadCombo(QWidget):
    """Keypad kalkulator menggunakan kombinasi QVBoxLayout dan QHBoxLayout."""

    button_clicked = pyqtSignal(str)

    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout()
        main_layout.setSpacing(8)

        font = QFont()
        font.setPointSize(18)
        font.setWeight(QFont.Weight.Medium)

        rows = [
            ["√x", "x²", "1/x", "C"],
            ["9", "8", "*", "/"],
            ["5", "4", "-", "+"],
            ["1", "0", "="],
        ]

        for row_items in rows:
            row_layout = QHBoxLayout()
            row_layout.setSpacing(8)

            for text in row_items:
                button = QPushButton(text)
                button.setMinimumHeight(90)
                if text == "C":
                  button.setStyleSheet("""
                      QPushButton {
                          background-color: #e74c3c;
                      }
                  """)
                elif text == "=":
                    button.setStyleSheet("""
                        QPushButton {
                            background-color: #2878d4;
                            color: white;
                            border: none;
                            border-radius: 8px;
                        }
                    """)
                elif text in {"0", "1", "4", "5", "8", "9"}:
                    button.setStyleSheet("""
                        QPushButton {
                            background-color: #363636;
                        }
                    """)

                button.setFont(font)
                button.clicked.connect(
                    lambda checked, t=text: self.button_clicked.emit(t)
                )

                # Tombol = lebih lebar
                stretch = 2 if text == "=" else 1
                row_layout.addWidget(button, stretch)

            main_layout.addLayout(row_layout)

        self.setLayout(main_layout)
