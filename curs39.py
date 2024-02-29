#creati o baza de date numita orase care va contine tabelul orase
#cititi din fisierul worldwide.csv si scrieti in baza de date 
# implementati o functie care primeste ca parametru un nume si returneaza totul sub forma unei liste

import os
import mysql.connector
import shutil
import time
import csv
import re
from dateutil import parser
from datetime  import datetime
import os.path




class MySqlConnection:
    def __init__(self):
        self.mydb = mysql.connector.connect(host ='localhost', user='root', password = '12345678', database = 'worlwide')
        self.cursor =self.mydb.cursor()

    def adauga_in_baza_de_date(self,query):
        self.cursor.execute(query)
        self.mydb.commit()

    def selecteaza_din_baza_de_date(self,query):
        self.cursor.execute(query)
        rezultat = self.cursor.fetchall()
        return rezultat

mysqlcon=MySqlConnection()


class Citire:
    def __init__(self):
        pass

    def citeste_fisier(self, fisier):
        try:
            with open(fisier, newline='', encoding='utf-8') as file:
                cititor_csv = csv.reader(file)
                next(cititor_csv)
                for continut in cititor_csv:
                    try:
                        query = f"INSERT INTO `worlwide`.`world` VALUES(null,'{continut[1]}','{continut[4]}','{continut[5]}','{continut[6]}','{continut[8]}',{continut[9]});"
                        mysqlcon.adauga_in_baza_de_date(query)
                    except Exception as e:
                        print(f'Eroare la adăugarea în baza de date: {e}')
                        continue 
        except Exception as e:
            print(f'Eroare la citirea fișierului CSV: {e}')
    
    def afiseaza_nume(self,nume_tara):
        lista_tari = []
        query = f"SELECT city_ascii FROM `worlwide`.`world` WHERE country = '{nume_tara}'"
        rezultat=mysqlcon.selecteaza_din_baza_de_date(query)
        lista_tari.append(rezultat)
        print(lista_tari)

        


citire1 = Citire()
#citire1.citeste_fisier('D:\Python curs\curs39\worldcities.csv')
citire1.afiseaza_nume('Japan')