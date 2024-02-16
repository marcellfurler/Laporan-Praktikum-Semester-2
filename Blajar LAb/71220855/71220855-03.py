hari_kerja=int(input("Masukan Hari kerja : "))
bruto=hari_kerja*8*10000
pajak=bruto*0.05
upah=bruto-pajak

print("Upah karyawan sebelum pajak : Rp.",bruto)
print("Upah yang harus dibayar : Rp.",pajak)
print("Penghasilan bersih yang diterima : Rp.",upah)