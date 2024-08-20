#Kesken
year = float(input("Syötä Vuosiluku: "))

if year % 4 == 0 :
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"Vuosi {year:.0f} on karkausvuosi")
        else:
            print(f"Vuosi {year:.0f} ei ole karkausvuosi")
    else:
        print(f"Vuosi {year:.0f} on karkausvuosi")
else:
    print(f"Vuosi {year:.0f} ei ole karkausvuosi")
