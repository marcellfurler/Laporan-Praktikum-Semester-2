# Fungsi
def hitung_kaki(sapi, ayam, anjing, angsa):
    sapi=sapi*4
    ayam=ayam*2
    anjing=anjing*4
    angsa=angsa*2
    kaki_dua=ayam+angsa
    kaki_empat=sapi+anjing
    print(f"Total jumlah kaki dikategori hewan berkaki dua adalah : {kaki_dua}")
    print(f"Total jumlah kaki dikategori hewan berkaki empat adalah : {kaki_empat}")
    if kaki_dua>kaki_empat:
        print("Kategori hewan berkaki dua lebih banyak")
    elif kaki_dua<kaki_empat:
        print("Kategori hewan berkaki empat lebih banyak")
    else:
        print("Keduanya sama banyak")
    

# Inputan
sapi=int(input("Masukan Jumlah Sapi : "))
ayam=int(input("Masukan Jumlah ayam : "))
anjing=int(input("Masukan Jumlah anjing : "))
angsa=int(input("Masukan Jumlah angsa : "))

hitung_kaki(sapi, ayam, anjing, angsa)