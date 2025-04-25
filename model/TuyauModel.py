from view.tuyau_key import Key

class TuyauModel:
    def __init__(self):
        self.image_folder = "images"
        self.images = [
            [("tuyau_coude.png",0), ("tuyau_droit.png",0), ("tuyau_droit.png",0), ("tuyau_coude.png",0)],
            [("tuyau_droit.png",0), ("tuyau_coude.png",0), ("tuyau_coude.png",0), ("tuyau_droit.png",0)],
            [("tuyau_droit.png",0), ("tuyau_droit.png",0), ("tuyau_droit.png",0), ("tuyau_droit.png",0)],
            [("tuyau_coude.png",0), ("tuyau_coude.png",0), ("tuyau_coude.png",0), ("tuyau_coude.png",0)]
        ]

#Permet au jouer de tourner une tuile
    def play(self, x, y):
        pass


    def name_player(self):
        # ajouter un layout
        #mettre un nom
        pass

    def time(self):
        #chrono
        pass

    def coup(self):
        #coup stocker dans un tableau
        #compter le tableau
        #afficher
        #clear a la fin
        pass



# Mélanger
    def shuffleBoard(self):
        #Melange la grille quand cliquer
        #faire un layout bourton
        #l'associer au melange
        #l'associer a la fonction qui affiche le model
        pass

    # Verifie si la grille est valider
    def winner(self):
        # quentino
        pass