import random

class Rekisteri_:
    def __init__(self):
        self.autot = {'abc-454': ['volvo', '2005'],
            'hjs-852': ['toyota', '2015'],
            'mms-115': ['audi', '1998'],
            'joi-962': ['mercedes-benz', '2020'] 
            }

        self.avaimet = list(self.autot.keys())
        self.__rek = " "
        self.__merkki = " "
        self.__vuosi = " "

    @property
    def rek(self):
        return self.__rek
    
    @property
    def merkki(self):
        return self.__merkki
    
    @property
    def vuosi(self):
        return self.__vuosi

    def nollaa(self):
        self.__rek = " "
        self.__merkki = " "
        self.__vuosi = " "

   
    
    def etsi(self, rekisterinumero):
        print(f"Searching for {rekisterinumero}...")
        if rekisterinumero in self.autot:
            self.__merkki, self.__vuosi = self.autot[rekisterinumero]
            print(f"Found: {self.__merkki}, {self.__vuosi}")
            return True
        else:
            print("Not found.")
            return False
        

