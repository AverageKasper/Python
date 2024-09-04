# Lisäsin heitto counterin extrana
import random as r

throw = 1

def dice():
    dice_roll = r.randint(1,6)
    return(dice_roll)

final_roll = dice()

while final_roll != 6:
    print(f"Nopan tulos on {final_roll}, heitetään uudestaan")
    final_roll = dice()
    throw += 1
else:
    print(f"Lopputulos {final_roll}, saavutettu {throw} heitossa")