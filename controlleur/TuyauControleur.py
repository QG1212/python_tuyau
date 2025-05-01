from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton

from model.TuyauModel import TuyauModel
from view.TuyauView import TuyauView

#appel la vue/model avevc une instance
# constructeur
# demarrer l'appli qui est appeler dans  le main
# verifier si le programme est lancer avec un bool

class TuyauControleur():

    def __init__(self, model, view):
        # instance
        self.model = model
        self.vue = view
        # Ce connecte au signal de la grille
        self.vue.jeu.grille.signal.connect(self.get_update_click)
        # fait le lien entre le modele (image) et la grille qui créer l'ensemble des boutons
        self.vue.jeu.grille.display(self.model.images)
        #self.model.coutdown()


    def get_update_click(self, x, y):
        self.model.play(x, y)
        self.vue.jeu.grille.display(self.model.images)
        self.vue.jeu.option.increment_coups()
        print(x,y)
        print(self.model.winner())

    def start(self):
        #self.model.coutdown()
        self.vue.show()


