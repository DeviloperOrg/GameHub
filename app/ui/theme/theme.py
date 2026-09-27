APP_STYLE = """
/* =========================================================
   GLOBAL
========================================================= */

QMainWindow {
    background-color: #090B10;
}

QWidget {
    color: #F4F4F5;
    font-family: "Segoe UI";
    font-size: 14px;
}

QToolTip {
    background-color: #181B23;
    color: #FFFFFF;
    border: 1px solid #2A2F3A;
    padding: 6px;
}


/* =========================================================
   SIDEBAR
========================================================= */

QFrame#Sidebar {
    background-color: #0D0F14;
    border-right: 1px solid #1B1F28;
}

QLabel#Logo {
    color: #FFFFFF;
    font-size: 22px;
    font-weight: 800;
}

QLabel#LogoAccent {
    color: #8B5CF6;
}

QLabel#LogoSubtitle {
    color: #5F6675;
    font-size: 9px;
    font-weight: 600;
}


/* Navigation */

QPushButton#NavButton {
    background-color: transparent;
    color: #777F90;

    border: none;
    border-radius: 10px;

    padding: 11px 14px;

    text-align: left;

    font-size: 13px;
    font-weight: 600;
}

QPushButton#NavButton:hover {
    background-color: #151922;
    color: #E8E9ED;
}

QPushButton#NavButton:checked {
    background-color: #211936;
    color: #A78BFA;
}


/* =========================================================
   PAGE
========================================================= */

QLabel#PageTitle {
    color: #FFFFFF;
    font-size: 27px;
    font-weight: 750;
}

QLabel#PageSubtitle {
    color: #707887;
    font-size: 13px;
}


/* =========================================================
   SEARCH
========================================================= */

QLineEdit#SearchBar {
    background-color: #11141B;

    color: #E5E7EB;

    border: 1px solid #1D222C;
    border-radius: 10px;

    padding: 10px 14px;

    selection-background-color: #8B5CF6;
}

QLineEdit#SearchBar:focus {
    border: 1px solid #7C3AED;
}


/* =========================================================
   STAT CARDS
========================================================= */

QFrame#StatCard {
    background-color: #11141B;

    border: 1px solid #1C212B;
    border-radius: 14px;
}

QFrame#StatCard:hover {
    border: 1px solid #30264A;
}

QLabel#StatTitle {
    color: #737B8B;
    font-size: 11px;
    font-weight: 600;
}

QLabel#StatValue {
    color: #FFFFFF;
    font-size: 25px;
    font-weight: 750;
}

QLabel#StatExtra {
    color: #777F90;
    font-size: 11px;
}

QLabel#StatIcon {
    color: #A78BFA;
    font-size: 19px;
}


/* =========================================================
   GAME CARD
========================================================= */

QFrame#GameCard {
    background-color: #11141B;

    border: 1px solid #1C212B;
    border-radius: 14px;
}

QFrame#GameCard:hover {
    background-color: #151821;
    border: 1px solid #352951;
}

QLabel#GameCover {
    background-color: #181C25;
    color: #555D6D;

    border-radius: 10px;

    font-size: 12px;
    font-weight: 600;
}

QLabel#GameTitle {
    color: #FFFFFF;
    font-size: 15px;
    font-weight: 700;
}

QLabel#GameGenre {
    color: #7C8494;
    font-size: 11px;
}

QPushButton#PlayButton {
    background-color: #8B5CF6;
    color: #FFFFFF;

    border: none;
    border-radius: 8px;

    padding: 8px 14px;

    font-size: 11px;
    font-weight: 700;
}

QPushButton#PlayButton:hover {
    background-color: #9B72F8;
}

QPushButton#PlayButton:pressed {
    background-color: #7446D8;
}


/* =========================================================
   SECTION HEADER
========================================================= */

QLabel#SectionTitle {
    color: #FFFFFF;
    font-size: 18px;
    font-weight: 700;
}

QPushButton#ViewAllButton {
    background-color: transparent;
    color: #8B5CF6;

    border: none;

    font-size: 11px;
    font-weight: 600;
}

QPushButton#ViewAllButton:hover {
    color: #A78BFA;
}


/* =========================================================
   SCROLLBAR
========================================================= */

QScrollBar:vertical {
    background: transparent;
    width: 8px;
}

QScrollBar::handle:vertical {
    background: #292E38;
    border-radius: 4px;
}

QScrollBar::handle:vertical:hover {
    background: #3A4150;
}

QScrollBar::add-line:vertical,
QScrollBar::sub-line:vertical {
    height: 0px;
}
/* =========================================================
   INPUTS
========================================================= */

QComboBox {
    background-color: #11141B;
    color: #E5E7EB;

    border: 1px solid #1D222C;
    border-radius: 10px;

    padding: 10px;
}

QComboBox:hover {
    border: 1px solid #30264A;
}

QComboBox::drop-down {
    border: none;
}

QComboBox QAbstractItemView {
    background-color: #151821;
    color: #FFFFFF;

    border: 1px solid #2A2F3A;
    selection-background-color: #2A2042;
}

QDialog {
    background-color: #0D0F14;
}

QDialog QPushButton {
    background-color: #181C25;
    color: #D9DCE3;

    border: 1px solid #242A34;
    border-radius: 8px;

    padding: 9px 16px;
}

QDialog QPushButton:hover {
    background-color: #202530;
    border-color: #383E4B;
}
"""