#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi. 
#Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.
num1 = input("Syötä ensimmäinen luku: ")
if not num1:
    print("Ilman numeroa ei saa listaa aikaiseksi") 
else:
    float(num1)
numlist = []
while num1:
    numlist.append(num1)
    num2 = input("Syötä seuraava luku: ")
    if not num2:
        numlist.sort(key=float)
        print(f"Listan pienin luku on {numlist[0]} ja suurin luku on {numlist[-1]}")
        break
    else:
        float(num2)
        num1 = num2
else:
    pass