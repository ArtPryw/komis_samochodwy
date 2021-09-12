from osobowe import *
from motocykle import *
from ciezarowe import *

class Komis:

    def __init__(self):
        self.budzet = 100000
        self.osobowe = []
        self.ciezarowe = []
        self.motocykle = []


    def kup(self,obj):
        if obj.typ == 'osobowy':
            self.osobowe.append(obj)
            self.budzet -= obj.cena

        elif obj.typ == 'ciezarowy':
            self.ciezarowe.append(obj)
            self.budzet -= obj.cena

        elif obj.typ == 'motocykl':
            self.motocykle.append(obj)
            self.budzet -= obj.cena

    def wyswiel_liste_samochodow(self, lista):
        if lista == 'osobowe':
            lista = self.osobowe
        elif lista == 'ciezarowe':
            lista = self.ciezarowe
        elif lista == 'motocykle':
            lista = self.motocykle
        else:
            print("Nie mamy takiego typu pozajdów. Dostępne są: osobowe, ciezarowe, motocykle")

        for i,j in enumerate(lista):
            print(f"{i+1}: {j.opis()}")

    def podsumowanie(self):

        print("--"*8)
        print("OSOBOWE:")
        self.wyswiel_liste_samochodow('osobowe')
        print("--" * 8)
        print("CIĘŻAROWE:")
        self.wyswiel_liste_samochodow('ciezarowe')
        print("--" * 8)
        print("MOTOCYKLE:")
        self.wyswiel_liste_samochodow('motocykle')
        print("--" * 8)
        print("==== AKTUALNY BUDŻET =====")
        print(self.budzet)

    def sprzedaj(self, index_obj):
        if index_obj.typ == 'osobowy':
            self.budzet += (index_obj.cena + (index_obj.cena /10))
            self.osobowe.pop(index_obj)
            return self.osobowe, self.budzet
        elif index_obj.typ == 'ciezarowy':
            self.budzet += (index_obj.cena + (index_obj.cena / 10))
            self.ciezarowe.pop(index_obj)
            return self.ciezarowe, self.budzet
        elif index_obj.typ == 'motocykl':
            self.budzet += (index_obj.cena + (index_obj.cena / 10))
            self.motocykle.pop(index_obj)
            return self.motocykle, self.budzet


'''NAPISAĆ FUNKCJE Która wyswietli w liscie, ponumerowanej opis
każdego auta w liscie. (lista podana jako parametr w funkcji)

NAPISAĆ FUNKCJE KTÓRA wyświetli podsumowanie tzn. Wszystkie samochody
z podziałem na typy i budzet komisu'''
komis1 = Komis()

print(komis1.osobowe)
bmw_x3 = Osobowy(25000, 80)
print(f"BMW {bmw_x3.typ}")
ford_transit = Ciezarowy(5000,90,1500)
fiat_ducato = Ciezarowy(15000,120,2000)
print(f"transit {ford_transit.typ}")
komis1.kup(bmw_x3)
komis1.kup(ford_transit)
komis1.kup(fiat_ducato)

komis1.wyswiel_liste_samochodow("ciezarowe")
komis1.podsumowanie()

