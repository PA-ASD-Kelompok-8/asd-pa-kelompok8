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

## Struktur Project

...

## Fitur dan Fungsionalitas

...

## Cara Penggunaan

#### Menu Awal
![image](https://user-images.githubusercontent.com/121870536/232696368-b1a4b68f-d458-40d7-9c31-c85c810ce1a6.png)

Pada saat menjalankan program, program akan menampilkan menu awal yang berisi tiga pilihan yaitu Login Admin, Login User, Register User.


#### Login Sebagai User
![image](https://user-images.githubusercontent.com/121870536/232704546-b658ac42-5601-4f9c-b7dc-5ed56c307f59.png)

Jika kita login sebagai user maka program akan menampilkan beberapa pilihan yang dapat dilakukan seperti, Menambah To Do List, Menghapus To Do List, Menandai To Do List yang sudah selesai, Menampilkan To Do List, Mencari To Do List dan Mengurutkan To Do List.


#### Login Sebagai Admin
![image](https://user-images.githubusercontent.com/121870536/232700594-b242517f-4168-4d43-bd0d-05ce971dad96.png)

Sedangkan jika kita login sebagai admin maka program akan menampilkan beberapa pilihan yang dapat dilakukan sama seperti login sebagai user namun ada satu kelebihan yaitu admin dapat Menampilkan History input dan delete data.



#### Tambah To Do List
![image](https://user-images.githubusercontent.com/121870536/232784999-760b9a5b-e05a-492c-8ebf-da3eb84ef0ef.png)

...

#### Hapus To Do List
![image](https://user-images.githubusercontent.com/121870536/232790372-5f3d3886-4291-4339-a886-9358495f07db.png)

...

#### Tandai To Do List yang selesai
















