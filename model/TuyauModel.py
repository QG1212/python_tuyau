from view.tuyau_key import Key

class TuyauModel:
    def __init__(self):
        #constructeur ?
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

    def level1(self):
        image_folder = "images"
        images = [
            "tuyau_coude.png", "tuyau_droit.png", "tuyau_droit.png", "tuyau_coude.png",
            "tuyau_droit.png", "tuyau_coude.png", "tuyau_coude.png", "tuyau_droit.png",
            "tuyau_droit.png", "tuyau_droit.png", "tuyau_droit.png", "tuyau_droit.png",
            "tuyau_coude.png", "tuyau_coude.png", "tuyau_coude.png", "tuyau_coude.png"
        ]
        pass

# Permet au jouer de tourner une tuile
    def play(self):
        keys = Key(self.level1())
        keys.buttonClicked()
        keys.update_icon()
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