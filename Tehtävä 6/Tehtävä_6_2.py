#Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän. 
# Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa. 
# Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan nopan maksimisilmäluku, 
# joka kysytään käyttäjältä ohjelman suorituksen alussa.#

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
