# # TugasMandiri 2.1

# print("*****SELAMAT DATANG DI BODY MASS INDEX CALCULATOR*****")
# berat=float(input("Masukan Berat Badan Anda (KG) : "))
# tinggi=float(input("Masukan Tinggi Badan Anda (M) : "))
# # tinggiM=tinggi/100


# rumusBMI=berat/tinggi**2


# print(f"Perhitungan BMI anda adalah {rumusBMI}")


# if rumusBMI<18.5:
#     print("Anda mengalami kekurangan berat badan")
# elif rumusBMI<24.9:
#     print("Anda memiliki berat badan Ideal")
# elif rumusBMI<29.9:
#     print("Anda memiliki kelebihan berat badan")
# elif rumusBMI>30.0:
#     print("Anda mengalami Obesitas")



# no 1 yg betul

# soal 1
input
tinggi_badan = int(input("Masukan Tinggi Badan Anda (CM): "))
bmi = float(input("Masukan target BMI: "))

#proses

tinggi_badan = tinggi_badan/100
rumus_bmi = bmi * (tinggi_badan**2)
# mencari_berat_sesuai_target_bmi = int(mencari_berat_sesuai_target_bmi)
#output

print(f"Target yang harus dicapai: {int(rumus_bmi)} KG")


# TugasMandiri 2.2

print("Kalkulator Fungsi")
masukanX=int(input("Masukan Nilai X : "))

rumusfungsi=(2*masukanX**3)+(2*masukanX)+(15/masukanX)

print(f"Hasil fungsinya adalah {int(rumusfungsi)}")




# # Tugas Mandiri 2.3


# pernyataan
waktuminggu=5
pajak_gaji=0.14
baju=0.10
alat_tulis=0.01
sedekah=0.25
sedekah_seribu=0.30

# proses
gaji=int(input("Masukan Gaji yang diinginkan (per jam) : "))
jamker=int(input("Masukan Jam Kerja (per minggu) : "))

rumus_gaji_budi=gaji*(jamker*waktuminggu)
rumus_sesudah_pajak=rumus_gaji_budi-(int(rumus_gaji_budi*pajak_gaji))
rumus_uang_baju=int(rumus_sesudah_pajak*baju)
uang_sisa1=rumus_sesudah_pajak-rumus_uang_baju
rumus_alattulis=int(rumus_sesudah_pajak*alat_tulis)
uang_sisa2=uang_sisa1-rumus_alattulis
rumus_uang_sedekah=int(uang_sisa2*sedekah)
uang_sisa3=uang_sisa2-rumus_uang_sedekah
rumus_anak_yatim=int(rumus_uang_sedekah*sedekah_seribu)
uang_sisa4=uang_sisa3-rumus_anak_yatim
rumus_dhuafa=int(rumus_uang_sedekah-rumus_anak_yatim)




sebelum_pajak=print(f"1. Pendapatan Budi selama Musim Panas adalah Rp.{rumus_gaji_budi}")
sesudah_pajak=print(f"2. Pendapatan Budi selama musim panas setelah membayar pajak adalah Rp.{rumus_sesudah_pajak}")
uang_baju=print(f"3. Uang yang digunakan Budi untuk membeli pakaian dan aksesoris adalah Rp.{rumus_uang_baju}")
uang_alattulis=print(f"4. Uang yang digunakan Budi untuk membeli Alat Tulis adalah Rp.{rumus_alattulis}")
uang_sedekah=print(f"5. Uang yang akan disedekahkan Budi adalah Rp.{rumus_uang_sedekah}")
uang_anak_yatim=print(f"6. Uang yang diterima anak yatim adalah RP.{rumus_anak_yatim}")
uang_kaum_dhafa=print(f"7. Uang yang diterima kaum dhuafa adalah Rp.{rumus_dhuafa}")








# # perbaikan no 3

# #pernyataan
# waktuminggu=5
# pajak_gaji=0.14
# baju=0.10
# alat_tulis=0.01
# sedekah=0.25
# sedekah_seribu=0.30
# #input

# gaji=int(input("Masukan Gaji yang diinginkan (per jam) : "))
# jamker=int(input("Masukan Jam Kerja (per minggu) : "))


# #proses

# rumus_gaji_budi = (jamker*5)*gaji
# rumus_sesudah_pajak = rumus_gaji_budi-(rumus_gaji_budi*pajak_gaji)
# rumus_uang_baju = rumus_gaji_budi - (rumus_gaji_budi*gaji)
# rumus_alat_tulis = rumus_uang_baju - (rumus_uang_baju*alat_tulis)
# rumus_sedekah = rumus_alat_tulis*sedekah
# anak_yatim = (rumus_sedekah/1000) * sedekah_seribu * 1000
# rumus_dhuafa = rumus_sedekah - anak_yatim


# #output

# sebelum_pajak=print(f"1. Pendapatan Budi selama Musim Panas adalah Rp.{rumus_gaji_budi}")
# sesudah_pajak=print(f"2. Pendapatan Budi selama musim panas setelah membayar pajak adalah Rp.{rumus_sesudah_pajak}")
# uang_baju=print(f"3. Uang yang digunakan Budi untuk membeli pakaian dan aksesoris adalah Rp.{rumus_uang_baju}")
# uang_alattulis=print(f"4. Uang yang digunakan Budi untuk membeli Alat Tulis adalah Rp.{rumus_alat_tulis}")
# uang_sedekah=print(f"5. Uang yang akan disedekahkan Budi adalah Rp.{rumus_sedekah}")
# uang_anak_yatim=print(f"6. Uang yang diterima anak yatim adalah RP.{anak_yatim}")
# uang_kaum_dhafa=print(f"7. Uang yang diterima kaum dhuafa adalah Rp.{rumus_dhuafa}")
# 
# 
# 
# # pendapatan_kotor = (jumlah_jamm_kerja*5)*masukan_gaji
# pendapatan_bersih = pendapatan_kotor-(pendapatan_kotor*14/100)
# setelah_membeli_aksesoris = pendapatan_kotor - (pendapatan_kotor*10/100)
# setelah_membeli_alat_tulis = setelah_membeli_aksesoris - (setelah_membeli_aksesoris*1/100)
# sisa_untuk_disedekahkan = setelah_membeli_alat_tulis*25/100
# jumlah_yang_diterima_anak_yatim = (sisa_untuk_disedekahkan/1000) * 30/100 * 1000
# jumlah_yang_diterima_kaum_dhuafa = sisa_untuk_disedekahkan - jumlah_yang_diterima_anak_yatim

# rumus_gaji_budi = (jamker*5)*gaji
# rumus_sesudah_pajak = rumus_gaji_budi-(rumus_gaji_budi*14/100)
# rumus_uang_baju = rumus_gaji_budi - (rumus_gaji_budi*10/100)
# rumus_alat_tulis = rumus_uang_baju - (rumus_uang_baju*1/100)
# rumus_sedekah = rumus_alat_tulis*25/100
# anak_yatim = (rumus_sedekah/1000) * 30/100 * 1000
# rumus_dhuafa = rumus_sedekah - anak_yatim