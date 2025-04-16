from PySide6.QtWidgets import QWidget, QGridLayout, QHBoxLayout, QVBoxLayout
from tuyau_key import Key

class Grille(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        lv = QVBoxLayout()
        lh = QHBoxLayout()
        lg = QGridLayout()

        self.setWindowTitle("Jeu du tuyau")
        self.setMinimumSize(600, 600)

        lh1 = QHBoxLayout()
        lh2 = QHBoxLayout()
        lh3 = QHBoxLayout()
        lh4 = QHBoxLayout()

#Ligne 1
        case1 = Key(" ")
        lh1.addWidget(case1)

        case2 = Key(" ")
        lh1.addWidget(case2)

        case3 = Key(" ")
        lh1.addWidget(case3)

        case4 = Key(" ")
        lh1.addWidget(case4)

# Ligne 2
        case5 = Key(" ")
        lh2.addWidget(case5)

        case6 = Key(" ")
        lh2.addWidget(case6)

        case7 = Key(" ")
        lh2.addWidget(case7)

        case8 = Key(" ")
        lh2.addWidget(case8)

#Ligne 3
        case9 = Key(" ")
        lh3.addWidget(case9)

        case10 = Key(" ")
        lh3.addWidget(case10)

        case11 = Key(" ")
        lh3.addWidget(case11)

        case12 = Key(" ")
        lh3.addWidget(case12)

#Ligne 4
        case13 = Key(" ")
        lh4.addWidget(case13)

        case14 = Key(" ")
        lh4.addWidget(case14)

        case15 = Key(" ")
        lh4.addWidget(case15)

        case16 = Key(" ")
        lh4.addWidget(case16)

# Grille
        lg.addLayout(lh1)
        lg.addLayout(lh2)
        lg.addLayout(lh3)
        lg.addLayout(lh4)

        self.setLayout(lg)