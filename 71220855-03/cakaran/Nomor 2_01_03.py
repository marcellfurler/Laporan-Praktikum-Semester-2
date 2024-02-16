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