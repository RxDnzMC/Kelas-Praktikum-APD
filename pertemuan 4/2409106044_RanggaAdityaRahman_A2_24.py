#  pertemuan 4 looping
# ulang = 10
# for i in range(ulang):
#     print("Perulangan ke-" + str(i))

# contoh
# for j in range(2,12,2):
#     print("halo")
# print("hai")

# print("menu rumah makan informatika 24: ")
# print("----------------------------------")
# simpan = [12, "udin petot", 14.5, True, 'A']
# for i in simpan:
#     print(i)

# print("menu rumah makan informatika 24: ")
# print("----------------------------------")
# simpan = [12, "udin petot", 14.5, True, 'A']
# for i, menu in enumerate(simpan,start=1):
#     print(f"{i}.{menu}")

# print("menu rumah makan informatika 24: ")
# print("----------------------------------")
# simpan = ["Nasi goreng", "Mie Goreng", "Mie Ayam", "Bakso", "Soto"]
# for i in range(len(simpan)):
#     print(f"{i+1}. {simpan[i]}")

# for i in range(1,4):
#     for j in range (1,4):
#         print(f"{i} x {j} = {i * j}")
#     print()

# cara indexnya adalah i mempunyai 3 nilai dan didalam i ada terdapat j yang memiliki 3 nilai juga
#  jika i dijalankan maka i pertama akan menjalankan juga j tapi j harus dihabiskan
# sampai 3 kali karena j nya memiliki 3 perulangan
# jadi i 1 menjalankan 3 j
#  i 2 menjalankan 3 j
# i 3 menjalankan 3 j
# makanan = ["mie","sop","bakso"]
# minuman = ["es teh","air putih","es jeruk"]

# for i in makanan:
#     for j in minuman:
#         print(f"{i} & {j}")
#     print()


# perulangan while
# while True:
#     print("Hello World")

# jawab = 'ya'
# hitung = 0
# while (jawab == 'ya' or jawab == 'Ya'):
#     hitung += 1
#     jawab = input("Ulang lagi tidak? ")
#     print(f"Total perulangan: {hitung}")

# i = 0
# while i < 5:
#     print(i)
#     i += 1

# break

# i = 0
# while i < 5:
#     print(i)
#     break
#     i += 1

# hitung = 0
# while True:
#     hitung += 1
#     ulang = input("Masih ingin mengulang? ")
#     if ulang == "tidak" or ulang == "Tidak":
#         print("oke kita udahan")
#         break
# print(f"Total perulangan: {hitung}")

# continue

# hitung = 0
# while True:
#     hitung += 1
#     ulang = input("Masih ingin Lanjut? ")
#     if ulang == "y" or ulang == "Y":
#         print("oke kita lanjut")
#         continue

# print(f"Total perulangan: {hitung}")

# print("Daftar bilangan ganjil dari 1-10")
# for i in range(10):
#     if i % 2 == 0:
#         print(f"{i} genap")
#         continue
#     else:
#         print(f"{i} Ganjil")
#         continue

# total = 0
# while True:
#     angka = int(input("Masukkan Angka Positif (Masukkan Nilai Negatif Jika Ingin Berhenti): "))
#     if angka < 0:
#         break
#     total += angka

# print("Jumlah total adalah:", total)


# range_maks = int(input("Range maksimal : "))

# hitung_prima = 0 
# for angka in range(1, range