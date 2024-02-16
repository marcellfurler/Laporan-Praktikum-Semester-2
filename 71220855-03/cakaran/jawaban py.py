# # nomor1

# # inputan

num1=int(input("Masukan Bilangan 1 : "))
num2=int(input("Masukan Bilangan 2 : "))
num3=int(input("Masukan Bilangan 3 : "))
num4=int(input("Masukan Bilangan 4 : "))
num5=int(input("Masukan Bilangan 5 : "))

# proses
terbesar1 = max(num1, num2, num3, num4, num5)

# Menghapus bilangan terbesar pertama dari daftar bilangan
if num1 == terbesar1:
    num1 = float('-inf')
elif num2 == terbesar1:
    num2 = float('-inf')
elif num3 == terbesar1:
    num3 = float('-inf')
elif num4 == terbesar1:
    num4 = float('-inf')
elif num5 == terbesar1:
    num5 = float('-inf')

# Menentukan bilangan terbesar kedua
terbesar2 = max(num1, num2, num3, num4, num5)

# Mencetak bilangan terbesar kedua
print(f"Bilangan terbesar kedua adalah {terbesar2}")
# # proses

# # if bilangan5<=bilangan1 <= bilangan2 :
# #     print(bilangan1)
# # elif bilangan1<=bilangan2<=bilangan3:
# #     print(bilangan2)
# # elif bilangan2<=bilangan3<=bilangan4:
# #     print(bilangan3)
# # elif bilangan3<=bilangan4<=bilangan5:
# #     print(bilangan4)
# # else:
# #     print(bilangan5)


# # proses
# if num1>(num2 or num3 or num4 or num5):
#     print(num1)
# elif num2>(num1 or num3 or num4 or num5):
#     print(num2)
# elif num3>(num2 or num1 or num4 or num5):
#     print(num3)
# elif num4>(num2 or num3 or num1 or num5):
#     print(num4)
# elif num5>(num2 or num3 or num4 or num1):
#     print(num5)


# nomor1
# Menerima input dari pengguna
# bil1 = int(input("Masukkan bilangan pertama: "))
# bil2 = float(input("Masukkan bilangan kedua: "))
# bil3 = float(input("Masukkan bilangan ketiga: "))
# bil4 = float(input("Masukkan bilangan keempat: "))
# bil5 = float(input("Masukkan bilangan kelima: "))








# nomor2

# input

print("Masukan 2 angka dikisaran 10-99")
angkast=int(input("Masukan Angka Pertama : "))
angkand=int(input("Masukan Angka kedua : "))

# proses

# Menerima input dari pengguna
# num1 = int(input("Masukkan bilangan pertama (10..99): "))
# num2 = int(input("Masukkan bilangan kedua (10..99): "))

# Memeriksa apakah dua bilangan memiliki setidaknya satu digit yang sama
if angkast // 10 == angkand % 10 or angkast // 10 == angkand // 10 or angkast % 10 == angkand // 10 or angkast % 10 == angkand % 10:
    print(f"Anda angka yang sama pada {angkast} dan {angkand}.")
else:
    print(f"Tidak ada angka yang sama pada {angkast} dan {angkand}.")




# nomor3
# Menerima input dari pengguna
bil1 = int(input("Masukkan bilangan pertama: "))
bil2 = int(input("Masukkan bilangan kedua: "))
bil3 = int(input("Masukkan bilangan ketiga: "))

# Menghitung penjumlahan pembulatan
penjumlahan_pembulatan = round(bil1) + round(bil2) + round(bil3)

# Mencetak hasil
print("Penjumlahan pembulatan dari ketiga bilangan adalah:", penjumlahan_pembulatan)