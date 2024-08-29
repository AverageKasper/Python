#Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. 
# Ohjelma palauttaa listassa olevien lukujen summan. 
# Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen palauttaman summan.

numlist = [1,2,3,4,5,6,7,8,9]

def laskuri(num):
    score = 0
    for i in num:
        score = score + i
    return(score)

print(f"Listan summa on {laskuri(numlist)}.")