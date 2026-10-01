
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QAction, QIcon, QKeySequence, QShortcut
from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QTabWidget,
    QPushButton,
    QMenu,
    QStyle,
)

from logic.calculator import Calculator
from ui.display import Display
from ui.keypad_grid import KeypadGrid
from ui.keypad_combo import KeypadCombo


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Kalkulator")
        self.setWindowIcon(QIcon("assets/icons/calculator.png"))
        self.resize(500, 600)

        # Logika kalkulator per tab
        self.calc1 = Calculator()
        self.calc2 = Calculator()

        # Widget tab
        self.tabs = QTabWidget()
        self.tabs.setTabPosition(QTabWidget.TabPosition.North)
        self.tabs.setMovable(True)
        self.tabs.setDocumentMode(True)

        # Tab 1: layout Grid
        tab1 = QWidget()
        tab1_layout = QVBoxLayout(tab1)

        self.display1 = Display()
        self.keypad1 = KeypadGrid()

        self.keypad1.button_clicked.connect(
            lambda text: self._handle_button(
                self.calc1, self.display1, text
            )
        )

        tab1_layout.addWidget(self.display1)
        tab1_layout.addWidget(self.keypad1)

        # Tab 2: layout kombinasi VBox + HBox
        tab2 = QWidget()
        tab2_layout = QVBoxLayout(tab2)

        self.display2 = Display()
        self.keypad2 = KeypadCombo()

        self.keypad2.button_clicked.connect(
            lambda text: self._handle_button(
                self.calc2, self.display2, text
            )
        )

        tab2_layout.addWidget(self.display2)
        tab2_layout.addWidget(self.keypad2)

        self.tabs.addTab(tab1, "Grid")
        self.tabs.addTab(tab2, "Kombinasi")

        self.setCentralWidget(self.tabs)

        # Ikon bantuan di pojok tab
        self._setup_corner_menu()

        # Shortcut keyboard
        self._setup_shortcuts()

    def _setup_corner_menu(self):
        """Tombol ikon bantuan di pojok kanan atas tab, posisi pas di tengah."""
        icon = self.style().standardIcon(
            QStyle.StandardPixmap.SP_MessageBoxQuestion
        )

        self.help_btn = QPushButton()
        self.help_btn.setIcon(icon)
        self.help_btn.setIconSize(QSize(20, 20))
        self.help_btn.setFixedSize(28, 28)
        self.help_btn.setStyleSheet("""
            QPushButton {
                border: none;
                padding: 0px;
                margin: 4px;
            }
        """)
        self.help_btn.clicked.connect(self._show_help_menu)

        self.tabs.setCornerWidget(
            self.help_btn,
            Qt.Corner.TopRightCorner
        )

    def _show_help_menu(self):
        """Tampilkan menu navigasi tab saat ikon diklik."""
        menu = QMenu(self)

        tab1_action = QAction("Tab Grid\tCtrl+1", self)
        tab1_action.triggered.connect(
            lambda: self.tabs.setCurrentIndex(0)
        )
        menu.addAction(tab1_action)

        tab2_action = QAction("Tab Kombinasi\tCtrl+2", self)
        tab2_action.triggered.connect(
            lambda: self.tabs.setCurrentIndex(1)
        )
        menu.addAction(tab2_action)

        help_btn = self.sender()
        if help_btn:
            menu.exec(
                help_btn.mapToGlobal(
                    help_btn.rect().bottomLeft()
                )
            )

    def _setup_shortcuts(self):
        """Shortcut keyboard untuk pindah tab."""
        shortcut1 = QShortcut(QKeySequence("Ctrl+1"), self)
        shortcut1.activated.connect(
            lambda: self.tabs.setCurrentIndex(0)
        )

        shortcut2 = QShortcut(QKeySequence("Ctrl+2"), self)
        shortcut2.activated.connect(
            lambda: self.tabs.setCurrentIndex(1)
        )

    def _handle_button(
        self,
        calc: Calculator,
        display: Display,
        text: str,
    ):
        """Proses klik tombol kalkulator."""
        if text in {"0", "1", "4", "5", "8", "9"}:
            result = calc.input_number(text)
        elif text in {"+", "-", "*", "/"}:
            result = calc.input_operator(text)
        elif text == "=":
            result = calc.calculate()
        elif text == "C":
            result = calc.clear()
        elif text == "√x":
            result = calc.square_root()
        elif text == "x²":
            result = calc.square()
        elif text == "1/x":
            result = calc.reciprocal()
        else:
            return

        display.set_text(result)