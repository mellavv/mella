import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class Omaikkuna(QMainWindow):
    def __init__(self):
        super().__init__()
        #self.setGeometry(100,100,350,250)

def main():
    sovellus = QApplication(sys.argv) # olio luokasta QApplication
    ikkuna = Omaikkuna() # olio luokasta Omaikkuna, joka peri QMainWindow ominaisuudet
    ikkuna.show() # kutsutaan ikkuna oliolle metodia show()
    sys.exit(sovellus.exec()) # käynnistetään sovellus(sovellus.exec()). Kun loppuu, välitetään paluuarvo sys.exit() metodille

if __name__ == "__main__":
    main()