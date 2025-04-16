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