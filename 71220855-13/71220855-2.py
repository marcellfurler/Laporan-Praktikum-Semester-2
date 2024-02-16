def kapital(kalimat):
    huruf_kapital=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    if kalimat[0] in huruf_kapital:
        return kalimat[0]
    else:
        return kapital(kalimat[1:])
    
kalimat=input("Masukan Kalimat : ")


print(f"Huruf kapital pada kata/kalimat '{kalimat}' adalah {kapital(kalimat)}")


