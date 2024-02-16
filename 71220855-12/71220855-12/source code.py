# # Nomor 1
# kumpulan_aplikasi = {}
# jumlah_kategori = int(input("Masukkan jumlah kategori: "))

# for _ in range(jumlah_kategori):
#     nama_kategori = input("Masukkan nama Kategori: ")
#     print(f"Masukkan 5 nama aplikasi di kategori {nama_kategori}")

#     aplikasi = []
#     for _ in range(5):
#         nama_aplikasi = input("Nama Aplikasi: ")
#         aplikasi.append(nama_aplikasi)
#     kumpulan_aplikasi[nama_kategori] = aplikasi

# print(kumpulan_aplikasi)

# aplikasi_1 = set()
# aplikasi_more1 = set()

# for aplikasi in kumpulan_aplikasi.values():
#     aplikasi_1.symmetric_difference_update(aplikasi)
#     if not aplikasi_more1:
#         aplikasi_more1.update(aplikasi)
#     else:
#         aplikasi_more1.intersection_update(aplikasi)

# print(f"Aplikasi yang muncul dalam 1 kategori adalah: {aplikasi_1}")

# list_aplikasi=[]

# for application in kumpulan_aplikasi.values():
#     list_aplikasi.append(set(application))

# hasil = set(list_aplikasi[0])
# for aplikasi in list_aplikasi[1:]:
#     hasil.intersection_update(aplikasi)
# print(f"Aplikasi yang muncul >2 di antara kategori adalah: {hasil}")





# # nomor 2
# print("| * | " * 3 + "Kalkulator konversi List-Set-Tuple" + " | * | " * 3)
# print("1. Konversi List to Set\n2. Konversi Set to List\n3. Konversi Tuple to Set\n4. Konversi Set to Tuple")
# inputan=int(input("Masukan angka yang ingin anda masukan : "))

# if inputan==1:
#     panjang_list=int(input("Masukan panjang list : "))
#     kumpulan_list=[]
#     for a in range(panjang_list):
#         inputan_list=input("Masukan : ")
#         kumpulan_list.append(inputan_list)
#     print(f"Data anda saat List : {kumpulan_list}")
#     print(f"Data anda setelah dirubah menjadi Set : {set(kumpulan_list)}")
# elif inputan==2:
#     panjang_set=int(input("Masukan panjang set : "))
#     kumpulan_set=set()
#     for b in range(panjang_set):
#         inputan_set=input("Masukan : ")
#         kumpulan_set.add(inputan_set)
#     print(f"Data anda saat Set : {kumpulan_set}")
#     print(f"Data anda setelah dirubah menjadi List : {list(kumpulan_set)}")
# elif inputan==3:
#     panjang_tuple=int(input("Masukan panjang tuple : "))
#     kumpulan_tuple=()
#     kumpulan_tuple=list(kumpulan_tuple)
#     for c in range(panjang_tuple):
#         inputan_tuple=input("Masukan : ")
#         kumpulan_tuple.append(inputan_tuple)
#     print(f"Data anda saat Tuple : {tuple(kumpulan_tuple)}")
#     print(f"Data anda setelah dirubah menjadi Set : {set(kumpulan_tuple)}")
# elif inputan==4:
#     panjang_set=int(input("Masukan panjang Set : "))
#     kumpulan_set=set()
#     kumpulan_set=list(kumpulan_set)
#     for d in range(panjang_set):
#         inputan_tuple=input("Masukan : ")
#         kumpulan_set.append(inputan_tuple)
#     print(f"Data anda saat Set : {set(kumpulan_set)}")
#     print(f"Data anda setelah dirubah menjadi Tuple : {tuple(kumpulan_set)}")
# else:
#     print("Ada Kesalahan Input!")       







# # Nomor 3
# import os

# inputan_pertama=input("Masukan file 1 : ")
# inputan_kedua=input("Masukan file 2 : ")

# if not os.path.exists(inputan_pertama):
#     print(f"File pertama anda {inputan_pertama} tidak ditemukan!")
#     exit()

# if not os.path.exists(inputan_kedua):
#     print(f"File kedua anda {inputan_kedua} tidak ditemukan!")
#     exit()

# buka_inputan_pertama=open(inputan_pertama, "r")
# buka_inputan_kedua=open(inputan_kedua, "r")



# buka_inputan_pertama=set(buka_inputan_pertama.read().split())
# buka_inputan_kedua=set(buka_inputan_kedua.read().split())

# set_inputan_pertama=set()
# set_inputan_kedua=set()

# for a in buka_inputan_pertama:
#     set_inputan_pertama.add(a.lower())
# for b in buka_inputan_kedua:
#     set_inputan_kedua.add(b.lower())

# gabungan_kata=set_inputan_pertama.union(set_inputan_kedua)

# kata_muncul=set_inputan_pertama.intersection(set_inputan_kedua)

# print("Kata-kata yang muncul pada kedua file : ")
# print(kata_muncul)




for (int i=0; i<arr.length-1; i++)
{}
