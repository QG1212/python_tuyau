from controlleur.TuyauControleur import TuyauControleur
from view.TuyauView import TuyauView
from model.TuyauModel import TuyauModel


from PySide6.QtWidgets import QApplication


if __name__ == "__main__":
    app = QApplication([])

    vue = TuyauView()
    model = TuyauModel()

    game = TuyauControleur(model, vue)
    game.start()


    app.exec_()

