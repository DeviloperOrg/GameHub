from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QStackedWidget,
)

from app.database.database import Database

from app.ui.theme import APP_STYLE
from app.ui.widgets.sidebar import Sidebar

from app.ui.pages.dashboard import DashboardPage
from app.ui.pages.games_page import GamesPage
from app.ui.pages.performance_page import PerformancePage
from app.ui.pages.vault_page import VaultPage
from app.ui.pages.settings_page import SettingsPage


class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle(
            "GameHub"
        )

        self.resize(
            1400,
            820
        )

        self.setMinimumSize(
            1100,
            700
        )

        self.setStyleSheet(
            APP_STYLE
        )

        # Database
        self.database = Database()

        self._build_ui()

    def _build_ui(self):

        central = QWidget()

        self.setCentralWidget(
            central
        )

        main_layout = QHBoxLayout(
            central
        )

        main_layout.setContentsMargins(
            0, 0, 0, 0
        )

        main_layout.setSpacing(0)


        self.sidebar = Sidebar()

        main_layout.addWidget(
            self.sidebar
        )


        self.pages = QStackedWidget()

        self.dashboard_page = (
            DashboardPage()
        )

        self.games_page = GamesPage(
            self.database
        )

        self.performance_page = (
            PerformancePage()
        )

        self.vault_page = (
            VaultPage()
        )

        self.settings_page = (
            SettingsPage()
        )

        self.pages.addWidget(
            self.dashboard_page
        )

        self.pages.addWidget(
            self.games_page
        )

        self.pages.addWidget(
            self.performance_page
        )

        self.pages.addWidget(
            self.vault_page
        )

        self.pages.addWidget(
            self.settings_page
        )

        main_layout.addWidget(
            self.pages
        )

        # Navigation

        self.sidebar.page_changed.connect(
            self.change_page
        )

    def change_page(self, page):

        pages = {
            "dashboard": 0,
            "games": 1,
            "performance": 2,
            "vault": 3,
            "settings": 4,
        }

        index = pages.get(page)

        if index is not None:

            self.pages.setCurrentIndex(
                index
            )

    def closeEvent(self, event):

        self.database.close()

        event.accept()