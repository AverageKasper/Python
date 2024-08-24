#Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa, onko se alkuluku. 
#Tässä tehtävässä alkulukuja ovat luvut, jotka ovat jaollisia vain ykkösellä ja itsellään.
#Esimerkiksi luku 13 on alkuluku, koska se voidaan jakaa vain luvuilla 1 ja 13 siten, että jako menee tasan.
#Toisaalta esimerkiksi luku 21 ei ole alkuluku, koska se voidaan jakaa tasan myös luvulla 3 tai luvulla 7.
num = int(input("Syötä kokonaisluku: "))
if num > 1:
    for n in range(2, (num//2)+1):
        if num % n == 0:
            print(f"Luku {num} ei ole alkuluku.")
            break
    else:
        print(f"Luku {num} on alkuluku")
else:
    print(f"Luku {num} ei ole alkuluku.1")