from PySide6.QtWidgets import QWidget
from view.tuyau_grille import Grille


class TuyauView(QWidget):
    def __init__(self):
        super(TuyauView, self).__init__()
        self.gridV = Grille()
        self.gridV.show()

# Affichage de la grille
    def print_board(self):

        self.gridV.show()

# Envoie des messages à l'utilisateur
    def message(self):
        pass

