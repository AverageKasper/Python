#Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina ja palauttaa paluuarvonaan vastaavan litramäärän.
#Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi. 
#Muunnos on tehtävä aliohjelmaa hyödyntäen. Muuntamista jatketaan siihen saakka, kunnes käyttäjä syöttää negatiivisen gallonamäärän.
#Yksi gallona on 3,785 litraa.

gallon = float(input("Syötä gallona määrä: "))

def converter(g_amount):
    liter = g_amount * 3.785
    print(f"{g_amount} Gallonia on {liter} Litraa")
    
while gallon > 0:
    converter(gallon)
    gallon = float(input("Syötä gallona määrä: "))
else:
    print("Syötetty negatiivinen numero, ohjelma lopetetaan")