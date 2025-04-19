from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QGridLayout
from tuyau_grille import Grille


class TuyauView(QWidget):
    def __init__(self):
        self.gridV = Grille()
        self.gridV.show()

# Affichage de la grille
    def print_board(self):
        self.gridV.show()

# Envoie des messages à l'utilisateur
    def message(self):
        pass

