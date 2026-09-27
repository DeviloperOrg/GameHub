from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import (
    QFrame,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QButtonGroup,
    QSizePolicy,
)


class Sidebar(QFrame):

    page_changed = pyqtSignal(str)

    def __init__(self):
        super().__init__()

        self.setObjectName("Sidebar")
        self.setFixedWidth(220)

        self.button_group = QButtonGroup(self)
        self.button_group.setExclusive(True)

        self._build_ui()

    def _build_ui(self):

        layout = QVBoxLayout(self)

        layout.setContentsMargins(16, 24, 16, 18)
        layout.setSpacing(5)


        # LOGO


        logo = QLabel("GAMEHUB")
        logo.setObjectName("Logo")

        subtitle = QLabel("GAMING COMPANION")
        subtitle.setObjectName("LogoSubtitle")

        layout.addWidget(logo)
        layout.addWidget(subtitle)

        layout.addSpacing(32)

        # MAIN NAVIGATION

        self._add_button(
            layout,
            "⌂    Home",
            "dashboard",
            checked=True
        )

        self._add_button(
            layout,
            "◈    Games",
            "games"
        )

        self._add_button(
            layout,
            "◉    Performance",
            "performance"
        )

        self._add_button(
            layout,
            "▣    Gaming Vault",
            "vault"
        )

        layout.addStretch()


        # SETTINGS


        self._add_button(
            layout,
            "⚙    Settings",
            "settings"
        )

    def _add_button(
        self,
        layout,
        text,
        page,
        checked=False
    ):

        button = QPushButton(text)

        button.setObjectName("NavButton")

        button.setCheckable(True)
        button.setChecked(checked)

        button.setCursor(
            button.cursor().shape()
        )

        button.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Fixed
        )

        button.setMinimumHeight(42)

        button.clicked.connect(
            lambda: self.page_changed.emit(page)
        )

        self.button_group.addButton(button)

        layout.addWidget(button)