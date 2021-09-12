from abc import ABC, abstractmethod

class Pojazdy(ABC):

    @abstractmethod
    def cena(self):
        pass

    @abstractmethod
    def opis(self):
        pass

    @abstractmethod
    def wlacz_silnik(self):
        pass

    @abstractmethod
    def wylacz_silnik(self):
        pass