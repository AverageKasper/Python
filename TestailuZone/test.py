import random as r
def sum(list):
    score = 0
    for i in list:
        score += i
    return(score)

list_size = int(input("How many D20 to roll:"))
dice_list = []
for n in range(0, list_size):
    dice_score = r.randint(1,20)
    dice_list.append(dice_score)

print(f"Total score is {sum(dice_list)}")
print(f"Dice totals are {dice_list}")