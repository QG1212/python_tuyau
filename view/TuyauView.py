from PySide6.QtWidgets import QMainWindow, QVBoxLayout
from view.Tuyau_Jeu import Jeu

# la vue hérite de la fenêtre
class TuyauView(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        # super(QMainWindow, self).__init__()
        self.setWindowTitle("Jeu de tuyau")
        self.setFixedSize(800, 600)

        # Widget principal de la fenêtre
        layout = QVBoxLayout()
        self.jeu = Jeu()
        self.setCentralWidget(self.jeu)

        self.setLayout(layout)

