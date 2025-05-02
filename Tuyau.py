from controlleur.TuyauControleur import TuyauControleur
from view.TuyauView import TuyauView
from model.TuyauModel import TuyauModel
from PySide6.QtWidgets import QApplication

if __name__ == "__main__":
    # Fenêtre en attente de l'application
    app = QApplication([])

    # Instance de la vue et du conntroleur
    model = TuyauModel()
    vue = TuyauView()

    # Instance du controleur
    game = TuyauControleur(model, vue)
    game.start()

    app.exec_()

