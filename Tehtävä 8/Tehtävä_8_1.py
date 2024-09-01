import mysql.connector

def airport_finder(icao):
    sql = f"select name, municipality from airport where airport.ident = '{icao}';"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount >0:
        for rivi in tulos:
            print(f"Lentokentän nimi on {rivi[0]}, kaupungista {rivi[1]}")

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