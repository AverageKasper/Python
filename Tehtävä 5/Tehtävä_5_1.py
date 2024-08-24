import random as r
dice_amount = int(input("Montako noppaa heitetään: "))
dice = []
score = 0
while dice_amount > 0:
    roll = r.randint(1,6)
    dice.append(roll)
    dice_amount = dice_amount - 1
for n in dice:
     score = score + n 
print(f"Noppien kokonais tulo : {score}")
