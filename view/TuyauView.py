from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QGridLayout


class TuyauView(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        lv = QVBoxLayout()
        lh = QHBoxLayout()
        lg = QGridLayout()

        self.setWindowTitle("Jeu du tuyau")
        self.setMinimumSize(600, 600)

        lh1 = QHBoxLayout()
        lh2 = QHBoxLayout()
        lh3 = QHBoxLayout()
        lh4 = QHBoxLayout()

        pass

# Affichage de la grille
    def print_board(self):
        case1 = Key(" ")
        pass

# Envoie des messages à l'utilisateur
    def message(self):
        pass
# Affiche les tuyau dans la grille
    def print_tuyau(self):
        pass
