def cek_kalimat(kalimat):
    kata=kalimat.split()
    pendek = min(kata, key=len)
    panjang = max(kata, key=len)
    print(f"Kata terpendek adalah '{pendek}' dan kata terpanjang adalah '{panjang}'")
       

kalimat=input("Masukan kalimat : ")

cek_kalimat(kalimat)



