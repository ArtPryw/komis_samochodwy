class Komis:

    def __init__(self):
        self.budzet = 100000
        self.osobowe = []
        self.ciezarowe = []
        self.motocykle = []


    def kup(self, typ, obj):
        if typ == 'osobowe':
            self.osobowe.append(obj)
            self.budzet -= obj.cena
            return self.osobowe, self.budzet
        elif typ == 'ciezarowe':
            self.ciezarowe.append(obj)
            self.budzet -= obj.cena
            return self.ciezarowe, self.budzet
        elif typ == 'motocykl':
            self.motocykle.append(obj)
            self.budzet -= obj.cena
            return self.motocykle, self.budzet


    def sprzedaj(self, typ, index_obj):
        if typ == 'osobowe':
            self.budzet += (index_obj.cena + (index_obj.cena /10))
            self.osobowe.pop(index_obj)
            return self.osobowe, self.budzet
        elif typ == 'ciezarowe':
            self.budzet += (index_obj.cena + (index_obj.cena / 10))
            self.ciezarowe.pop(index_obj)
            return self.ciezarowe, self.budzet
        elif typ == 'motocykl':
            self.budzet += (index_obj.cena + (index_obj.cena / 10))
            self.motocykle.pop(index_obj)
            return self.motocykle, self.budzet