jam_awal=int(input("Masukan jam awal : "))
menit_awal=int(input("Masukan menit awal : "))

jam_akhir=int(input("Masukan Jam akhit : "))
menit_akhir=int(input("Masukan menit akhir : "))

jam1=jam_awal*60+menit_awal
jam2=jam_akhir*60+menit_akhir

if jam1<=jam2:
    waktu=jam2-jam1
    print("Selisihnya adalah",waktu,"menit")