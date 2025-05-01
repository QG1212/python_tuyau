from view.tuyau_key import Key
from PySide6.QtWidgets import QWidget
import time

class TuyauModel(QWidget):
    def __init__(self):
        self.image_folder = "images"
        self.images = [
            [("tuyau_coude.png",0), ("tuyau_droit.png",0), ("tuyau_droit.png",0), ("tuyau_coude.png",0)],
            [("tuyau_droit.png",0), ("tuyau_coude.png",0), ("tuyau_coude.png",0), ("tuyau_droit.png",0)],
            [("tuyau_droit.png",0), ("tuyau_droit.png",0), ("tuyau_droit.png",0), ("tuyau_droit.png",0)],
            [("tuyau_coude.png",0), ("tuyau_coude.png",0), ("tuyau_coude.png",0), ("tuyau_coude.png",0)]
        ]

        self.Rectangle = {
            0:[(-1,0), (1,0)],
            90:[(0, -1), (0, 1)],
            180:[(-1,0), (1,0)],
            270:[(0, -1), (0, 1)],
        }

        self.Coude = {
            0:[(0,1), (-1,0)],
            90:[(-1,0), (0,-1)],
            180:[(0,-1), (1,0)],
            270:[(1,0), (0,1)],
        }

# Gere la rotation des tuiles
    def play(self, x, y):
        #recupere d'abord en y (quel tableau), puis en x (contenu du tableau)
        path, angle = self.images[y][x]
        angle = (angle + 90) % 360
        self.images[y][x] = (path, angle)

    def coutdown(self):
        seconds = 0
        while seconds >= 0:
            print(seconds)
            # arret du programme pendant 1 sec
            time.sleep(1)
            seconds = seconds + 1
        print(seconds)

# Mélanger
    def shuffleBoard(self):
        #Melange la grille quand cliquer
        #faire un layout bourton
        #l'associer au melange
        #l'associer a la fonction qui affiche le model
        pass

    # Verifie si la grille est valider
    def winner(self):
        for i in range(4):
            for j in range(4):
                nom, angle = self.images[i][j]
                if nom == "tuyau_droit.png":
                    # tuyau contient un tableau du dico, qui correspond aux voisins
                    tuyau = self.Rectangle[angle]
                elif nom == "tuyau_coude.png":
                    tuyau = self.Coude[angle]

                for voisin in tuyau:
                    #j2 = x / i2 = y
                    j2,i2 = voisin
                    xVoisin = j2 + j
                    yVoisin = i2 + i

                    if 0<=xVoisin<=3 and 0<=yVoisin<=3:
                        nom_voisin, angle_voisin = self.images[yVoisin][xVoisin]
                        if nom_voisin == "tuyau_droit.png":
                            # tuyau contient un tableau du dico, qui correspond aux voisins
                            tuyau_voisin = self.Rectangle[angle_voisin]
                        else:
                            tuyau_voisin = self.Coude[angle_voisin]

                        new_voisin = []
                        for next_voisin in tuyau_voisin:
                            # j2 = x / i2 = y
                            j2, i2 = next_voisin
                            xNextV = j2 + xVoisin
                            yNextV = i2 + yVoisin
                            # coordonné précise de voisin
                            new_voisin.append((xNextV, yNextV))

                        print((j,i), new_voisin)
                        if (j,i) not in new_voisin:
                            return False

        return True





    pass