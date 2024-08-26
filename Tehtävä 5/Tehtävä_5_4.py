#Kirjoita ohjelma, joka kysyy käyttäjältä viiden kaupungin nimet yksi kerrallaan (käytä for-toistorakennetta nimien kysymiseen) 
# ja tallentaa ne listarakenteeseen. 
# Lopuksi ohjelma tulostaa kaupunkien nimet yksi kerrallaan allekkain samassa järjestyksessä kuin ne syötettiin. 
# käytä for-toistorakennetta nimien kysymiseen ja for/in toistorakennetta niiden läpikäymiseen.
city = []
for n in range(5):
    city_name = input("Syötä Kaupunki: ")
    city.append(city_name)
for i in city:
    print(i)