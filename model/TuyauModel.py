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

# Permet au jouer de tourner une tuile
    def play(self):
        Key.buttonClicked()
        Key.update_icon()
        pass

    # def niveau(self):
    #     image_folder = "images"
    #     images = [
    #         "tuyau_coude.png", "tuyau_droit.png", "tuyau_droit.png", "tuyau_coude.png",
    #         "tuyau_droit.png", "tuyau_coude.png", "tuyau_coude.png", "tuyau_droit.png",
    #         "tuyau_droit.png", "tuyau_droit.png", "tuyau_droit.png", "tuyau_droit.png",
    #         "tuyau_coude.png", "tuyau_coude.png", "tuyau_coude.png", "tuyau_coude.png"
    #     ]
    #     # Créer la grille avec des images aléatoires
    #     for i in range(16):  # 4 cases par ligne
    #         # Choisir une image aléatoire parmi celles définies dans images
    #         image_path = os.path.join(image_folder, images[i])
    #
    #         case = Key(image_path)
    #         if i < 4:
    #             lh1.addWidget(case)
    #         elif i < 8:
    #             lh2.addWidget(case)
    #         elif i < 12:
    #             lh3.addWidget(case)
    #         else:
    #             lh4.addWidget(case)
    #     pass

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