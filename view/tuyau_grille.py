from PySide6.QtWidgets import QWidget, QGridLayout, QHBoxLayout, QVBoxLayout
from view.tuyau_key import Key
import os
import random


class Grille(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        lv = QVBoxLayout()
        lh = QHBoxLayout()
        lg = QGridLayout()

        self.setWindowTitle("Jeu du tuyau")
        self.setMinimumSize(600, 600)

# a comprendre !!!!!!!!!!!!!!!!!!!

        # Layouts horizontaux pour chaque ligne
        lh1 = QHBoxLayout()
        lh2 = QHBoxLayout()
        lh3 = QHBoxLayout()
        lh4 = QHBoxLayout()

        image_folder = "images"
        images = [
            "tuyau_coude.png", "tuyau_droit.png", "tuyau_droit.png", "tuyau_coude.png",
            "tuyau_droit.png", "tuyau_coude.png", "tuyau_coude.png", "tuyau_droit.png",
            "tuyau_droit.png", "tuyau_droit.png", "tuyau_droit.png", "tuyau_droit.png",
            "tuyau_coude.png", "tuyau_coude.png", "tuyau_coude.png", "tuyau_coude.png"
        ]

<<<<<<< HEAD
        # Créer la grille avec des images aléatoires
        for i in range(16):  # 4 cases par ligne
            # Choisir une image aléatoire parmi celles définies dans images
            image_path = os.path.join(image_folder, images[i])
=======
        # Layouts horizontaux pour chaque ligne
        lh1 = QHBoxLayout()
        lh2 = QHBoxLayout()
        lh3 = QHBoxLayout()
        lh4 = QHBoxLayout()

>>>>>>> b30c24cfbe46291d39e09ee761570cac8f654227

        for i in range(16):
            image_path = os.path.join(image_folder, images[i])
            case = Key(image_path)
            if i < 4:
                lh1.addWidget(case)
            elif i < 8:
                lh2.addWidget(case)
            elif i < 12:
                lh3.addWidget(case)
            else:
                lh4.addWidget(case)

# Grille
        lg.addLayout(lh1, 0, 0)
        lg.addLayout(lh2, 1, 0)
        lg.addLayout(lh3, 2, 0)
        lg.addLayout(lh4, 3, 0)

        self.setLayout(lg)