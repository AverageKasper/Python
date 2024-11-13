from flask import Flask, request
import mysql.connector
app = Flask(__name__)
@app.route('/airport/<icao>')
def airport(icao):

    connector = mysql.connector.connect(
         host='localhost',
         database='flight_game',
         user='kasper',
         password='Monkey',
         autocommit=True,
         collation="utf8mb4_general_ci"
         )
    
    try:
        sql = f"select name,municipality,ident from airport where ident = '{icao}';"
        cursor = connector.cursor()
        cursor.execute(sql)
        info = cursor.fetchall()
        info_dict = {
            "ICAO" : info[0][2],
            "Name" : info[0][0],
            "Municipality" : info[0][1]
        }
        return info_dict
    except mysql.connector.Error as e:
        return {
            "Shit broke" : e,
        }
   
if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=4000)
