import random
ran_gender = random.randint(1,6)
gender = str
if ran_gender == 1:
    gender = "he/him"
elif ran_gender == 2:
    gender = "she/her"
elif ran_gender == 3:
    gender = "they/them"
elif ran_gender == 4:
    gender = "dog"
elif ran_gender == 5:
    gender = "cat"
elif ran_gender == 6:
    gender = "bunny"
print(f"Your gender is {gender}")