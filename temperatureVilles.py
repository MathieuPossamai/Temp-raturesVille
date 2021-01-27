# coding: UTF-8
"""
Script: pythonProject6/temperatureVilles.py
Création: mpossamai, le 15/01/2021
"""


# Imports
import requests
import mysql.connector
import time
# Fonctions

def get_villes():
    cnx = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='bdd_temperaturevilles')
    cursor = cnx.cursor()
    cursor.execute("SELECT ville FROM temperaturevilles")
    result = cursor.fetchall()
    cnx.commit()
    cursor.close()
    cnx.close()
    list_villes = []

    for ville in result:
        list_villes += ville

    return list_villes

def get_temperature(ville):
    url="http://api.openweathermap.org/data/2.5/weather?q="+ville+",fr&units=metric&lang=fr&appid=0a73790ec47f53b9e1f2e33088a0f7d0"
    return float(requests.get(url).json()['main']['temp'])


def set_temperature_bdd(ville, temperature):
    cnx = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='bdd_temperaturevilles')
    cursor = cnx.cursor()
    update_val = ("UPDATE temperaturevilles SET temperature = (%s) WHERE ville = (%s)")
    data = (temperature, ville)
    cursor.execute(update_val, data)
    cnx.commit()
    cursor.close()
    cnx.close()
# Programme principal


def main():
    list_villes = get_villes()
    print("Liste des villes :",list_villes)
    while 1:
        print("refresh...")
        for ville in list_villes:
            set_temperature_bdd(ville, get_temperature(ville))
        print("Done !")
        time.sleep(300)


    pass
if __name__ == '__main__':
    main()
# Fin
