num1 = input("Syötä ensimmäinen luku: ")
if not num1:
    print("Ilman numeroa ei saa listaa aikaiseksi") 
else:
    float(num1)
numlist = []
amount = 0
while num1:
    numlist.append(num1)
    num2 = input("Syötä seuraava luku: ")
    if not num2:
        numlist.sort(key=float,reverse=True)
        break
    else:
        float(num2)
        num1 = num2
print("Suurimmat luvut:")
for n in numlist:
    if amount < 5:
        print (n)
        amount = amount + 1