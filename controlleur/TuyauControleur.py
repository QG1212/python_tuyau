class TuyauControleur():

    def __init__(self, model, view):
        # instance
        self.model = model
        self.vue = view
        # Ce connecte au signal de la grille
        self.vue.jeu.grille.signal.connect(self.get_update_click)
        # fait le lien entre le modele (image) et la grille qui créer l'ensemble des boutons
        self.vue.jeu.grille.display(self.model.images)


    # Modification à chaque click
    # récupère les différentes methodes
    def get_update_click(self, x, y):
        # Coordonné
        self.model.play(x, y)
        self.model.increment_coups()
        self.vue.jeu.grille.display(self.model.images)
        self.vue.jeu.option.set_coups(self.model.nb_coups)
        self.vue.jeu.option.temps.setText("Temps : " + str(self.model.coutdown().seconds))

        print(x,y)
        print(self.model.winner())
        if self.model.winner():
            print("Vous avez fini le jeu en "+ str(self.model.coutdown().seconds) + " secondes avec " + str(self.model.nb_coups) + " coups.")

    def start(self):
        # La fenêtre principal
        self.vue.show()


