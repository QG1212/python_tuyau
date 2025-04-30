from PySide6.QtGui import QIcon, QTransform, QPixmap
from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import QSize


class Key(QPushButton):
    def __init__(self, image_path, angle, options):
        super().__init__()

        self.setFixedSize(100, 100)
        self.setIconSize(self.size())

        self.options = options
        self.angle = angle
        self.image_path = image_path
        self.update_icon()

        # prevenir le controlleur de l'action + coor
        self.clicked.connect(self.buttonClicked)

# model

# a comprendre !!!!!!!!!!!!!!!!!!!!!!

    def update_icon(self):
        # Appliquer la rotation en fonction de l'angle
        transform = QTransform()
        transform.rotate(self.angle)

        # Créer un QPixmap de l'image et appliquer la transformation
        image_path = QPixmap(self.image_path).transformed(transform)

        # Définir le QPixmap comme icône du bouton
        self.setIcon(QIcon(image_path))
        self.setIconSize(self.size())

    def buttonClicked(self, angle):

        self.angle = (angle) % 360

        # Mettre à jour l'icône après rotation
        self.update_icon()
        self.options.increment_coups()
