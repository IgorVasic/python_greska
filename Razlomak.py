from fractions import Fraction


class Razlomak(object):
    """
    Ovo je klasa razlomak
    """
    def __init__(self, brojnik, nazivnik):
        self.brojnik = brojnik
        self.nazivnik = nazivnik



    @property
    def brojnik(self):
        return self._brojnik


    @brojnik.setter
    def brojnik(self, value):
        self._brojnik = value


    @property
    def nazivnik(self):
        return self._nazivnik

    @nazivnik.setter
    def nazivnik(self,value):
        self._nazivnik = value




    def skrati(self):
        return Fraction(self.brojnik, self.nazivnik)



#1.2
    def __str__(self):
        return f'{self.brojnik:d}|{self.nazivnik:d}'
    def __repr__(self):
        return f"Razlomak({self.brojnik:d}, {self.nazivnik:d})"
    def
r2 = Razlomak(12,36)
r3 = Razlomak(22,48)

print(repr(r2))






