from view.tuyau_key import Key
from PySide6.QtWidgets import QWidget
import datetime


class TuyauModel(QWidget):
    def __init__(self):
        self.nb_coups = 0
        self.image_folder = "images"
        self.images = [
            [("tuyau_coude.png",0), ("tuyau_droit.png",0), ("tuyau_droit.png",0), ("tuyau_coude.png",0)],
            [("tuyau_droit.png",0), ("tuyau_coude.png",0), ("tuyau_coude.png",0), ("tuyau_droit.png",0)],
            [("tuyau_droit.png",0), ("tuyau_droit.png",0), ("tuyau_droit.png",0), ("tuyau_droit.png",0)],
            [("tuyau_coude.png",0), ("tuyau_coude.png",0), ("tuyau_coude.png",0), ("tuyau_coude.png",0)]
        ]

        # Dicto de tableau contenant des sorties/entrées pour chaque rotation pour un tuyau rectangle
        self.Rectangle = {
            0:[(-1,0), (1,0)],
            90:[(0, -1), (0, 1)],
            180:[(-1,0), (1,0)],
            270:[(0, -1), (0, 1)],
        }

        # Dicto de tableau contenant des sorties/entrées pour chaque rotation pour un tuyau coude
        self.Coude = {
            0:[(0,1), (-1,0)],
            90:[(-1,0), (0,-1)],
            180:[(0,-1), (1,0)],
            270:[(1,0), (0,1)],
        }

        # la date quand le jeu est lancé
        self.startChrono = datetime.datetime.now()

# Gere la rotation des tuiles
    def play(self, x, y):
        #recupere d'abord en y (quel tableau), puis en x (contenu du tableau)
        path, angle = self.images[y][x]
        angle = (angle + 90) % 360
        self.images[y][x] = (path, angle)

# Chrono
    def coutdown(self):
        # date du jour - date du lancement
        timer = datetime.datetime.now() - self.startChrono
        return timer

# Ajoute des coups à l'attribut
    def increment_coups(self):
        self.nb_coups += 1

# Vérifie si la grille est valider
    def winner(self):
        # Parcours de la grille
        for i in range(4):
            for j in range(4):
                # Tuples de l'image
                nom, angle = self.images[i][j]
                # Vérifie quelle images est sur la bouton
                if nom == "tuyau_droit.png":
                    # tuyau contient un tableau du dico, qui correspond aux voisins
                    tuyau = self.Rectangle[angle]
                elif nom == "tuyau_coude.png":
                    tuyau = self.Coude[angle]

                for voisin in tuyau:
                    #j2 = x / i2 = y
                    #Pour aller au voisin
                    j2,i2 = voisin
                    #Le voisin
                    xVoisin = j2 + j
                    yVoisin = i2 + i

                    # Vérifie si nous sommes bien dans le tableau
                    if 0<=xVoisin<=3 and 0<=yVoisin<=3:
                        # Tuple du voisin
                        nom_voisin, angle_voisin = self.images[yVoisin][xVoisin]
                        if nom_voisin == "tuyau_droit.png":
                            # tuyau contient un tableau du dico, qui correspond aux voisins
                            tuyau_voisin = self.Rectangle[angle_voisin]
                        else:
                            tuyau_voisin = self.Coude[angle_voisin]

                        # Coordonnées des voisins de B
                        new_voisin = []
                        for next_voisin in tuyau_voisin:
                            # j2 = x / i2 = y
                            j2, i2 = next_voisin
                            xNextV = j2 + xVoisin
                            yNextV = i2 + yVoisin
                            # coordonné précise du voisin
                            new_voisin.append((xNextV, yNextV))

                        # vérifie que les coordonnées de A sois dans les voisins de B
                        if (j,i) not in new_voisin:
                            return False

        return True





    pass