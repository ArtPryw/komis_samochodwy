from pojazdy import *

class Osobowy(Pojazdy):

    def __init__(self, cena, max_paliwo, typ="osobowy"):
        self.cena = cena
        self.max_paliwo = max_paliwo
        self.czy_sie_rusza = False
        self.typ = typ

    def jedz(self):
        if self.czy_sie_rusza == True:
            print("Samochód jest już w ruchu")
        else:
            if self.silnik_status == 1:
                print("Ruszam..")
                self.czy_sie_rusza = True
            else:
                print("Włącz silnik aby ruszyć.")

    def zatrzymaj_sie(self):
        if self.czy_sie_rusza == False:
            print("Samochód już stoi...")
        else:
            self.czy_sie_rusza = False
            print("Zatrzymuje się...")

    #TODO: obsluzyć typ danych i to by nie dało się przelać pełnego baku
    def tankuj(self, litry):
        self.max_paliwo += litry

    def wlacz_silnik(self):
        self.silnik_status = 1
        return "Silnik włączony"

    def wylacz_silnik(self):
        self.silnik_status = 0

    def opis(self):
        return f"Samochód {self.typ}, cena: {self.cena}, pojemnośc baku = {self.max_paliwo} "

    def cena(self):
        return self.cena

