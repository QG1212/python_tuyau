from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout
from view.Tuyau_Nom import Nom

class Option(QWidget):
     def __init__(self):
         QWidget.__init__(self)
         layout = QVBoxLayout()
         self.setLayout(layout)


