from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from model.TuyauModel import TuyauModel


# from view.Tuyau_Time import Tuyau_Time

class Option(QWidget):
     def __init__(self):
         QWidget.__init__(self)
         self.layout = QVBoxLayout()
         self.setLayout(self.layout)


         self.coups = QLabel(f"Coups : 0")
         self.temps = QLabel("Temps : ")

        # applique le style a chaque label
         for label in (self.temps, self.coups) :
             label.setStyleSheet("font-size: 20px; margin: 20px;border: 2px solid black; border-radius: 10px; background-color: #f0f0f0; padding: 15px;")

         # Ajout des widget
         self.layout.addWidget(self.temps)
         self.layout.addWidget(self.coups)

         # Ajoute de l'espace en bas pour l'esthétique
         self.layout.addStretch()

         self.setLayout(self.layout)

     # Mets à jour l'affichage
     def set_coups(self, nb_coups):
         self.coups.setText(f"Coups : {nb_coups}")



