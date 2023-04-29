import os
import pwinput
import json
from colorama import Fore,Style
from koneksi import database

conn = database()
mycursor = conn.cursor()

def tambahtabel():
    global x
    while True:
        x = str(input("masukkan nama tabel history : ")).replace(" ","_")
        if x == "":
            print(Fore.RED + "nama tabel tidak boleh kosong ❗❗❗",Style.RESET_ALL)
        else:
            mycursor.execute("CREATE TABLE"+" "+x+" "+"(status VARCHAR(20), keterangan VARCHAR(50), waktu VARCHAR(30))")
            break

def indextabel():
    mycursor.execute("show tables")
    indexnama = x
    tampung = []
    for row in mycursor:
        for i in row:
            tampung.append(i)
    if indexnama in tampung:
        return(tampung.index(indexnama))
    else:
        print(Fore.RED + "nama tabel tidak ada di database ❗❗❗",Style.RESET_ALL)

def namatabel(index):
    mycursor.execute("show tables")
    tampung = []
    for row in mycursor:
        for i in row:
            tampung.append(i)
    for i in range(len(tampung)):
        if i == index:
            return(tampung[index])

admin = {"username" : ["novan", "lisya", "faiz"],
         "password" : ["awd", "admin2", "admin3"]}

file_json = open("dataUser.json")
data_1 = json.loads(file_json.read())
def settingUser():
	with open("dataUser.json", "w") as dataBaru:
		json.dump(data_1, dataBaru)
		
def login_user():
    while True:
        username = input("Silahkan Masukkan Username Anda : ")
        password = pwinput.pwinput ("Silahkan Masukkan Password Anda : ")
        if password.isnumeric:
            try:
                login = data_1["username"].index(username)
                if username == data_1["username"][login] and password == data_1["password"][login]:
                    tabelhistory = str(namatabel(login))
                    os.system('cls')
                    return tabelhistory
                else:
                    print(Fore.RED + "\nPassword Anda Salah ❗❗❗ \nSilahkan Coba Kembali\n",Style.RESET_ALL)
            except ValueError:
                print(Fore.RED + "\nUsername Anda Salah❗❗❗ \nSilahkan Coba Kembali\n",Style.RESET_ALL)

def tambah_user():
    while True:
        try:
            username = input("Masukkan Username Baru Anda : ")
            if username.isalnum()==False:
                print(Fore.RED + "Username tidak boleh ada spasi, simbol dan kosong ❗❗❗",Style.RESET_ALL)
            elif username in data_1["username"]:
                print(Fore.RED + "Username telah digunakan ❗❗❗",Style.RESET_ALL)
            elif username not in data_1["username"]:
                password=str(pwinput.pwinput("Masukkan password : ")).replace("\t","").replace(" ","")
                if password =="":
                    print(Fore.RED + "Password dilarang kosong dan menggunakan spasi ❗❗❗",Style.RESET_ALL)
                else:
                    tambahtabel()
                    data_1["username"].insert(indextabel(),username)
                    data_1["password"].insert(indextabel(),password)
                    os.system('cls')
                    print(Fore.GREEN + "Registrasi berhasil ^____^",Style.RESET_ALL)
                    settingUser()
                    break
        except ValueError:
            print (Fore.RED + "Dilarang memasukkan data kosong ❗❗❗",Style.RESET_ALL)

def login_admin():
        while True:
            username = input("Silahkan Masukkan Username Anda : ")
            password = pwinput.pwinput ("Silahkan Masukkan Password Anda : ")
            try:
                login = admin.get("username").index(username)
                if username == admin.get("username")[login] and password == admin.get("password")[login]:
                    os.system('cls')
                    break
                else:
                    print(Fore.RED + "\nPassword Anda Salah ❗❗❗ \nSilahkan Coba Kembali\n",Style.RESET_ALL)
            except ValueError:
                print(Fore.RED + "\nUsername Anda Salah ❗❗❗ \nSilahkan Coba Kembali\n",Style.RESET_ALL)
