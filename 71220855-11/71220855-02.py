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

# nama=tuple(data_diri_Marcell[0])
# nama2=tuple(nama[1:7])
# print(f"Nama Depan\t: {nama2}")



