from PySide6.QtWidgets import QMainWindow, QVBoxLayout
from view.Tuyau_Jeu import  Grille
from view.Tuyau_Jeu import Jeu

# la vue hérite de la fenêtre
#pas la fenêtre de ma chambre
class TuyauView(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        # super(QMainWindow, self).__init__()
        self.setWindowTitle("Jeu de tuyau")
        self.setMinimumSize(800, 600)

        # Widget principal de la fenêtre
        layout = QVBoxLayout()
        self.jeu = Jeu()
        self.setCentralWidget(self.jeu)

        self.setLayout(layout)


        #self.gridV = Grille()
        #self.gridV.show()


# Affichage de la grille
    def print_board(self):
        pass

