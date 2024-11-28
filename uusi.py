class Tuote:
    tuote_id = 1000
    def __init__(self, tuote_nimi: str, hinta: float):
        self.__nimi = tuote_nimi
        self.__hinta = hinta
        self.__tuote_id = Tuote.tuote_id
        Tuote.tuote_id += 1

    def lue_hinta(self):
        print(self)
        return self.__hinta

    def asetus(self, uusihinta:float):
        if uusihinta >= 0.1 and uusihinta >= 0.9*self.hinta:
            self.__hinta = uusihinta
        else:
            print("Ei tommosia hintoja..")
    
    def __str__(self):
        return f"Tuote ID: {self.__tuote_id}\nNimi: {self.__nimi}\nHinta: {self.__hinta}"

t1 = Tuote("banaani", 0.8)
t2 = Tuote("kakku", 6.5)
t3 = Tuote("hattu", 12.65)

tuotteet = []

tuotteet.append(t1)
tuotteet.append(t2)
tuotteet.append(t3)

def uusi_tuote():
    tuotenimi = input("Nimi: ")
    hinta = float(input("Hinta: "))
    uusituote = Tuote(tuotenimi, hinta)
    tuotteet.append(uusituote)


print(vars(t1)) #palauttaa olion tiedot dictionarynä
print(t3)