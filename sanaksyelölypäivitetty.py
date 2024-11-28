import sys
import json
from Sanakysely import Sanakysely

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QFileDialog
import random


class Sanakysely_ikkuna(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,100,350,250)
        self.setStyleSheet("background-color: lightgrey;")
        self.kysely = Sanakysely()

        self.alusta_ikkuna() #tämä viimeisenä!!!
        

    def alusta_ikkuna(self):
        self.setWindowTitle(f'Sanakysely: {self.kysely.avain}')
        


        self.arvattava_sana = QLineEdit(self.kysely.seuraavaSana(), self)
        self.arvattava_sana.setGeometry(20, 80, 120, 30)
        self.arvattava_sana.setEnabled(False)
        self.arvattava_sana.setStyleSheet("border: 1px solid black;")
        self.arvattava_sana.setStyleSheet("background-color: white") 

        self.vastaus = QLineEdit(self)
        self.vastaus.setGeometry(200, 80, 120, 30)
        self.vastaus.setPlaceholderText("Kirjoita sana")
        self.vastaus.returnPressed.connect(self.tarkista_sana)
        self.vastaus.setStyleSheet("border: 1px solid black;")
        self.vastaus.setStyleSheet("background-color: white") 

        self.vahvista = QPushButton("Aloita alusta", self)
        self.vahvista.clicked.connect(self.aloita_alusta)
        self.vahvista.setGeometry(70, 120, 200, 30)
        self.vahvista.setStyleSheet("border: 1px solid black;")
        self.vahvista.setStyleSheet("background-color: lightgreen") 

        self.oikeat = QLabel("Oikeat: 0", self)
        self.oikeat.setGeometry(60, 30, 80, 40)

        self.väärät = QLabel("Väärät: 0", self)
        self.väärät.setGeometry(140, 30, 80, 40)

        self.sana = QLabel("Sana: 1", self)
        self.sana.setGeometry(220, 30, 80, 40)

        menupalkki = self.menuBar()
        tiedostomenu = menupalkki.addMenu("&Tiedosto")
        avaa = tiedostomenu.addAction("&Avaa")
        avaa.triggered.connect(self.menu_avaa)

    def tarkista_sana(self):
        vastaus = self.vastaus.text()
        self.kysely.tarkista(vastaus)

        self.arvattava_sana.setText(self.kysely.seuraavaSana())
        self.vastaus.clear()
        self.päivitä_tiedot()

    def aloita_alusta(self):
        self.kysely.nollaa()
        self.arvattava_sana.setText(self.kysely.seuraavaSana())

        self.päivitä_tiedot()
        self.setWindowTitle(f"Sanakysely: {self.kysely.avain}")

    def päivitä_tiedot(self):
        self.oikeat.setText(f"Oikeat: {self.kysely.oikeat}")
        self.väärät.setText(f"Väärät: {self.kysely.vaarat}")
        self.sana.setText(f"Sana: {self.kysely.sananro}")

    def menu_avaa(self):
        tiedosto = QFileDialog.getOpenFileName(self, "Avaa sanasto")
        with open(tiedosto[0], "r") as t:
            tiedoston_sisältö = t.read()
            self.kysely.sanasto = json.loads(tiedoston_sisältö)
            self.aloita_alusta()

def main():
    sovellus = QApplication(sys.argv) # olio luokasta QApplication
    ikkuna = Sanakysely_ikkuna() # olio luokasta Hedelmäpeli, joka peri QMainWindow ominaisuudet
    ikkuna.show() # kutsutaan ikkuna oliolle metodia show()
    sys.exit(sovellus.exec()) # käynnistetään sovellus(sovellus.exec()). Kun loppuu, välitetään paluuarvo sys.exit() metodille

if __name__ == "__main__":
    main()

