import os
import subprocess
from pathlib import Path
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QLineEdit,
    QGridLayout,
    QFrame,
    QMessageBox,
)

import subprocess

from app.ui.pages.game_dialog import AddGameDialog


class GameCard(QFrame):

    def __init__(self, game, database, parent=None):

        super().__init__(parent)

        self.game = game
        self.database = database

        self.setObjectName(
            "GameCard"
        )

        self.setMinimumHeight(310)

        self._build_ui()

    def _build_ui(self):

        layout = QVBoxLayout(self)

        layout.setContentsMargins(
            12, 12, 12, 12
        )

        layout.setSpacing(8)

        # ------------------------------------------
        # COVER
        # ------------------------------------------

        cover = QLabel()

        cover.setObjectName(
            "GameCover"
        )

        cover.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        cover.setMinimumHeight(160)

        cover_path = self.game["cover_path"]

        if cover_path:

            pixmap = QPixmap(
                cover_path
            )

            if not pixmap.isNull():

                pixmap = pixmap.scaled(
                    400,
                    160,
                    Qt.AspectRatioMode.KeepAspectRatioByExpanding,
                    Qt.TransformationMode.SmoothTransformation
                )

                cover.setPixmap(
                    pixmap
                )

        else:

            cover.setText(
                "GAME\nART"
            )

        layout.addWidget(
            cover
        )

        # ------------------------------------------
        # NAME
        # ------------------------------------------

        name = QLabel(
            self.game["name"]
        )

        name.setObjectName(
            "GameTitle"
        )

        layout.addWidget(
            name
        )

        # ------------------------------------------
        # GENRE
        # ------------------------------------------

        genre = QLabel(
            self.game["genre"] or "Unknown"
        )

        genre.setObjectName(
            "GameGenre"
        )

        layout.addWidget(
            genre
        )

        layout.addStretch()

        # ------------------------------------------
        # BUTTONS
        # ------------------------------------------

        buttons = QHBoxLayout()

        play = QPushButton(
            "▶  PLAY"
        )

        play.setObjectName(
            "PlayButton"
        )

        play.clicked.connect(
            self._launch_game
        )

        delete = QPushButton(
            "×"
        )

        delete.setFixedWidth(38)

        delete.setStyleSheet("""
            QPushButton {
                background-color: #191D25;
                color: #8B93A3;
                border: none;
                border-radius: 8px;
                font-size: 18px;
            }

            QPushButton:hover {
                background-color: #3A1D25;
                color: #F87171;
            }
        """)

        delete.clicked.connect(
            self._delete_game
        )

        buttons.addWidget(
            play
        )

        buttons.addWidget(
            delete
        )

        layout.addLayout(
            buttons
        )

    def _launch_game(self):

        path = self.game["executable_path"]
        if not path:

            QMessageBox.warning(
            self,
            "Game Path Missing",
            f"No executable path has been configured for "
            f"'{self.game['name']}'.\n\n"
            "Edit the game and select its .exe file."
        )

            return

        path = os.path.normpath(path)

        if not os.path.isfile(path):

            QMessageBox.critical(
                self,
                "Game Not Found",
                f"The executable could not be found:\n\n"
                f"{path}\n\n"
                "The game may have been moved or uninstalled."
            )

            return


        executable = Path(path)

        working_directory = str(
            executable.parent
        )



        try:

            subprocess.Popen(
                [str(executable)],
                cwd=working_directory,
                shell=False
            )

        except PermissionError:

            QMessageBox.critical(
                self,
                "Permission Error",
                "Windows blocked GameHub from launching "
                "this game."
            )

        except FileNotFoundError:

            QMessageBox.critical(
                self,
                "Launch Error",
                "The game executable could not be found."
            )

        except Exception as error:

            QMessageBox.critical(
                self,
                "Launch Error",
                f"Could not launch the game.\n\n"
                f"{error}"
            )

    def _delete_game(self):

        result = QMessageBox.question(
            self,
            "Delete Game",
            f"Remove '{self.game['name']}' "
            "from your library?"
        )

        if result != QMessageBox.StandardButton.Yes:
            return

        self.database.delete_game(
            self.game["id"]
        )

        self.parent().refresh()


class GamesPage(QWidget):

    def __init__(self, database):

        super().__init__()

        self.database = database

        self._build_ui()

        self.refresh()

    def _build_ui(self):

        layout = QVBoxLayout(self)

        layout.setContentsMargins(
            34, 28, 34, 28
        )

        layout.setSpacing(20)

        # ------------------------------------------
        # HEADER
        # ------------------------------------------

        header = QHBoxLayout()

        title_box = QVBoxLayout()

        title = QLabel(
            "Game Library"
        )

        title.setObjectName(
            "PageTitle"
        )

        subtitle = QLabel(
            "Manage and launch your games."
        )

        subtitle.setObjectName(
            "PageSubtitle"
        )

        title_box.addWidget(title)
        title_box.addWidget(subtitle)

        header.addLayout(
            title_box
        )

        header.addStretch()

        self.search = QLineEdit()

        self.search.setObjectName(
            "SearchBar"
        )

        self.search.setPlaceholderText(
            "Search games..."
        )

        self.search.setFixedWidth(
            250
        )

        self.search.textChanged.connect(
            self.refresh
        )

        header.addWidget(
            self.search
        )

        add_button = QPushButton(
            "+  Add Game"
        )

        add_button.setObjectName(
            "PlayButton"
        )

        add_button.clicked.connect(
            self._open_add_dialog
        )

        header.addWidget(
            add_button
        )

        layout.addLayout(
            header
        )

        # ------------------------------------------
        # GAME GRID
        # ------------------------------------------

        self.grid = QGridLayout()

        self.grid.setSpacing(16)

        layout.addLayout(
            self.grid
        )

        layout.addStretch()

    def refresh(self):

        # Remove existing cards

        while self.grid.count():

            item = self.grid.takeAt(0)

            widget = item.widget()

            if widget:
                widget.deleteLater()

        games = self.database.get_games()

        query = (
            self.search.text()
            .strip()
            .lower()
        )

        if query:

            games = [
                game
                for game in games
                if query in game["name"].lower()
            ]

        columns = 3

        for index, game in enumerate(games):

            row = index // columns
            column = index % columns

            card = GameCard(
                game,
                self.database,
                self
            )

            self.grid.addWidget(
                card,
                row,
                column
            )

        if not games:

            empty = QLabel(
                "No games found.\n\n"
                "Click '+ Add Game' to add your first game."
            )

            empty.setAlignment(
                Qt.AlignmentFlag.AlignCenter
            )

            empty.setStyleSheet("""
                QLabel {
                    color: #606978;
                    font-size: 14px;
                }
            """)

            self.grid.addWidget(
                empty,
                0,
                0,
                1,
                3
            )

    def _open_add_dialog(self):

        dialog = AddGameDialog(
            self.database,
            self
        )

        if dialog.exec():

            self.refresh()