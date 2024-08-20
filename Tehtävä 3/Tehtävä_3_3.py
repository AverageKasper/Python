gender = input("Sukupuoli (Mies/Nainen): ")
hemogob = float(input("Hemoglobiiniarvo (g/l): "))
if gender == "Mies":
    if hemogob < 117:
        print("Hemoglobiiniarvo alhainen.")
    elif hemogob >= 117 and hemogob <= 175:
        print("Hemoglobiiniarvo normaali.")
    elif hemogob > 175:
        print("Hemoglobiiniarvo korkea.")
elif gender == "Nainen":
    if hemogob < 134:
        print("Hemoglobiiniarvo alhainen.")
    elif hemogob >= 134 and hemogob <= 195:
        print("Hemoglobiiniarvo normaali.")
    elif hemogob > 195:
        print("Hemoglobiiniarvo korkea.")
else:
    print("Virheellinen sukupuoli")