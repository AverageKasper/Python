leiviskä = float(input("Anna leiviskät: "))
naula = float(input("Anna naulat: "))
luoti = float(input("Anna luodit: "))

luoti_paino = 13.3
naula_paino = luoti_paino * 32
leiviskä_paino = naula_paino * 20

leiviskä_2 = leiviskä*leiviskä_paino
luoti_2 = luoti * luoti_paino
naula_2 = naula * naula_paino

kokopaino = float(leiviskä_2+luoti_2+naula_2)
kg = int(kokopaino/1000)
gramma = kokopaino-kg*1000

print(f"Massa nykymittojen mukaan\n{int(kg)} Kilogrammaa ja {gramma:.2f} grammaa")