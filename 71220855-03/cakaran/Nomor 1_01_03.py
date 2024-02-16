# nomor1

num1=int(input("Masukan 1 : "))
num2=int(input("Masukan 2 : "))
num3=int(input("Masukan 3 : "))
num4=int(input("Masukan 4 : "))
num5=int(input("Masukan 5 : "))

# proses
a=[num1,num2,num3,num4,num5]
a.sort()

# output
print(f"Angka terbesar kedua adalah {a[-2]}")