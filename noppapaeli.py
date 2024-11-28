#terminaaliin 'pip install PySide6' saa asennettua PySide6 kirjastot
import sys
import random
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PySide6.QtGui import QPixmap

class Noppa(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(500,100,500,400)
        self.setWindowTitle('Noppapeli')
        self.alusta_uusi()


    def alusta_uusi(self):
        self.painike = QPushButton("Heitä noppaa", self)
        self.painike.setGeometry(100, 150, 120, 80)
        self.painike.clicked.connect(self.painike_painettu)

        self.etiketti = QLabel("Tulos:", self)
        self.etiketti.setGeometry(100, 50, 150, 80) # x, y, koot x ja y

        kuva = QPixmap("noppa.png")
        self.etiketti2 = QLabel(self)
        self.etiketti2.setGeometry(220, 140, 100, 100)
        self.etiketti2.setPixmap(kuva)
        

    def painike_painettu(self):
        arvottu_luku = random.randint(1, 99)
        self.etiketti.setText(f"Tulos: {arvottu_luku}")
    

def main():
    sovellus = QApplication(sys.argv) # olio luokasta QApplication
    ikkuna = Noppa() # olio luokasta Noppa, joka peri QMainWindow ominaisuudet
    ikkuna.show() # kutsutaan ikkuna oliolle metodia show()
    sys.exit(sovellus.exec()) # käynnistetään sovellus(sovellus.exec()). Kun loppuu, välitetään paluuarvo sys.exit() metodille

if __name__ == "__main__":
    main()