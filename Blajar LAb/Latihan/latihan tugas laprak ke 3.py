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

# numero duo

nomor1=int(input("Masukan Angka pertama : "))
nomor2=int(input("Masukan Angka kedua : "))

puluhan_nomor1=nomor1//10 
satuan_nomor1=nomor1%10

puluhan_nomor2=nomor2//10 
satuan_nomor2=nomor2%10

if puluhan_nomor1==puluhan_nomor2 or puluhan_nomor1== satuan_nomor2 or puluhan_nomor2==satuan_nomor1 or puluhan_nomor2==puluhan_nomor1:
    print("Ada yang sama")
else:
    print("Tidak ada yang sama")


# number drie

num1=int(input("Masukan biiangan pertama : "))
num2=int(input("Masukan biiangan kedua : "))
num3=int(input("Masukan biiangan ketiga: "))

# proses
# jumlah=round(num1)+round(num2)+round(num3)

num1=round(num1,-1)
num2=round(num2,-1)
num3=round(num3,-1)
# num4=round(num4,-1)
# num5=round(num5,-1)

jumlah=num1+num2+num3#num4+num5

print(f"Jawabannya adalah : {jumlah}")

# jumlah_num1=float(num1)
# jumlah_num2=float(num2)
# jumlah_num3=float(num3)

