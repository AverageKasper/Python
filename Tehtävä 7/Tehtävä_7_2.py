name_list = set()
name = input("Syötä nimi: ")
while name:
    if name in name_list:
        print("Aiemmin syötetty nimi")
    elif name not in name_list:
        print("Uusi nimi")
        name_list.add(name)
    name = input("Syötä nimi: ") 
print(f"Syötetyt nimet: {name_list}")