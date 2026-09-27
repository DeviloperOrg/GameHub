from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QFrame,
    QPushButton,
    QLineEdit,
)


class DashboardPage(QWidget):

    def __init__(self):
        super().__init__()

        self._build_ui()

    # ==================================================
    # MAIN UI
    # ==================================================

    def _build_ui(self):

        layout = QVBoxLayout(self)

        layout.setContentsMargins(
            34, 28, 34, 28
        )

        layout.setSpacing(24)

        # ==============================================
        # HEADER
        # ==============================================

        header = QHBoxLayout()

        title_box = QVBoxLayout()
        title_box.setSpacing(4)

        title = QLabel(
            "Good evening, BBC 👋"
        )

        title.setObjectName("PageTitle")

        subtitle = QLabel(
            "Everything you need for your gaming setup."
        )

        subtitle.setObjectName("PageSubtitle")

        title_box.addWidget(title)
        title_box.addWidget(subtitle)

        header.addLayout(title_box)

        header.addStretch()

        search = QLineEdit()

        search.setObjectName("SearchBar")

        search.setPlaceholderText(
            "Search games..."
        )

        search.setFixedWidth(230)
        search.setFixedHeight(40)

        header.addWidget(search)

        layout.addLayout(header)

        # ==============================================
        # SYSTEM STATUS
        # ==============================================

        stats_layout = QHBoxLayout()

        stats_layout.setSpacing(14)

        stats_layout.addWidget(
            self._create_stat_card(
                "CPU",
                "32%",
                "56°C",
                "◉"
            )
        )

        stats_layout.addWidget(
            self._create_stat_card(
                "GPU",
                "71%",
                "68°C",
                "◈"
            )
        )

        stats_layout.addWidget(
            self._create_stat_card(
                "MEMORY",
                "58%",
                "9.2 GB",
                "▣"
            )
        )

        layout.addLayout(stats_layout)

        # ==============================================
        # RECENT GAMES HEADER
        # ==============================================

        section_header = QHBoxLayout()

        section_title = QLabel(
            "Recently Played"
        )

        section_title.setObjectName(
            "SectionTitle"
        )

        section_header.addWidget(
            section_title
        )

        section_header.addStretch()

        view_all = QPushButton(
            "View All  →"
        )

        view_all.setObjectName(
            "ViewAllButton"
        )

        section_header.addWidget(
            view_all
        )

        layout.addLayout(section_header)

        # ==============================================
        # GAME CARDS
        # ==============================================

        games_layout = QHBoxLayout()

        games_layout.setSpacing(16)

        games_layout.addWidget(
            self._create_game_card(
                "Nioh 3",
                "RPG",
                "24h 18m"
            )
        )

        games_layout.addWidget(
            self._create_game_card(
                "GTA V",
                "Action",
                "18h 42m"
            )
        )

        games_layout.addWidget(
            self._create_game_card(
                "Skyrim",
                "RPG",
                "42h 11m"
            )
        )

        layout.addLayout(games_layout)

        # ==============================================
        # QUICK ACTIONS
        # ==============================================

        layout.addSpacing(6)

        quick_title = QLabel(
            "Quick Actions"
        )

        quick_title.setObjectName(
            "SectionTitle"
        )

        layout.addWidget(
            quick_title
        )

        actions = QHBoxLayout()

        actions.setSpacing(12)

        actions.addWidget(
            self._create_action(
                "🎮",
                "Add Game",
                "Add a new game to your library."
            )
        )

        actions.addWidget(
            self._create_action(
                "📊",
                "Performance",
                "Open system monitoring."
            )
        )

        actions.addWidget(
            self._create_action(
                "🔐",
                "Gaming Vault",
                "Manage your accounts."
            )
        )

        layout.addLayout(actions)

        layout.addStretch()

    # ==================================================
    # STAT CARD
    # ==================================================

    def _create_stat_card(
        self,
        title,
        value,
        extra,
        icon
    ):

        card = QFrame()

        card.setObjectName(
            "StatCard"
        )

        card.setMinimumHeight(125)

        layout = QVBoxLayout(card)

        layout.setContentsMargins(
            18, 16, 18, 16
        )

        # Top row
        top = QHBoxLayout()

        title_label = QLabel(title)

        title_label.setObjectName(
            "StatTitle"
        )

        icon_label = QLabel(icon)

        icon_label.setObjectName(
            "StatIcon"
        )

        top.addWidget(title_label)

        top.addStretch()

        top.addWidget(icon_label)

        layout.addLayout(top)

        # Value
        value_label = QLabel(value)

        value_label.setObjectName(
            "StatValue"
        )

        layout.addWidget(
            value_label
        )

        # Extra
        extra_label = QLabel(extra)

        extra_label.setObjectName(
            "StatExtra"
        )

        layout.addWidget(
            extra_label
        )

        return card

    # ==================================================
    # GAME CARD
    # ==================================================

    def _create_game_card(
        self,
        name,
        genre,
        playtime
    ):

        card = QFrame()

        card.setObjectName(
            "GameCard"
        )

        card.setMinimumHeight(235)

        layout = QVBoxLayout(card)

        layout.setContentsMargins(
            12, 12, 12, 12
        )

        layout.setSpacing(9)

        # Cover
        cover = QLabel(
            "GAME\nART"
        )

        cover.setObjectName(
            "GameCover"
        )

        cover.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        cover.setMinimumHeight(125)

        layout.addWidget(
            cover
        )

        # Title
        title = QLabel(name)

        title.setObjectName(
            "GameTitle"
        )

        layout.addWidget(
            title
        )

        # Genre
        genre_label = QLabel(
            f"{genre}  •  {playtime}"
        )

        genre_label.setObjectName(
            "GameGenre"
        )

        layout.addWidget(
            genre_label
        )

        # Play button
        play = QPushButton(
            "▶  PLAY"
        )

        play.setObjectName(
            "PlayButton"
        )

        play.setCursor(
            play.cursor().shape()
        )

        layout.addWidget(
            play
        )

        return card

    # ==================================================
    # QUICK ACTION
    # ==================================================

    def _create_action(
        self,
        icon,
        title,
        description
    ):

        card = QFrame()

        card.setObjectName(
            "StatCard"
        )

        card.setMinimumHeight(80)

        layout = QHBoxLayout(card)

        layout.setContentsMargins(
            15, 12, 15, 12
        )

        icon_label = QLabel(icon)

        icon_label.setStyleSheet(
            """
            QLabel {
                font-size: 20px;
                color: #A78BFA;
            }
            """
        )

        layout.addWidget(
            icon_label
        )

        text_layout = QVBoxLayout()

        title_label = QLabel(title)

        title_label.setStyleSheet(
            """
            QLabel {
                color: #FFFFFF;
                font-size: 13px;
                font-weight: 700;
            }
            """
        )

        desc_label = QLabel(description)

        desc_label.setStyleSheet(
            """
            QLabel {
                color: #666F80;
                font-size: 10px;
            }
            """
        )

        text_layout.addWidget(
            title_label
        )

        text_layout.addWidget(
            desc_label
        )

        layout.addLayout(
            text_layout
        )

        layout.addStretch()

        return card