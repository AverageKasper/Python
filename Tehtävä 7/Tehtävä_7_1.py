#Nyt en keksinyt viisaampaa ratkaisua
seasons = ("kevät", "kesä", "syksy", "talvi")
months = int(input("Syötä monesko kuukausi: "))
if months == 3 or months == 4 or months == 5:
    print(f"{months}. kuukausi on {seasons[0]} aikaa")
elif months == 6 or months == 7 or months == 8:
    print(f"{months}. kuukausi on {seasons[1]} aikaa")
elif months == 9 or months == 10 or months == 11:
    print(f"{months}. kuukausi on {seasons[2]} aikaa")
elif months == 12 or months == 1 or months == 2:
    print(f"{months}. kuukausi on {seasons[3]} aikaa")
else:
    print(f"Syötetty virheellinen kuukausi")