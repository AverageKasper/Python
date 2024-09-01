command = input("Syötä komento (uusi,etsi,lopeta): ")
airport_dict = {}
while True:
    if command == "uusi":
        airport_code = input("Syötä lentokentän ICAO-koodi: ")
        airport_name = input("Syötä lentokentän nimi: ")
        airport_dict[airport_code] = airport_name
    elif command == "etsi":
        code_search = input("Syötä lentokentän ICAO-koodi: ")
        # Estäää ohjelman kaatumisen jos koodia ei löydy listasta
        if code_search not in airport_dict:
            print(f"Antamasi lentokenttä ei löydy listasta")
        else:
            print(f"Lentokentän nimi on {airport_dict[code_search]}")
    elif command == "lopeta":
        print("Hyvästi")
        break
    # Komento nähdäkseen kaikki tallennetut tiedot
    elif command == "kaikki":
        print(airport_dict)
    command = input("Syötä komento (uusi,etsi,lopeta): ")