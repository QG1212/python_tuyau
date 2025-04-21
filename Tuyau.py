from controlleur.TuyauControleur import TuyauControleur
from view.TuyauView import TuyauView
from PySide6.QtWidgets import QApplication



if __name__ == "__main__":
    vue = TuyauView()
    vue.print_board()

    game = TuyauControleur()
    game.start()

    app = QApplication([])
    app.exec_()

