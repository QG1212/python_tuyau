from PySide6.QtWidgets import QWidget, QHBoxLayout

from view.Tuyau_Option import Option
from view.tuyau_grille import Grille

class Jeu(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        layout = QHBoxLayout()

        self.grille = Grille()
        self.option = Option()

        layout.addWidget(self.grille)
        layout.addWidget(self.option)

        self.setLayout(layout)
