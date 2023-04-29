# Dokumentasi Program To Do List
----


## Nama anggota  :
* Alisya Nisrina Sativa    (2209116005)
* Abdulah Faiz Tedjo Putro (2209116026)
* Awang M. Novandra A.     (2209116040)


## Deskripsi Program 

Program to-do list adalah program yang digunakan untuk membuat dan mengelola daftar tugas atau aktivitas yang harus dilakukan dalam suatu proyek atau kegiatan. Dengan menggunakan program ini, pengguna dapat memasukkan daftar tugas, menandai tugas yang sudah selesai, serta menghapus tugas yang sudah tidak diperlukan.

Biasanya, program to-do list dapat menampilkan daftar tugas dalam format yang mudah dibaca dan dapat disortir berdasarkan waktu, prioritas, atau kategori. Program ini juga dapat memiliki fitur pengingat atau notifikasi untuk membantu pengguna mengingat tugas-tugas yang harus dilakukan dalam waktu yang telah ditentukan.

Program to-do list biasanya digunakan oleh individu atau tim yang ingin mengelola tugas-tugas dalam suatu proyek atau kegiatan secara efektif dan efisien. Dengan menggunakan program to-do list, pengguna dapat mengoptimalkan produktivitas dan memastikan bahwa semua tugas yang harus dilakukan sudah dicatat dan dikerjakan dengan baik.


## Implementasi Module

Module yang digunakan dalam Project ini adalah sebagai berikut :


* Prettytable adalah sebuah modul Python yang dapat digunakan untuk membuat tabel dengan format yang estetis dan mudah dibaca.
* Datetime adalah sebuah modul Python yang digunakan untuk bekerja dengan tanggal dan waktu.
* Pwinput adalah sebuah modul Python yang digunakan untuk meminta input password dari pengguna dengan cara yang aman dan terenkripsi.
* Clear Screen (cls) merupakan modul untuk memberikan efek clear pada screen terminal. 
* Json merupakan sebuah modul Python yang digunakan untuk menyimpan dan bertukar data.
* MySQL Connector merupakan sebuah perangkat lunak yang digunakan untuk menghubungkan aplikasi dengan database MySQL. MySQL Connector menyediakan antarmuka untuk berkomunikasi dengan server database MySQL, sehingga aplikasi dapat membaca atau menulis data dari atau ke database. MySQL Connector dapat digunakan untuk mengakses dan memanipulasi data pada database MySQL, seperti melakukan query data, memasukkan data baru, mengubah data yang sudah ada, atau menghapus data dari database. Pada program ini, kami menggunakan database untuk menyimpan data history user.


## Penjelasan Program

Pada program to do list ini, kami menggunakan  linked list dengan jenis double linked list. Double linked list merupakan linked list dengan menggunakan pointer, dimana setiap node memiliki 3 field, yaitu 1 field pointer yang menunjuk pointer berikutnya (next), 1 field menunjuk pointer sebelumnya (prev), serta sebuah field yang berisi data untuk node tersebut.

Program ini memiliki multiuser admin dan pengguna. 
Privilege dari user admin adalah admin dapat melihat history dari seluruh pengguna dan admin juga dapat menghapus history para pengguna. 
Sedangkan privilege dari user pengguna adalah setiap pengguna dapat memasukkan to do list, menghapus to do list yang sudah dibuat oleh pengguna, menandai to do list yang sudah diselesaikan pengguna, menampilkan seluruh to do list yang telah dibuat, mencari to do list, mengurutkan to do list yang telah dibuat sesuai abjad, menampilkan history to do list pengguna, dan dapat menghapus seluruh to do listnya.


## Cara Penggunaan

#### Menu Awal
![image](https://user-images.githubusercontent.com/121870536/232696368-b1a4b68f-d458-40d7-9c31-c85c810ce1a6.png)

Pada saat menjalankan program, program akan menampilkan menu awal yang berisi tiga pilihan yaitu Login Admin, Login User, Register User.


#### Login Sebagai User
![image](https://user-images.githubusercontent.com/121870536/235283100-b3e6271f-b4ec-4d2a-8d67-4c87b6893335.png)

Jika kita login sebagai user maka program akan menampilkan beberapa pilihan yang dapat dilakukan seperti, Menambah To Do List, Menghapus To Do List, Menandai To Do List yang sudah selesai, Menampilkan To Do List, Mencari To Do List, Mengurutkan To Do List, Menampilkan History dan Menghapus semua History.


#### Tambah To Do List
![image](https://user-images.githubusercontent.com/121870536/235283386-97847970-0861-4d53-93a6-b867d0a5e9c9.png)

Untuk fungsi tambah, user dapat menambah atau membuat to do list dengan menginputkan seperti contoh pada gambar tersebut.


#### Hapus To Do List
![image](https://user-images.githubusercontent.com/121870536/235283474-1af4e535-a89d-4306-88c2-ada273553166.png)


#### Tandai To Do List yang selesai
![image](https://user-images.githubusercontent.com/121870536/235283583-8bd76c11-478a-45de-829e-a0a9bc04f94a.png)


#### Tampil To Do List
![image](https://user-images.githubusercontent.com/121870536/235283615-0bf103b6-c6ac-4197-bb0f-7a41b951d0a8.png)


#### Cari To Do List
![image](https://user-images.githubusercontent.com/121870536/235284173-5506c4bb-3c7e-45dc-a193-a70e89c28a69.png)


#### Mengurutkan To Do List
![image](https://user-images.githubusercontent.com/121870536/235284560-870b5de9-3f86-4b1f-be29-c9788b691c99.png)
![image](https://user-images.githubusercontent.com/121870536/235284569-b4cf11ea-0889-4187-ba8c-076356119ba9.png)



#### Menampilkan History To Do List
![image](https://user-images.githubusercontent.com/121870536/235284585-ef41a25a-a6dc-452f-82c5-d89807424c1c.png)


#### Menghapus Semua History To Do List
![image](https://user-images.githubusercontent.com/121870536/235284603-7a790f98-20c0-4546-9bb0-c6b5b5bacaa0.png)




#### Login Sebagai Admin
![image](https://user-images.githubusercontent.com/121870536/235282971-71247699-cd61-493b-81cc-5f0d2a869569.png)

Sedangkan jika kita login sebagai admin maka kita dapat melihat history dari user dan dapat menghapus history user


#### Tampilkan History User
![image](https://user-images.githubusercontent.com/121870536/235285476-1fd59012-dbb8-4d09-976e-1bd45c1c4128.png)


#### Hapus History User
![image](https://user-images.githubusercontent.com/121870536/235285497-a108af72-21c3-478c-b58a-813c5368ee3a.png)

