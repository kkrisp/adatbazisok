# ENGLISH
# This is a project that simulates of the growth 
# of a random recursive tree. Made for the class
# 'Stochastic processes', in ELTE. Because the
# class is in hungarian, the project is commented
# and documented in hungarian as well.
# MAGYAR
# Veletlen rekurziv fat szimulalo kod. Az ELTE
# fizika szakos Veletlen fizikai folyamatok
# orara keszult.
import sys
import argparse
import math
import random
import matplotlib


class Csucs:
    """Egy graf csucsat szimulalo osztaly
    'azonosito' az megkulonboztetesre szolgalo szam
    'kapcsolat' azon csucsok azonositojanak listaja,
    melyhez ebbol a csucsbol el vezet."""
    def __init__(self, azonosito=0, kapcsolat=None):
        self.azonosito = azonosito
        self.kapcsolat = []
        self.fokszam = 0
    
    def uj_el(self, uj_azonosito):
        self.kapcsolat.append(uj_azonosito)
        self.fokszam += 1


class Veletlen_Rekurziv_Fa:
    def __init__(self):
        self.csucsok = [Csucs(0)]
        self.N_csucs = 1
        self.elek_szama = 0
    
    def uj_csucs(self):
        self.csucsok.append(Csucs(self.N_csucs))
        veletlen_csucs = random.randint(0, self.N_csucs-1)
        self.csucsok[self.N_csucs].uj_el(veletlen_csucs)
        self.csucsok[veletlen_csucs].uj_el(self.N_csucs)
        #print("Az uj, {} csucs a {} csucshoz kapcsolodott.".format(self.csucsok[self.N_csucs].azonosito, veletlen_csucs) )
        self.N_csucs += 1
        self.elek_szama += 1
        #print("Most mar {} csucs van.".format(self.N_csucs) )
    
    def atlagos_fokszam(self):
        N_osszes = 0
        for cs in self.csucsok:
            #print("Az {} csucs fokszama {}".format(cs.azonosito, cs.fokszam) )
            N_osszes += cs.fokszam
        return N_osszes/len(self.csucsok)

fa = Veletlen_Rekurziv_Fa()

fajl = open("atlagos_fokszameloszlas.dat", 'w')

for i in range(12):
    fajl.write("{}, {:.3f}\n".format(i, fa.atlagos_fokszam()))
    fa.uj_csucs()