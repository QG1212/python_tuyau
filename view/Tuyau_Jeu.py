from PySide6.QtWidgets import QWidget, QHBoxLayout

from view.Tuyau_Option import Option
from view.tuyau_grille import Grille
from view.Tuyau_Nom import Nom

class Jeu(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QHBoxLayout()


        self.grille = Grille()
        self.option = Option()

        layout.addWidget(self.grille)
        layout.addWidget(self.grille)

        self.setLayout(layout)
