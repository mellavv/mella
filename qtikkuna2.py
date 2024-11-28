#terminaaliin 'pip install PySide6' saa asennettua PySide6 kirjastot
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel

class Omaikkuna(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(500,100,500,400)
        self.setWindowTitle('Terve')
        self.alusta_uusi()
        self.painettu = False


    def alusta_uusi(self):
        self.painike = QPushButton("Paina tästä!😁", self)
        self.painike.setGeometry(100, 100, 120, 80)
        self.painike.clicked.connect(self.painike_painettu)

        self.etiketti = QLabel("Tervetuloa", self)
        self.etiketti.setGeometry(250, 50, 150, 80) # x, y, koot x ja y
        

    def painike_painettu(self):
        self.painettu = not self.painettu #muutetaan käänteiseksi arvoksi
        if self.painettu:
            self.etiketti.setText("Painoit nappia 😶‍🌫️")
        else:
            self.etiketti.setText("Paina uudelleen🤯")
    

def main():
    sovellus = QApplication(sys.argv) # olio luokasta QApplication
    ikkuna = Omaikkuna() # olio luokasta Omaikkuna, joka peri QMainWindow ominaisuudet
    ikkuna.show() # kutsutaan ikkuna oliolle metodia show()
    sys.exit(sovellus.exec()) # käynnistetään sovellus(sovellus.exec()). Kun loppuu, välitetään paluuarvo sys.exit() metodille

if __name__ == "__main__":
    main()