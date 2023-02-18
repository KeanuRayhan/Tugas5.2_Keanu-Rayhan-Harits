"""
Aplikasi Phone Book
oleh Keanu Rayhan Harits
NIM 221524043
Kelas 1B
"""

import json

#Function untuk membaca data phone book dari file
def bacaPhoneBook():
    try:
        with open("Phonebook.txt", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}
    return data

#Fungsi untuk menulis data phone book ke file
def tulisPhoneBook(data):
    with open("Phonebook.txt","w") as file:
        json.dump(data, file)

#Function untuk menambahkan kontak
def tambahKontak(nama, nomor):
    data = bacaPhoneBook()
    data[nama] = nomor
    tulisPhoneBook(data)

#Function untuk mencari kontak
def cariKontak(nama):
    data = bacaPhoneBook()
    if nama in data:
        return data[nama]
    else:
        return None

#Function untuk menampilkan kontak
def tampilkanKontak():
    data = bacaPhoneBook()
    print("Daftar Kontak")
    for nama, nomor in data.items():
        print(f"{nama}: {nomor}")

#Function untuk menghapus kontak
def hapusKontak(nama):
    data = bacaPhoneBook()
    if nama in data:
        del data[nama]
        tulisPhoneBook(data)
        return True
    else:
        return False

#Function untuk update data kontak
def updateKontak(nama, nomor):
    data = bacaPhoneBook()
    if nama in data:
        data[nama] = nomor
    tulisPhoneBook(data)


#Program Utama
while True:
    print("==========")
    print("Phone Book")
    print("==========")
    print("1. Tambah Kontak")
    print("2. Cari Kontak")
    print("3. Tampilkan Kontak")
    print("4. Hapus Kontak")
    print("5. Edit No Telepon")
    print("6. Keluar")

    pilih = input("Masukkan pilihan : ")

    #Perkondisian jika memilih 1 akan mengakses fitur Tambah Kontak
    if (pilih == "1"):
        nama = input("Masukkan nama : ")
        nomor = input("Masukkan nomor telepon : ")
        tambahKontak(nama, nomor)
        print("Kontak berhasil ditambahkan\n")

    #Perkondisian jika memilih 2 akan mengakses fitur Cari Kontak
    elif (pilih == "2"):
        nama = input("Masukkan nama : ")
        pencarian = cariKontak(nama)
        if pencarian:
            print("\nKontak ditemukan\n " + f"{nama}: {pencarian}" + "\n")
        else:
            print("Kontak tidak ditemukan\n")

    #Perkondisian jika memilih 3 akan mengakses fitur Tampilkan Semua Kontak
    elif (pilih == "3"):
        tampilkanKontak()
        print("\n")

    #Perkondisian jika memilih 4 akan mengakses fitur Hapus Kontak
    elif (pilih == "4"):
        nama = input("Masukkan nama: ")
        if hapusKontak(nama):
            print("Kontak berhasil dihapus\n")
        else:
            print("Kontak tidak ditemukan\n")

    #Perkondisian jika memilih 5 akan mengakses fitur Edit No.Telp Kontak
    elif (pilih == "5"):
        nama = input("Masukkan nama : ")
        nomor = input("Masukkan nomor telepon baru : ")
        updateKontak(nama, nomor)
        print("No. Telpon kontak berhasil diubah\n")

    #Perkondisian jika memilih 6 akan keluar program
    elif (pilih == "6"):
        print("Terima Kasih")
        break

    else:
        print("Pilihan tidak valid\n")
    
