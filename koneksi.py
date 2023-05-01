import mysql.connector
from colorama import Fore,Style

def database():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database = "asd")
        if mydb.is_connected():
            return mydb
    except Exception as error:
        if error:
            print(Fore.RED + f'Error:\n{error}.',Style.RESET_ALL)
            print(Fore.GREEN+"Harap nyalakan Apache dan MySQL di XAMPP dahulu, lalu buat database dengan nama \'asd\'",Style.RESET_ALL)
            exit()
