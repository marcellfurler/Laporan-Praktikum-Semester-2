def pangkat_table(angka, pangkat):
    hasil=dict()
    for angka in range(1, angka+1):
        hasil[angka]=angka**pangkat
    return hasil
    
angka=int(input("Masukan angka : "))
pangkat=int(input("Masukan pangkat : "))
hasil=pangkat_table(angka,pangkat)
print(hasil)