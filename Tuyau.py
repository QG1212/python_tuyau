from controlleur.TuyauControleur import TuyauControleur

from PySide6.QtWidgets import QApplication



if __name__ == "__main__":
    app = QApplication([])
    game = TuyauControleur()
    game.show()
    app.exec_()