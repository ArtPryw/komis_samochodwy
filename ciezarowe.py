from osobowe import *

class Ciezarowy(Osobowy):

    def __init__(self,cena, max_paliwo, ladownosc, typ="ciezarowy"):
        self.ladownosc = ladownosc
        self.zaladowane = 0
        super().__init__(cena, max_paliwo, typ)

    def wlacz_silnik(self):
        print("Uruchamiam samochód ciężarowy")
        super().wlacz_silnik()
    def wylacz_silnik(self):
        print("Wyłączam samochód ciężarowy")
        super().wylacz_silnik()
    def tankuj(self, litry):
        print("Tankuję, samochód ciężrowy")
        super().tankuj(litry)

    def laduj(self, ladunek):
        if ladunek < (self.ladownosc - self.zaladowane):
            print(f"Ładuje ładunek o masie {ladunek}")
            self.zaladowane = ladunek
        else:
            print("nie zmieścimy już tego ładunku.")
    #TODO: obsłużyć wyładowanie poniżej 0.

    def rozladuj(self, ladunek):
        print(f"Rozładowuje ładunek o masie {ladunek}")
        self.zaladowane -= ladunek

    def pokaz_stan_naladowania(self):
        print(f"Aktualnie załadowane {self.zaladowane} kg.")

