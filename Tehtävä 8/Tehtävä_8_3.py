import mysql.connector
from geopy.distance import geodesic

yhteys = mysql.connector.connect(
         host='localhost',
         database='flight_game',
         user='kasper',
         password='Monkey',
         autocommit=True,
         collation="utf8mb4_general_ci"
         )

def location(code):
    sql = f"select latitude_deg, longitude_deg from airport where ident = '{code}'"  
    kursori = yhteys.cursor()
    kursori.execute(sql)
    cords = kursori.fetchall()
    return(cords)
    
def distance(point_1,point_2):
    distance = geodesic(point_1, point_2).kilometers
    print(f"Etäisyys lentokenttien välillä on noin {distance:.2f} kilometriä.")

port1 = input("Syötä ensimmäisen lentokentän ICAO-koodi: ")
port2 = input("Syötä toisen lentokentän ICAO-koodi: ")
coord1 = location(port1)
coord2 = location(port2)
distance(coord1,coord2)