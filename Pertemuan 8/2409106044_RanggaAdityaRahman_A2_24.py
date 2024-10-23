# try:
#     angka = int(input("MAsukkan Angka : "))
# except ValueError:
#     print("Input SAlah (tolong masukkan angka)!!")



# def hitung():
#     print(angka)

# pilihan = int(input("pilihan"))

# if pilihan ==1:
#     print("MENU 1")

# elif pilihan == 2:
#     print("Menu 2")

# else:
#     print("Tidak ada")


# try:
#     angka = int(input("Masukkan angka: "))
# except ValueError:
#     print("Input yang anda masukkan bukan angka")
# else:
#     print(f"Angka yang kamu input: {angka}")
# finally:
#     print("Program selesai")

# try:
#     nama = input("Hello, what's your name? ")
#     if len(nama) > 5:
#         raise ValueError("Nama tidak boleh lebih dari 5 karakter")
# except ValueError as e:
#     print(e)



# menu1 = 0
# def menu():
#     print("=====================")
#     print("       MENU          ")
#     print("=====================")
#     print("1. Tambah")
#     print("2. keluar")
#     print("=====================")
#     menu1 = int(input("Pilihan = "))
#     return menu1

# def tambah():
#     try:
#         angka = int(input("Masukkan Angka Pertama : "))
#         angka2 = int(input("Masukkan Angka Kedua : "))
#         hasil = angka + angka2
#         print (hasil)
#     except ValueError:
#         print("Tolong Masukkan Angka")

# while True:
#     menu1 = menu()
#     if menu1 == 1:
#         tambah()
#     elif menu1 == 2:
#         break
#     else:
#         print("Pilihan Tidak Ada")


# Membaca seluruh isi file sekaligus
with open("data1.csv", "r") as file:
    konten = file.read()
    print(konten)
# Membaca baris per baris
with open("data1.csv", "r") as file:
    for baris in file:
        print(baris, end='')
