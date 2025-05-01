from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from model.TuyauModel import TuyauModel


# from view.Tuyau_Time import Tuyau_Time

class Option(QWidget):
     def __init__(self):
         QWidget.__init__(self)
         self.layout = QVBoxLayout()
         self.setLayout(self.layout)

         self.nb_coups = 0
         # model = TuyauModel()
         # model.coutdown()
         self.coups = QLabel(f"Coups : {self.nb_coups}")
         self.temps = QLabel("Temps : ")


         for label in (self.temps, self.coups) :
             label.setStyleSheet("font-size: 20px; margin: 20px;border: 2px solid black; border-radius: 10px; background-color: #f0f0f0; padding: 15px;")

         self.layout.addWidget(self.temps)
         self.layout.addWidget(self.coups)


         self.layout.addStretch()  # Ajoute de l'espace en bas pour l'esthétique

         self.setLayout(self.layout)

     def set_coups(self, value):
         self.coups.setText(f"Coups : {value}")



