from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QFont

class Nom(QLabel):
    def __init__(self):
        super().__init__("nom du joueur")

        self.setStyleSheet("border: 1px solid black;")
        self.setFont(QFont("Arial", 30))
        self.setMaximumHeight(50)