from PySide6.QtWidgets import QPushButton

class key(QPushButton):
    def __init__(self, keys):
        super().__init__(keys)
        self.clicked.connect(self.buttonClicked)

    def buttonClicked(self):
        self.parent().parent().buttonClicked(self.text())


class Key:
    pass