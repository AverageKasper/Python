gallon = float(input("Syötä gallona määrä: "))

def converter(g_amount):
    liter = g_amount * 3.785
    print(f"{g_amount} Gallonia on {liter} Litraa")
    
while gallon > 0:
    converter(gallon)
    gallon = float(input("Syötä gallona määrä: "))
else:
    print("Syötetty negatiivinen numero, ohjelma lopetetaan")