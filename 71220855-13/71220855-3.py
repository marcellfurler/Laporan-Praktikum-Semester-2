def hapus_karakter(kalimat):
    for objek in kalimat:
        if len(kalimat) <2:
            return kalimat
        elif kalimat[0] == kalimat[1]:
            return hapus_karakter(kalimat[1:])
        else:
            return kalimat[0] + hapus_karakter(kalimat[1:])
    

kalimat=input("Masukan sebuah objek : ")
print(hapus_karakter(kalimat))