import random

class Sanakysely:
    def __init__(self):
        self.sanasto = {"ruotsi": {'apina': 'apa', 
           'banaani':'banan',
           'juusto' : 'ost',
           'kakku' : 'kaka',
           'kala' : 'fisk',
           'kirja' : 'bok',
           'lintu' : 'fågel',
           'porkkana' :'morot',
           'punajuuri' :'rödbeta',
           'riisi':'ris'
           }}

        sanastonsisältö = list(self.sanasto.items())
        self.avain = sanastonsisältö[0][0] #valitaan listasta 'ruotsi' tai 'englanti' joka menee avaimen paikalla

        self.avaimet = list(self.sanasto[self.avain].keys()) #haetaan sanastosta avaimella 'ruotsi' sen arvojen avaimet
        self.__oikeat = 0
        self.__vaarat = 0
        self.__sana_nro = 0

    @property
    def oikeat(self):
        return self.__oikeat
    
    @property
    def vaarat(self):
        return self.__vaarat
    
    @property
    def sananro(self):
        return self.__sana_nro

    def nollaa(self):
        sanastonsisältö = list(self.sanasto.items())
        self.avain = sanastonsisältö[0][0]
        self.__oikeat = 0
        self.__vaarat = 0
        self.__sana_nro = 0
        self.avaimet = list(self.sanasto[self.avain].keys())


    def seuraavaSana(self):
        self.kysyttava_sana = random.choice(self.avaimet)
        self.__sana_nro += 1
        return self.kysyttava_sana
    
    def tarkista(self, vastaus):
        if self.sanasto[self.avain][self.kysyttava_sana] == vastaus.lower():
            self.__oikeat += 1
            self.avaimet.remove(self.kysyttava_sana)
        else:
            self.__vaarat += 1