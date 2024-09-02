import mysql.connector

yhteys = mysql.connector.connect(
         host='localhost',
         database='flight_game',
         user='kasper',
         password='Monkey',
         autocommit=True,
         collation="utf8mb4_general_ci"
         )

def airport_type(code):
    sql = f"select type,count(type) from airport where iso_country = '{code}' group by type;"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount >0:
        print(f"Maan lentokentät ovat seuraavan tyyppiset: ")
        for rivi in tulos:
            print(f"{rivi[0]}: {rivi[1]}")
    else:
        print("Virheellinen maakoodi")
country = input("Syötä maakoodi: ")
airport_type(country)