#Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen nopan silmäluvun väliltä 1..6. 
# Kirjoita pääohjelma, joka heittää noppaa niin kauan kunnes tulee kuutonen. 
# Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.
import random as r
def noppa():
    noppa_luku = r.randint(1,6)
    if noppa_luku != 6:
        print(f"Tulos on {noppa_luku}, heitetään uudestaan")
        noppa()
    elif noppa_luku == 6:
        print(f"Noppa tulos on {noppa_luku}, yippee")
    return()
noppa()

