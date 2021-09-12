from pojazdy import *

class Motocykl(Pojazdy):

    def __init__(self, cena, silnik_typ, liczba_miejsc):
        self.cena = cena
        self.silnik_typ = silnik_typ
        self.liczba_miejsc = liczba_miejsc
        self.typ = "motocykl"

    def cena(self):
        return self.cena

    def opis(self):
        return f"Motocyk kosztuje {self.cena}zł i ma {self.liczba_miejsc} miejsca."

    def wlacz_silnik(self):
        pass

    def wylacz_silnik(self):
        pass
