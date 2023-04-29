from prettytable import PrettyTable
import datetime
from LOGINNNNNNNNN import *
import mysql.connector
from colorama import Fore,Style

class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False
        self.next = None
        self.created_at = datetime.datetime.now()
        self.deleted_at = None

class ToDoList:
    global cursor
    global mydb
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database = "asd")
        
    cursor = mydb.cursor()
    
    def __init__(self):
        self.head = None
    
    def add_task(self, description):
        task = Task(description)
        if self.head is None:
            self.head = task
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = task
        sql = "INSERT INTO"+" "+printtabel+" "+"(status, keterangan, waktu) VALUES (%s , %s, %s)"
        val = ("menambahkan", task.description, task. created_at)
        cursor.execute(sql, val)
        mydb.commit()
    
    def remove_task(self, description):
        current = self.head
        previous = None
        while current is not None:
            if current.description == description:
                current.deleted_at = datetime.datetime.now()
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                sql = "INSERT INTO"+" "+printtabel+" "+"(status, keterangan, waktu) VALUES (%s , %s, %s)"
                val = ("menghapus", current.description, current.created_at)
                cursor.execute(sql, val)
                mydb.commit()
                return True
            previous = current
            current = current.next
        print(Fore.RED + "<<< To Do List Masih Kosong / To Do List Tidak Ada >>>",Style.RESET_ALL)
        return input("Tekan Enter untuk melanjutkan...")
    
    def complete_task(self, description):
        current = self.head
        while current is not None:
            if current.description == description:
                current.completed = True
                return True
            current = current.next
        print(Fore.RED + "<<< To Do List Masih Kosong >>>",Style.RESET_ALL)
        return input("Tekan Enter untuk melanjutkan...")
    
    def display_list(self):
        current = self.head
        while current is not None:
            if current.completed:
                print("[x]", current.description)
            else:
                print("[ ]", current.description)
            current = current.next

    def show_history(self):
        cursor.execute("SELECT * FROM"+" "+printtabel)
        table = PrettyTable()
        table.field_names = [i for i in cursor.column_names]
        for i in cursor:
            table.add_row(i)
        print(table)

    def jump_search_task(self, description):
        try:
            tasks = self.sort_tasks()
            n = len(tasks)
            jump = int(n**0.5)
            left = 0
            right = jump
            
            while right < n and tasks[right].description < description:
                left = right
                right += jump
            
            for i in range(left, min(right,n)):
                if tasks[i].description == description:
                    return tasks[i]
            return None
        except ValueError and KeyboardInterrupt:
            print(Fore.RED + "<<< harap input data yang benar >>>",Style.RESET_ALL)
    
    def sort_tasks(self):
        tasks = []
        current = self.head
        while current is not None:
            tasks.append(current)
            current = current.next
        tasks.sort(key=lambda tasks: tasks.description)
        return tasks
    

    def sort(self):
        sudah = []
        belum = []
        current = self.head
        while current is not None:
            if current.completed == True:
                sudah.append((current.description))
            elif current.completed == False:
                belum.append((current.description))
            current = current.next   
        return sudah + belum
    
    def mergesortasc(self,data):
        if len(data) > 1:
            mid = len(data) // 2
            left_data = data[:mid]
            right_data = data[mid:]

            self.mergesortasc(left_data)
            self.mergesortasc(right_data)

            i = j = k=0

            if x == '1':
                while i < len(left_data) and j < len (right_data):
                    if left_data[i] < right_data[j]:
                        data[k]= left_data[i]
                        i += 1
                        k += 1

                    else:
                        data[k] = right_data[j]
                        j += 1
                        k += 1
            elif x == '2':
                while i < len(left_data) and j < len (right_data):
                    if left_data[i] > right_data[j]:
                        data[k]= left_data[i]
                        i += 1
                        k += 1

                    else:
                        data[k] = right_data[j]
                        j += 1
                        k += 1

            while i < len(left_data):
                data[k] = left_data[i]
                i += 1
                k += 1

            while j < len(right_data):
                data[k] = right_data[j]
                j += 1
                k += 1
        return data
    
    def tampilansort(self,hasil):
        no = 1
        table = PrettyTable(["urutan","To do list"])
        for i in range(len(hasil)):
            table.add_row([no,hasil[i]])
            no +=1
        print(table)
        
    
    def aluruser(self):
        global x
        while True:
            try:
                print(60*"=")
                print("1. Tambahkan To Do List")
                print("2. Hapus To Do List ")
                print("3. Tandai To Do List yang Selesai")
                print("4. Tampilkan To Do List")
                print("5. Cari To Do List")
                print("6. Mengurutkan To Do List sesuai abjad ")
                print("7. Tampilkan History Input dan Delete Data ")
                print("8. Hapus History Semua To Do List")
                print("9. Exit")
                print(60*"=")
                pilihan = input("Masukkan pilihan anda : ")
                if pilihan == '1':
                    tdl = input("Masukkan to do list terbaru : ")
                    if len(tdl) > 50:
                        print(Fore.RED + "<<< to do list tidak boleh lebih dari 50 huruf (spasi juga dihitung) >>>",Style.RESET_ALL)
                    elif tdl == "":
                        print(Fore.RED + "<<< harap tidak menginput data kosong >>>",Style.RESET_ALL)
                    else:
                        self.add_task(tdl)
                        os.system("cls")
                elif pilihan == '2':
                    hapus = input("Masukkan to do list yang ingin dihapus : ")
                    self.remove_task(hapus)
                    os.system("cls")
                elif pilihan == '3':
                    tanda = input("Masukkan to do list yang sudah kelar : ")
                    self.complete_task(tanda)
                    os.system("cls")
                elif pilihan == '4':
                    self.display_list()
                    input("Tekan Enter untuk melanjutkan...")
                    os.system("cls")
                elif pilihan == '5':
                    tdl = input("Masukkan to do list yang ingin dicari : ")
                    task = self.jump_search_task(tdl)
                    if task is not None:
                        table = PrettyTable(['Description', 'Completed', 'Created At'])
                        table.add_row([task.description, task.completed, task.created_at])
                        print(table)
                    else:
                        print(f"Task dengan description '{tdl}' tidak ditemukan.")
                    input("Tekan Enter untuk melanjutkan...")
                    os.system("cls")
                elif pilihan == '6':
                    pilah = self.sort()
                    print("1. Ascending\n2. Descending")
                    x = input("masukkan pilihan (1/2) : ")
                    hasil = self.mergesortasc(pilah)
                    self.tampilansort(hasil)
                    input("Tekan Enter untuk melanjutkan...")
                elif pilihan == '7':
                    self.show_history()
                    input("Tekan Enter untuk melanjutkan...")
                    os.system("cls")
                elif pilihan == '8':
                    cursor.execute("DELETE FROM"+" "+printtabel)
                    print(Fore.RED + "<<< history telah dihapus >>>",Style.RESET_ALL)
                    input("Tekan Enter untuk melanjutkan...")
                    os.system("cls")
                else:
                    os.system("cls")
                    break
            except ValueError and KeyboardInterrupt:
                os.system("cls")
                print("harap masukkan pilihan yang tersedia")

    def aluradmin(self):
        global printtabel
        while True:
            try:
                print(65*"=")
                print("1. Tampilkan History Input dan Delete Data User")
                print("2. Hapus History User")                
                print("3. Exit")
                print(65*"=")
                pilihan = input("Masukkan pilihan anda : ")
                if pilihan == '1':
                    lihat = input("Masukkan username user yang ingin dilihat historynya : ")
                    if lihat in data_1["username"]:
                        indexuser = data_1["username"].index(lihat)
                        printtabel = namatabel(indexuser)
                        self.show_history()
                    else:
                        print(Fore.RED + "<<< username tidak ditemukan >>>",Style.RESET_ALL)
                    input("Tekan Enter untuk melanjutkan...")
                    os.system("cls")
                elif pilihan == '2':
                    lihat = input("Masukkan username user yang ingin dihapus historynya : ")
                    if lihat in data_1["username"]:
                        indexuser = data_1["username"].index(lihat)
                        tabeluser = namatabel(indexuser)
                        cursor.execute("DELETE FROM"+" "+tabeluser)
                        print(Fore.RED + "<<< history telah dihapus >>>",Style.RESET_ALL)
                        input("Tekan Enter untuk melanjutkan...")
                        os.system("cls")
                    else:
                        print(Fore.RED + "<<< username tidak ditemukan >>>",Style.RESET_ALL)
                        os.system("pause")
                    os.system("cls")
                else:
                    os.system("cls")
                    print(Fore.RED + "<<< harap masukkan pilihan yang tersedia >>>",Style.RESET_ALL)
                    break
            except ValueError and KeyboardInterrupt:
                os.system("cls")
                print("harap masukkan pilihan yang tersedia")
    
    def mulai(self):
        global printtabel
        while True:
            try:
                print("Selamat datang di program pembuatan to do list\nSilahkan login terlebih dahulu")
                print("1. Login Admin\n2. Login User\n3. Register User\nPRESS ENTER FOR EXIT")
                x = input("masukkan pilihan anda : ")
                if x == '1':
                    login_admin()
                    self.aluradmin()
                elif x == '2':
                    printtabel = login_user()
                    self.aluruser()
                elif x == '3':
                    tambah_user()
                else:
                    break
            except ValueError and KeyboardInterrupt:
                os.system("cls")
                print(Fore.RED + "<<<  harap masukkan pilihan yang benar >>>",Style.RESET_ALL)

            
import os
os.system("cls")
kaka = ToDoList()
kaka.mulai()
