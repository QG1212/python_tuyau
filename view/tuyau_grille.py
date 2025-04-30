from PySide6.QtWidgets import QWidget, QGridLayout
from PySide6.QtCore import Signal
from view.tuyau_key import Key



class Grille(QWidget):
    signal = Signal(int, int)

    def __init__(self, options):
        QWidget.__init__(self)
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.options = options

    def display(self, images):
        # Vérifie si le layout est vide
        # Prend le premier widget, s'il est pas vide -> supprime
        # layout -> un tableau de widget, on prend le 1er puis on le supprime
        while self.layout.count():
            item = self.layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        for i in range(4):
            for j in range(4):
                print(images[i][j])
                # Dissocie le tuple
                path,angle = images[i][j]
                # path -> image
                bouton = Key("images/"+path, angle)
                self.layout.addWidget(bouton, i, j)
                # Permet de mettre des parmètres à une fonction en parmètres
                bouton.clicked.connect(lambda checked, y=i, x=j: self.signal.emit(x, y))