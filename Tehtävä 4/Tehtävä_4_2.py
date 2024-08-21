number_inch = 5
while number_inch >= 0:
    number_inch = float(input("Syötä tuuma: "))
    number_cm = number_inch * 2.54
    if number_inch >= 0: 
        print(f"{number_inch:.2f} Tuumaa on {number_cm:.2f} Senttimetriä.")
    else:
        print("Negatiivisia lukuja ei tueta.")
else:
    pass