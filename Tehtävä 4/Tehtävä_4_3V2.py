num = input("Syötä ensimmäinen luku: ")
if not num :
    print("Ilman numeroa ei saa listaa aikaiseksi")
else:
    float(num)
nummin = num
nummax = num
while num:
    if float(num) < float(nummin):
        nummin = num
    elif float(num) > float(nummax):
        nummax = num
    num = input("Syötä seuraava luku: ")
    if not num:
        print(f"Listan pienin luku on {nummin} ja suurin luku on {nummax}")
        break
    else:
        float(num)
else:
    pass