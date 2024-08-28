#Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen nopan silmäluvun väliltä 1..6. 
# Kirjoita pääohjelma, joka heittää noppaa niin kauan kunnes tulee kuutonen. 
# Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.
import random as r

def dice():
    dice_roll = r.randint(1,6)
    return(dice_roll)

final_roll = dice()

while final_roll != 6:
    print(f"Nopan tulos on {final_roll}, heitetään uudestaan")
    final_roll = dice()
else:
    print(f"Lopputulos {final_roll}")