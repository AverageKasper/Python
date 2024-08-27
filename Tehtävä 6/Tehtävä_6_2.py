#Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän. 
# Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa. 
# Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan nopan maksimisilmäluku, 
# joka kysytään käyttäjältä ohjelman suorituksen alussa.#
import random as r
dice_sides = int(input("Nopan tahkomäärä: "))
def dice(sides):
    dice_roll = r.randint(1,sides)
    if dice_roll != sides:
        print(f"Tulos on {dice_roll}, heitetään uudestaan")
        dice(dice_sides)
    elif dice_roll == sides:
        return()

dice(dice_sides)
print(f"Noppa tulos on {dice_sides}, yippee")