from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import QSize

class Key(QPushButton):
    def __init__(self, image_path):
        super().__init__()

        self.setFixedSize(100, 100)
        self.setIcon(QIcon(image_path))
        self.setIconSize(QSize(100, 100))
        self.clicked.connect(self.buttonClicked)

    def buttonClicked(self):
        print("Bouton cliqué :", self)
        self.parent().parent().buttonClicked(self.text())
