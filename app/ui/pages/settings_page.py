from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel


class SettingsPage(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel("Settings")
        title.setObjectName("PageTitle")

        subtitle = QLabel(
            "Customize your GameHub experience."
        )
        subtitle.setObjectName("PageSubtitle")

        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addStretch()