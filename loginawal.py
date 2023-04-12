import os
import pwinput
import json
import mysql.connector

mydb = mysql.connector.connect(
    host="sql12.freemysqlhosting.net",
    user="sql12611967",
    password="dbopan7",
    database= "sql12611967"
    )

mycursor = mydb.cursor()

def tambahtabel():
    global x
    while True:
        x = str(input("Masukkan Nama Tabel History : "))
        if x == "":
            print("<<< Nama Tabel Tidak Boleh Kosong !!! >>>")
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
        print("<<< Nama Tabel Tidak Ada Di Database >>>")

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
    global tabelhistory
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
                    print("\n <<< Password Anda Salah >>> \nSilahkan Coba Kembali\n")
            except ValueError:
                print("\n<<< Username Anda Salah >>> \nSilahkan Coba Kembali\n")

def tambah_user():
    while True:
        try:
            username = input("Masukkan Username Baru Anda : ")
            if username.isalnum()==False:
                print("<<< Username tidak boleh ada spasi, simbol dan kosong >>>")
            elif username in data_1["username"]:
                print("<<< Maaf, Username telah digunakan >>>")
            elif username not in data_1["username"]:
                password=str(pwinput.pwinput("Masukkan Password : ")).replace("\t","").replace(" ","")
                if password =="":
                    print("!!! Password dilarang kosong dan menggunakan spasi !!! ")
                else:
                    tambahtabel()
                    data_1["username"].insert(indextabel(),username)
                    data_1["password"].insert(indextabel(),password)
                    os.system('cls')
                    print("Registrasi berhasil ^____^")
                    settingUser()
                    break
        except ValueError:
            print ("<<< Dilarang memasukkan data kosong !!! >>>")

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
                    print("\n <<< Password Anda Salah >>> \nSilahkan Coba Kembali\n")
            except ValueError:
                print("\n <<< Username Anda Salah >>> \nSilahkan Coba Kembali\n")
