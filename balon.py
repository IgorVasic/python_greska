class Balon(object):
    """
    klasa balon
    """
    """
    staticki atribut
    """
    jedinstvene_boje = set()#prazan skup pamti koje smo boje koristili

    def __init__(self, boja):
        self.boja = boja
        Balon.jedinstvene_boje.add(boja)

