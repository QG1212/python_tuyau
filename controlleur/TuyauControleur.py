from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton
from view.tuyau_grille import Grille


class TuyauControleur():
    def __init__(self):
        self.gridV = Grille()
        self.gridV.show()

    def show(self):
        self.gridV.show()

# Lance la partie
    def start(self):
        pass
# récupère l'action d'un joueur
    def getAction(self):
        pass
