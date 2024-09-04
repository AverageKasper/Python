import random
num1 = int(input("Anna numero: "))
rand_num = random.randint(1,10)
while num1:
    if num1 < rand_num:
        num1 = int(input("Numerosi on liian pieni\nAnna uusi numero: "))
    elif num1 > rand_num:
        num1 = int(input("Numerosi on liian suuri\nAnna uusi numero: "))
    elif num1 == rand_num:
        print("Arvasit oikein")
        break