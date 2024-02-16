# # nomor 1

# def perkalian(pengali, angka_dikali):
#     hasil=0
#     print(f"{pengali} x {angka_dikali} = ", end="")
#     for i in range(1, pengali+1):
#         if i==pengali:
#             print(f"{angka_dikali} = ", end="")
#         else:
#             print(f"{angka_dikali} + ", end="")
#         hasil=hasil+angka_dikali
#     return(f"{hasil}")

# pengali=int(input("Masukan pengali : "))
# angka_dikali=int(input("Masukan angka dikali : "))
    
# print(perkalian(pengali,angka_dikali))



# # # nomor 2
# bawah=int(input("Masukan batas bawah : "))
# atas=int(input("Masukan batas atas : "))

# if bawah>atas:
#     for i in range(bawah, atas-1, -1):
#         if i%2==1:
#             if i==atas or i==atas +1: 
#                 print(i)
#             else:
#                 print(i, end=", ")
# else:
#     for i in range(bawah, atas + 1):
#         if i%2==1:
#             if i==atas or i==atas-1:
#                 print(i)
#             else:
#                 print(i, end=", ")






# nomor 3
# matkul=int(input("Masukan jumlah matkul : "))
# kum_nilai=[]
# jum_nilai=0

# for i in range(matkul):
#     nilai=(input(f"Masukan Matkul {i+1} : "))
#     kum_nilai.append(nilai)
# for i in range(matkul):
#     if kum_nilai[i] == "A" :
#         jum_nilai=jum_nilai+4
#     elif kum_nilai[i] == "B":
#         jum_nilai=jum_nilai+3
#     elif kum_nilai[i] == "C":
#         jum_nilai=jum_nilai+2
#     elif kum_nilai[i] == "D":
#         jum_nilai=jum_nilai+1

# ips=float(jum_nilai*3/matkul/3)

# print(f"IPS Kamu adalah : {ips:.2f}")





# # cobA

# matkul=int(input("Masukan jumlah matkul : "))
# kum_nilai=[]
# jum_nilai=0

# for i in range(matkul):
#     nilai=(input(f"Masukan Matkul {i+1} : "))
#     kum_nilai.append(nilai)
# for i in range(matkul):
#     if kum_nilai[i] == "A":
#         jum_nilai=jum_nilai+4
#     elif kum_nilai[i] == "B":
#         jum_nilai=jum_nilai+3
#     elif kum_nilai[i] == "C":
#         jum_nilai=jum_nilai+2
#     elif kum_nilai[i] == "D":
#         jum_nilai=jum_nilai+1

# print("IPSnya adalah : ", float((((jum_nilai*3)/matkul/3))))


print(float(16*3/6/3))