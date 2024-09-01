import mysql.connector

def airport_finder(icao):
    sql = f"select airport.name as 'airport name', country.name as 'country name' from airport,country where airport.iso_country = country.iso_country and airport.ident = '{icao}';"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount >0:
        for rivi in tulos:
            print(f"Lentokentän nimi on {rivi[0]}, ja maa on {rivi[1]}")

yhteys = mysql.connector.connect(
         host='localhost',
         database='flight_game',
         user='kasper',
         password='Monkey',
         autocommit=True,
         collation="utf8mb4_general_ci"
         )

icao = input("Syötä lentokentän ICAO-koodi: ")
airport_finder(icao)