from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel


class VaultPage(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        title = QLabel("Gaming Vault")
        title.setObjectName("PageTitle")

        subtitle = QLabel(
            "Securely manage your gaming accounts."
        )
        subtitle.setObjectName("PageSubtitle")

        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addStretch()