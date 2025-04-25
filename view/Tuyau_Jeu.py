from PySide6.QtWidgets import QWidget, QHBoxLayout
from view.tuyau_grille import Grille
from view.Tuyau_Nom import Nom

class Jeu(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QHBoxLayout()
        layout_horizontale = QHBoxLayout()

        self.setMinimumSize(400, 600)

        self.grille = Grille()
        self.nom = Nom()
        layout.addWidget(self.grille)
        layout.addWidget(self.nom)

        self.setLayout(layout_horizontale)
