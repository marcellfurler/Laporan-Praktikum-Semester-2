# # No 1

# def konsonan(kalimat):
#     huruf_konsonan=["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y" , "z"]
#     if not kalimat:
#         return 0
#     else:
#         for huruf in huruf_konsonan:
#             huruf=kalimat[0].lower()
#             if huruf in huruf_konsonan:
#                 return 1+konsonan(kalimat[1:])
#             else:
#                 return konsonan(kalimat[1:])
    
# kalimat=input("Masukan Kalimat : ")

# print(f"Jumlah huruf konsonan pada kata '{kalimat}' berjumlah : {konsonan(kalimat)} buah")




# # No 2

# def kapital(kalimat):
#     huruf_kapital=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
#     if kalimat[0] in huruf_kapital:
#         return kalimat[0]
#     else:
#         return kapital(kalimat[1:])
    
# kalimat=input("Masukan Kalimat : ")

# print(f"Huruf kapital pada kata/kalimat '{kalimat}' adalah {kapital(kalimat)}")




# # No 3

# def hapus_karakter(kalimat):
#     for objek in kalimat:
#         if len(kalimat) <2:
#             return kalimat
#         elif kalimat[0] == kalimat[1]:
#             return hapus_karakter(kalimat[1:])
#         else:
#             return kalimat[0] + hapus_karakter(kalimat[1:])
    

# kalimat=input("Masukan sebuah objek : ")
# print(hapus_karakter(kalimat))



def konsonan_rekursif(string):
    contoh = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    if len(string) == 0:
        return 0
    elif string[0] in contoh:
        return 1 + konsonan_rekursif(string[1:])
    else:
        return konsonan_rekursif(string[1:])

def konsonan_iterative(string):
    contoh = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    hasil = 0
    for i in string:
        if i in contoh:
            hasil = hasil + 1
    return hasil

string = input('Masukkan string: ')
hasil_rekursif = konsonan_rekursif(string)
hasil_iterative = konsonan_iterative(string)
print(f'Jumlah konsonan iteratif adalah {hasil_iterative}')
print(f'Jumlah konsonan rekursif adalah {hasil_rekursif}')