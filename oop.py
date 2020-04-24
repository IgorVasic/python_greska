class Stolica(object):
    """
    Klasa stolica

    def __init__(self, ime, broj_nogu = 4):
        self.ime = ime
        self.broj_nogu = broj_nogu



stolica1 = Stolica("Barcelona")
stolica2 = Stolica("Barska stolica", 1)

print(stolica1.ime)
print(stolica1.broj_nogu)
print(stolica2.ime)
print(stolica2.broj_nogu)


class Pravokutnik(object):
    def __init__(self, sirina, visina):
        self.sirina = sirina
        self.visina = visina

    def getSirina(self):
        return self.sirina


    def setSirina(self, value):
        self.sirina = value


    def getVisina(self): #pristupamo vrijednostima
        return self.visina


    def setVisina(self, value):#mjenjamo vrijednosti
        self.Visina = value



    def povrsina(self):#metoda unutar klase u ovom slucaju za racunanje povrsine pravokutnika
        return self.getSirina() * self.getVisina()
    #moze se direktno pristupiti atributima return self.sirina * self.visina

p = Pravokutnik(50,10)

print(p.povrsina())
p.setSirina(20)
print(p.povrsina())
"""
#property

class Pravokutnik(object):
    """
    Ova klasa predstavlja pravokutnik
    """

    def __init__(self, sirina, visina):
        self.sirina = sirina
        self.visina = visina

    #getter od svojstva

    @property
    def sirina(self):
        return  self._sirina#mjenjamo naziv da ne bi doslo do rekurzivnog poziva

    #setter od svojstva
    @sirina.setter
    def sirina(self,value):
        self._sirina = value

    @property
    def visina(self):
        return  self._visina #mjenjamo naziv da ne bi doslo do rekurzivnog poziva

    #setter od svojstva
    @visina.setter
    def visina(self,value):
        self._visina = value

    @property
    def povrsina(self):
        return self.sirina * self.visina


    def __str__(self):
        return f'{self.visina:d}|{self.sirina:d}'
    def __repr__(self):
        return f"Razlomak({self.visina:d}, {self.sirina:d})"

p1 = Pravokutnik(3,4)
p2 = Pravokutnik(3,4)

print(repr(p1))
print(repr(p2))

























