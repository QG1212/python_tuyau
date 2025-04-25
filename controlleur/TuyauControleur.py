from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton

from model.TuyauModel import TuyauModel
from view.TuyauView import TuyauView

#appel la vue/model avevc une instance
# constructeur
# demarrer l'appli qui est appeler dans  le main
# verifier si le programme est lancer avec un bool

class TuyauControleur():

    def __init__(self, model, view):
        self._model = model
        self.vue = view
        #self.vue.grille.signal.connect(self.get_update_click)

    def get_update_click(self, x, y):
        print(x,y)




    def start(self):
        self.vue.show()


