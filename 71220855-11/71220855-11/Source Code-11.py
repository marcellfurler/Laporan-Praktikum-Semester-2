##Nomor 1
def tuple_kumpulan_angka(kumpulan_angka):
    if len(set(kumpulan_angka))==1:
        return True
    else:
        return False

kumpulan_angka=()
banyak_inputan=int(input("Masukan banyak tuple : "))

for banyak_tuple in range(banyak_inputan):
    masukan_tuple=int(input("Masukan Angka : "))
    kumpulan_angka += (masukan_tuple,)

print(kumpulan_angka)
tampilkan=tuple_kumpulan_angka(kumpulan_angka)
print(tampilkan)





##Nomor 2
data_diri_Marcell=("Marcell Jureinwi Manuhutu", "71220855", "Sagan, DI Yogyakarta")

nama=print(f"Nama\t: {data_diri_Marcell[0]}")
nim=print(f"NIM\t: {data_diri_Marcell[1]}")
alamat=print(f"Alamat\t: {data_diri_Marcell[2]}")

print()

nim=tuple(data_diri_Marcell[1])
print(f"NIM\t\t: {nim}")

nama=(data_diri_Marcell[0].split())
# print(nama)
nama2=tuple(nama[0])
nama2=nama2[1:]
print(f"Nama Depan\t: {nama2}")

nama=data_diri_Marcell[0].split()
nama=tuple(nama)
nama_terbalik=nama[::-1]
print(f"Nama terbalik\t: {nama_terbalik}")






##Nomor 3
jam=dict()
isi_list=list()

inputan_nama_file=input("Masukan Nama File : ")
inputan_nama_file=open(inputan_nama_file, "r")

for baris in inputan_nama_file:
    weerd = baris.split()
    if len(weerd) < 2 or weerd[0] != 'From':
        continue    
    karakter = weerd[5].find(':')
    uur = weerd[5][:karakter]
    jam[uur] = jam.get(uur, 0) + 1

isi_list = sorted(jam.items())

for key, val in isi_list:
    print(key, val)