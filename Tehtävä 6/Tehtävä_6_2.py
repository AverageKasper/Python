# Lisäsin heitto counterin extrana
import random as r

dice_sides = int(input("Syötä nopan tahkomäärä: "))
throw = 1

def dice(sides):
    dice_roll = r.randint(1,sides)
    return(dice_roll)

final_roll = dice(dice_sides)

while final_roll != dice_sides:
    print(f"Tulos oli {final_roll}, heitetään uudestaan")
    final_roll = dice(dice_sides)
    throw += 1
else:
    print(f"Nopan tulos on {final_roll}. Maksimi luku saavutettu {throw} heitossa")