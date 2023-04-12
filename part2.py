from prettytable import PrettyTable
import datetime
from loginawal import *

class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False
        self.next = None
        self.created_at = datetime.datetime.now()
        self.deleted_at = None

class ToDoList:
    def __init__(self):
        self.head = None
        self.history = []
    
    def add_task(self, description):
        task = Task(description)
        if self.head is None:
            self.head = task
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = task
        self.history.append(('Menambahkan', task.description, task.created_at))
    
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
                self.history.append(('Menghapus', current.description, current.deleted_at))
                return True
            previous = current
            current = current.next
        print("<<< To Do List Masih Kosong / To Do List Tidak Ada >>>")
        return os.system("pause")
    
    def complete_task(self, description):
        current = self.head
        while current is not None:
            if current.description == description:
                current.completed = True
                return True
            current = current.next
        print("<<< To Do List Masih Kosong >>>")
        return os.system("pause")
    
    def display_list(self):
        current = self.head
        while current is not None:
            if current.completed:
                print("[x]", current.description)
            else:
                print("[ ]", current.description)
            current = current.next

    def show_history(self):
        if self.history == []:
            print("Tidak Ada History")
        else:
            table = PrettyTable()
            table.field_names = ["Keterangan","To Do List","Waktu"]
            for i in self.history:
                table.add_row(i)
            print(table)

    def jump_search_task(self, description):
        tasks = self.sort_tasks()
        n = len(tasks)
        jump = int(n**0.5)
        left = 0
        right = 0
        
        while right < n and tasks[right].description < description:
            left = right
            right = min(right+jump, n-1)
        
        for i in range(left, right+1):
            if tasks[i].description == description:
                return tasks[i]
        return None
    
    def sort_tasks(self):
        tasks = []
        current = self.head
        while current is not None:
            tasks.append(current)
            current = current.next
        tasks.sort(key=lambda task: task.description)
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
            
            while i < len(left_data) and j < len (right_data):
                if left_data[i] < right_data[j]:
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
    
    def mergesortdesc(self,data):
        if len(data) > 1:
            mid = len(data) // 2
            left_data = data[:mid]
            right_data = data[mid:]

            self.mergesortdesc(left_data)
            self.mergesortdesc(right_data)

            i = j = k=0
            
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
                print("6. Mengurutkan To Do List sesuai Abjad ")
                print("7. Tampilkan History Input dan Delete Data ")
                print("8. Hapus Semua To Do List")
                print("9. Exit")
                print(60*"=")
                pilihan = input("Masukkan pilihan anda : ")
                if pilihan == '1':
                    tdl = input("Masukkan to do list terbaru : ")
                    if len(tdl) > 50:
                        print("<<< to do list tidak boleh lebih dari 50 huruf (spasi juga dihitung) >>>")
                    else:
                        self.add_task(tdl)
                        os.system("cls")
                elif pilihan == '2':
                    hapus = input("Masukkan to do list yang ingin dihapus : ")
                    self.remove_task(hapus)
                    os.system("cls")
                elif pilihan == '3':
                    tanda = input("Masukkan to do list yang sudah selesai : ")
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
                    x = input("Masukkan Pilihan (1/2) : ")
                    hasil = self.mergesortasc(pilah)
                    self.tampilansort(hasil)
                    input("Tekan Enter untuk melanjutkan...")
                elif pilihan == '7':
                    self.show_history()
                    input("Tekan Enter untuk melanjutkan...")
                    os.system("cls")
                elif pilihan == '8':
                    cursor.execute("DELETE FROM"+" "+printtabel)
                    print("<<< History Telah Dihapus >>>")
                    input("Tekan Enter untuk melanjutkan...")
                    os.system("cls")
                else:
                    os.system("cls")
                    break
            except ValueError and KeyboardInterrupt:
                os.system("cls")
                print(" !!! Mohon Masukkan Pilihan yang Tersedia !!! ")

    def aluradmin(self):
        global printtabel
        global x
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
                        print("<<< Username tidak ditemukan >>>")
                    input("Tekan Enter untuk melanjutkan...")
                    os.system("cls")
                elif pilihan == '2':
                    lihat = input("Masukkan username user yang ingin dihapus historynya : ")
                    if lihat in data_1["username"]:
                        indexuser = data_1["username"].index(lihat)
                        tabeluser = namatabel(indexuser)
                        cursor.execute("DELETE FROM"+" "+tabeluser)
                        print("<<< History Telah Dihapus >>>")
                        input("Tekan Enter untuk melanjutkan...")
                        os.system("cls")
                    else:
                        print("<<< Username Tidak Ditemukan >>>")
                        os.system("pause")
                    os.system("cls")
                else:
                    os.system("cls")
                    print(" !!! Mohon Masukkan Pilihan yang Tersedia !!! ")
                    break
            except ValueError and KeyboardInterrupt:
                os.system("cls")
                print("Mohon Masukkan Pilihan yang Tersedia")
                
    def mulai(self):
        global printtabel
        while True:
            try:
                print("Selamat datang di program pembuatan to do list\nSilahkan login terlebih dahulu")
                print("1. Login Admin\n2. Login User\n3. Register User\nPRESS ENTER FOR EXIT")
                x = input("Masukkan Pilihan Anda : ")
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
                print("<<<  Mohon Masukkan Pilihan yang Benar >>>")

            
import os
kaka = ToDoList()
kaka.mulai()
