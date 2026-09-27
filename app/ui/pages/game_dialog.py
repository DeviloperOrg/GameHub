from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QFileDialog,
    QMessageBox,
    QComboBox,
)


class AddGameDialog(QDialog):

    def __init__(self, database, parent=None):

        super().__init__(parent)

        self.database = database

        self.setWindowTitle("Add Game")
        self.setFixedSize(520, 560)

        self._build_ui()

    def _build_ui(self):

        layout = QVBoxLayout(self)

        layout.setContentsMargins(
            28, 28, 28, 28
        )

        layout.setSpacing(14)

        # ------------------------------------------
        # TITLE
        # ------------------------------------------

        title = QLabel("Add Game")

        title.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 24px;
                font-weight: 700;
            }
        """)

        subtitle = QLabel(
            "Add a game to your GameHub library."
        )

        subtitle.setStyleSheet("""
            QLabel {
                color: #737B8B;
                font-size: 12px;
            }
        """)

        layout.addWidget(title)
        layout.addWidget(subtitle)

        layout.addSpacing(12)

        # ------------------------------------------
        # GAME NAME
        # ------------------------------------------

        layout.addWidget(
            self._label("Game Name")
        )

        self.name_input = QLineEdit()

        self.name_input.setPlaceholderText(
            "e.g. Cyberpunk 2077"
        )

        self.name_input.setObjectName(
            "SearchBar"
        )

        layout.addWidget(
            self.name_input
        )

        # ------------------------------------------
        # GENRE
        # ------------------------------------------

        layout.addWidget(
            self._label("Genre")
        )

        self.genre_input = QComboBox()

        self.genre_input.addItems([
            "Action",
            "Adventure",
            "RPG",
            "FPS",
            "Racing",
            "Strategy",
            "Simulation",
            "Sports",
            "Other",
        ])

        layout.addWidget(
            self.genre_input
        )

        # ------------------------------------------
        # EXECUTABLE
        # ------------------------------------------

        layout.addWidget(
            self._label("Game Executable")
        )

        executable_layout = QHBoxLayout()

        self.executable_input = QLineEdit()

        self.executable_input.setPlaceholderText(
            "Select game .exe"
        )

        self.executable_input.setObjectName(
            "SearchBar"
        )

        browse_exe = QPushButton(
            "Browse"
        )

        browse_exe.clicked.connect(
            self._select_executable
        )

        executable_layout.addWidget(
            self.executable_input
        )

        executable_layout.addWidget(
            browse_exe
        )

        layout.addLayout(
            executable_layout
        )

        # ------------------------------------------
        # COVER
        # ------------------------------------------

        layout.addWidget(
            self._label("Cover Image")
        )

        cover_layout = QHBoxLayout()

        self.cover_input = QLineEdit()

        self.cover_input.setPlaceholderText(
            "Select cover image"
        )

        self.cover_input.setObjectName(
            "SearchBar"
        )

        browse_cover = QPushButton(
            "Browse"
        )

        browse_cover.clicked.connect(
            self._select_cover
        )

        cover_layout.addWidget(
            self.cover_input
        )

        cover_layout.addWidget(
            browse_cover
        )

        layout.addLayout(
            cover_layout
        )

        layout.addStretch()

        # ------------------------------------------
        # BUTTONS
        # ------------------------------------------

        buttons = QHBoxLayout()

        buttons.addStretch()

        cancel = QPushButton(
            "Cancel"
        )

        cancel.clicked.connect(
            self.reject
        )

        add = QPushButton(
            "Add Game"
        )

        add.setObjectName(
            "PlayButton"
        )

        add.clicked.connect(
            self._add_game
        )

        buttons.addWidget(cancel)
        buttons.addWidget(add)

        layout.addLayout(
            buttons
        )

    def _label(self, text):

        label = QLabel(text)

        label.setStyleSheet("""
            QLabel {
                color: #A5ACBA;
                font-size: 12px;
                font-weight: 600;
            }
        """)

        return label

    def _select_executable(self):

        path, _ = QFileDialog.getOpenFileName(
            self,
            "Select Game Executable",
            "",
            "Executable (*.exe)"
        )

        if path:
            self.executable_input.setText(
                path
            )

    def _select_cover(self):

        path, _ = QFileDialog.getOpenFileName(
            self,
            "Select Game Cover",
            "",
            "Images (*.png *.jpg *.jpeg *.webp)"
        )

        if path:
            self.cover_input.setText(
                path
            )

    def _add_game(self):

        name = self.name_input.text().strip()

        genre = self.genre_input.currentText()

        executable = (
            self.executable_input
            .text()
            .strip()
        )

        cover = (
            self.cover_input
            .text()
            .strip()
        )

        if not name:

            QMessageBox.warning(
                self,
                "Missing Information",
                "Please enter the game name."
            )

            return

        self.database.add_game(
            name=name,
            genre=genre,
            executable_path=executable,
            cover_path=cover
        )

        self.accept()