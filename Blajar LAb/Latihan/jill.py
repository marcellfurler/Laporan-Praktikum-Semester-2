# # soal 1
# #input
# masukan_tinggi = int(input("Masukan Tinggi Badan dalam satuan CM: "))
# masukan_target_bmi = float(input("Masukan target BMI: "))

# #proses

# masukan_tinggi = masukan_tinggi/100
# mencari_berat_sesuai_target_bmi = masukan_target_bmi * (masukan_tinggi**2)
# mencari_berat_sesuai_target_bmi = int(mencari_berat_sesuai_target_bmi)
# #output

# print("Target yang harus dicapai: Kg ", mencari_berat_sesuai_target_bmi)

# # soal 2

# #input

# x = int(input("Masukan Nilai x = "))

# # proses

# f = (2*(x**3)+(2*x)+(15/x))

# # output

# print("Hasilnya Adalah: ", int(f))

# # soal 3
#input

masukan_gaji = int(input("Masukan Gaji Per jam yang Anda inginkan: "))
jumlah_jamm_kerja = int(input("Jumlah jam kerja yang akan dilakukan dalam 1 minggu: "))

#proses

pendapatan_kotor = (jumlah_jamm_kerja*5)*masukan_gaji
pendapatan_bersih = pendapatan_kotor-(pendapatan_kotor*14/100)
setelah_membeli_aksesoris = pendapatan_kotor - (pendapatan_kotor*10/100)
setelah_membeli_alat_tulis = setelah_membeli_aksesoris - (setelah_membeli_aksesoris*1/100)
sisa_untuk_disedekahkan = setelah_membeli_alat_tulis*25/100
jumlah_yang_diterima_anak_yatim = (sisa_untuk_disedekahkan/1000) * 30/100 * 1000
jumlah_yang_diterima_kaum_dhuafa = sisa_untuk_disedekahkan - jumlah_yang_diterima_anak_yatim

#output

print(f"Pendapatan Budi selama libur musim panas sebelum melakukan pembayaran pajak\t: Rp.{pendapatan_kotor} " )
print(f"Pendapatan Budi selama libur musim panas setelah melakukan pembayaran pajak\t: Rp.{pendapatan_bersih} " )
print(f"Jumlah uang yang akan Budi habiskan untuk membeli pakaian dan aksesoris\t\t: Rp.{setelah_membeli_aksesoris} " )
print(f"Jumlah uang yang akan Budi habiskan untuk membeli alat tulis\t\t\t: Rp.{setelah_membeli_alat_tulis} " )
print(f"Jumlah uang yang akan Budi sedekahkan\t\t: Rp.{sisa_untuk_disedekahkan} " )
print(f"Jumlah uang yang akan diterima anak yatim\t: Rp.{jumlah_yang_diterima_anak_yatim} " )
print(f"Jumlah uang yang akan diterima kaum dhuafa\t: Rp.{jumlah_yang_diterima_kaum_dhuafa} " )