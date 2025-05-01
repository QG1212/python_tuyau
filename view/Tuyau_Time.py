import time

from PySide6.QtWidgets import QLabel


class Tuyau_Time(QLabel):
    def __init__(self):
        self.setFixedSize(100, 100)
        self.setStyleSheet("font-size: 20px; margin: 20px;")


    def coutdown(self):
        seconds = 5
        while seconds > 0:
            print(seconds)
            # arret du programme pendant 1 sec
            time.sleep(1)
            seconds = seconds - 1
        print("finish")




