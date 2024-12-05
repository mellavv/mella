# pip install PySide6
#Tee oheisen kuvan mukainen ikkuna, josta voidaan syöttää 
# auton tietoja rekisteriin. 
#Lisää-painiketta painettaessa tiedot luetaan 
# tekstikentistä ja lisätään tietorakenteeseen. 
#Kun syötetään pelkkä rekisteritunnus ja painetaan 
# Hae-painiketta, haetaan merkki ja vuosi tekstikenttiin 
# rekisteritunnusta vastaavat tiedot tietorakenteesta.
#Tietorakenteena kannattaa käyttää sitä tietorakennetta, 
# joka sisältää hakutoiminnon.


import sys
import random
from rekisteris import Rekisteri_
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit

class Rekisteri(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rekisteri")
        self.setGeometry(200,200,250,250)
        self.rekisteri = Rekisteri_()
        
        self.alustaIkkuna()
    
    def alustaIkkuna(self):
        self.rek = QLabel("Rek.nro", self)
        self.rek.setGeometry(15,10,60,30)

        self.merkki = QLabel("Merkki", self)
        self.merkki.setGeometry(15,50,60,30)

        self.vuosi = QLabel("Vuosi", self)
        self.vuosi.setGeometry(15,90,60,30)

        self.rek2 = QLineEdit(self)
        self.rek2.setGeometry(70,10,110,30)
        self.rek2.returnPressed.connect(self.hae_tiedot)

        self.merkki2 = QLineEdit(self)
        self.merkki2.setGeometry(70,50,110,30)

        self.vuosi2 = QLineEdit(self)
        self.vuosi2.setGeometry(70,90,110,30)

        self.lisää = QPushButton("Lisää", self)
        self.lisää.setGeometry(15,140,150,30)
        self.lisää.clicked.connect(self.lisää_tiedot)

        self.hae = QPushButton("Hae", self)
        self.hae.setGeometry(15,180,150,30)
        self.hae.clicked.connect(self.hae_tiedot)

        self.nollaus = QPushButton("Tyhjennä", self)
        self.nollaus.setGeometry(15,210,90,25)
        self.nollaus.clicked.connect(self.nollaa)

        
    def lisää_tiedot(self):
        rekisterinumero = self.rek2.text()
        merkki = self.merkki2.text()
        vuosi = self.vuosi2.text()
    
        if rekisterinumero and merkki and vuosi:
            self.rekisteri.autot[rekisterinumero] = [merkki, vuosi]
            self.rekisteri.avaimet.append(rekisterinumero)
            self.nollaa()
        else:
            pass

    def hae_tiedot(self):
        rekisterinumero = self.rek2.text()
        if self.rekisteri.etsi(rekisterinumero):
            self.päivitä_tiedot()
        else:
            self.merkki2.setText("Not found")
            self.vuosi2.setText("Not found")
        

    def päivitä_tiedot(self):
        self.merkki2.setText(self.rekisteri.merkki)
        self.vuosi2.setText(self.rekisteri.vuosi)
        
    def nollaa(self):
        self.rek2.clear()
        self.merkki2.clear()
        self.vuosi2.clear()     


def main():
    sovellus = QApplication(sys.argv) # olio luokasta QApplication
    ikkuna = Rekisteri() # olio luokasta Arvaaluku, joka peri QMainWindow ominaisuudet
    ikkuna.show() # kutsutaan ikkuna oliolle metodia show()
    sys.exit(sovellus.exec()) # käynnistetään sovellus(sovellus.exec()). Kun loppuu, välitetään paluuarvo sys.exit() metodille

if __name__ == "__main__":
    main()