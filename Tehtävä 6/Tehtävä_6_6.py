#Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä sekä pizzan hinnan euroina. 
# Funktio laskee ja palauttaa pizzan yksikköhinnan euroina per neliömetri. 
# Pääohjelma kysyy käyttäjältä kahden pizzan halkaisijat ja hinnat sekä ilmoittaa, 
# kumpi pizza antaa paremman vastineen rahalle (eli kummalla on alhaisempi yksikköhinta). 
# Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.
import math as m

phalf_1 = float(input("Pizzan halkaisija senteissä: "))
peuro_1 = float(input("Pizzan hinta euroissa: "))
phalf_2 = float(input("Toisen pizzan halkaisija senteissä: "))
peuro_2 = float(input("Toisen pizzan hinta euroissa: "))

def pizza_calc(half, euro):
    pizza_rad = half / 2
    pizza_area = m.pi * (pizza_rad ** 2)
    area_in_sqm = pizza_area / 10000
    price = euro / area_in_sqm
    return(price)

if pizza_calc(phalf_1,peuro_1) < pizza_calc(phalf_2,peuro_2):
    print(f"Ensimmäinen pizza on halvempi (Pizza 1: {pizza_calc(phalf_1,peuro_1):.3f}eur/m², Pizza 2: {pizza_calc(phalf_2,peuro_2):.3f}eur/m²)")
else:
    print(f"Toinen pizza on halvempi (Pizza 1: {pizza_calc(phalf_1,peuro_1):.3f}eur/m², Pizza 2: {pizza_calc(phalf_2,peuro_2):.3f}eur/m²)")