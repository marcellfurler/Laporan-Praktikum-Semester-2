def konsonan(kalimat):
    huruf_konsonan=["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y" , "z"]
    if not kalimat:
        return 0
    else:
        for huruf in huruf_konsonan:
            huruf=kalimat[0].lower()
            if huruf in huruf_konsonan:
                return 1+konsonan(kalimat[1:])
            else:
                return konsonan(kalimat[1:])
    
kalimat=input("Masukan Kalimat : ")

print(f"Jumlah huruf konsonan pada kata '{kalimat}' berjumlah : {konsonan(kalimat)} buah")