from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton

from model.TuyauModel import TuyauModel
from view.TuyauView import TuyauView

#appel la vue/model avevc une instance
# constructeur
# demarrer l'appli qui est appeler dans  le main
# verifier si le programme est lancer avec un bool

class TuyauControleur():

    def __init__(self):
        self.model = TuyauModel()
        self.vue = TuyauView()
        pass

    def start(self):
        # Lance la partie
        pass
