from pojazdy import *

class Osobowy(Pojazdy):

    def __init__(self, cena, max_paliwo):
        self.silnik_status = 0
        self.cena = cena
        self.max_paliwo = max_paliwo
        self.czy_sie_rusza = False

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
        return "Some desc."

    def cena(self):
        return self.cena


a = Osobowy(5000,50)
print(a.silnik_status)
a.wlacz_silnik()
print(a.silnik_status)
a.tankuj(50)
print(a.max_paliwo)
a.wylacz_silnik()
a.jedz()
a.wlacz_silnik()
a.jedz()