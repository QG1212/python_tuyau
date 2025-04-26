from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from view.Tuyau_Nom import Nom

class Option(QWidget):
     def __init__(self):
         QWidget.__init__(self)
         layout = QVBoxLayout()
         self.nom = QLabel("Nom: Joueur")
         self.coups = QLabel("Coups: 0")
         self.temps = QLabel("Temps: 0")

         for label in (self.nom, self.coups, self.temps):
             label.setStyleSheet("font-size: 20px; margin: 20px;")

         layout.addWidget(self.nom)
         layout.addWidget(self.coups)
         layout.addWidget(self.temps)

         layout.addStretch()  # Ajoute de l'espace en bas pour l'esthétique

         self.setLayout(layout)

         self.setStyleSheet("""
                     QWidget {
                         border: 2px solid black;
                         border-radius: 10px;
                         background-color: #f0f0f0;
                         padding: 15px;
                     }
                 """)


