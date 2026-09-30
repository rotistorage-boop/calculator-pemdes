from PyQt6.QtWidgets import QWidget, QPushButton, QGridLayout
from PyQt6.QtGui import QFont


class Keypad(QWidget):
    def __init__(self):
        super().__init__()

        layout = QGridLayout()
        layout.setSpacing(8)

        font = QFont()
        font.setPointSize(18)
        font.setWeight(QFont.Weight.Medium)

        buttons = [
            ("√x", 0, 0),
            ("x²", 0, 1),
            ("1/x", 0, 2),
            ("C", 0, 3),

            ("9", 1, 0),
            ("8", 1, 1),
            ("*", 1, 2),
            ("/", 1, 3),

            ("5", 2, 0),
            ("4", 2, 1),
            ("-", 2, 2),
            ("+", 2, 3),

            ("1", 3, 0),
            ("0", 3, 1),
        ]

        for text, row, column in buttons:
            button = QPushButton(text)
            button.setMinimumHeight(90)
            if text == "C":
              button.setStyleSheet("""
                  QPushButton {
                      background-color: #e74c3c;
                  }
              """)
            elif text in {"0", "1", "4", "5", "8", "9"}:
                button.setStyleSheet("""
                    QPushButton {
                        background-color: #363636;
                    }
                """)
                
            button.setFont(font)

            layout.addWidget(button, row, column)

        equal_button = QPushButton("=")
        equal_button.setMinimumHeight(90)
        layout.addWidget(equal_button, 3, 2, 1, 2) # baris 3, kolom 2, tingi 1, lebar 2 kolom
        equal_button.setFont(font)
        equal_button.setStyleSheet("""
            QPushButton {
                background-color: #2878d4;
                color: white;
                border: none;
                border-radius: 8px;
            }
        """)

        self.setLayout(layout)