# nama = ["celio","shandy","farel","ghazali","vito"]
# print(nama[0])

# nama = ["celio","shandy","farel","ghazali","vito"]
# print("senelum: ")
# print(nama)
# print("")
# print("sesudah: ")
# nama.append("afrizal")
# print("nama")


# nama = ["celio","shandy","farel","ghazali","vito"]
# print("senelum: ")
# print(nama)
# print("")
# print("sesudah: ")
# nama.insert(2,"afrizal")
# print(nama)


# nama = ["celio",
#         "shandy",
#         "farel",
#         "ghazali",
#         "vito",
#         "yuyun",
#         "andri",
#         "rizal",
#         "adi",
#         "ifnu"
# ]

# matkul = ["APD","APL","BASDAT","STRUKDAT","WEB","JARKOM"]
# data = nama+matkul

# print("senelum: ")
# print(nama)
# print("")
# print("sesudah: ")
# nama.insert(2,"afrizal")
# print(nama)
# nama[4]= "fufufafa"
# del nama[2]
# hapus = nama.pop(2)
# print(nama)
# print(hapus)
# print(nama[1:9:2])
# print(data)
# print(data*3)



# data = ["farel","celio",[1,2,["hai",23,2.3,True]]]

# # print(data[2][2][::-1])
# print(data[::-1])

# matkul = ([1,2,3],[4,5,6],[7,8,9])
# print(matkul[4][3][1])

# for i in matkul:
#     for j in i:
#         print(j)

# nama = ('farrel','vito','shandy','rijal')
# print(nama)


# ##mendeklarasikan tuple
# mahasiswa = (69, "Informatika", "2209106044", "Aldy septian ")
# # lalu kita unpacking
# absen, prodi, nim, nama = mahasiswa
# # maka ketiga variabel tersebut akan berisi data dari tuple mahasiswa
# # menampilkan variabel
# print(absen)
# print(prodi)
# print(nim)
# print(nama)



print(
"""
======================
  DATA MAHASISWA A24
======================
1. TAMBAH DATA
2. TAMPILKAN DATA
3. UBAH DATA
4. HAPUS DATA
5. KELUAR
======================
"""
)
data_mahasiswa = []
while True:
    pilih = int(input("PILIH : "))
    if pilih == 1:
        nama = input("NAMA :")
        nim = input("NIM : ")
        kelas = input("KELAS : ")
        data_mahasiswa.append([nama,nim,kelas])

    elif pilih == 2:
        for data in data_mahasiswa:
            for i in range(len(data)):
                print(f"Data Mahasiswa ke-{i+1} NAMA : {data_mahasiswa[i][0]} NIM : {data_mahasiswa[i][1]} KELAS : {data_mahasiswa[i][2]}")

    elif pilih == 3:
        nama_lama = input("Nama Baru : ")
        for i in range(len(data_mahasiswa)):
            if data_mahasiswa[i][0] == nama_lama:
                nama_baru = input("Nama : ")
                nim_baru = input("NIM : ")
                kelas_baru = input("KELAS : ")
                data_mahasiswa[i][0] = nama_baru
                data_mahasiswa[i][1] = nim_baru
                data_mahasiswa[i][2] = kelas_baru

    elif pilih == 4:
        nama_lama = input("Nama Baru")
        for i in range(len(data_mahasiswa)):
            if data_mahasiswa[i][0] == nama_lama:
                del data_mahasiswa[i]
                
    elif pilih == 5:
        print("Terimakasih Telah Mengakses Data Mahasiswa")

    else:
        print("Anda Salah Input")