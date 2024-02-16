# nama="marcell"
# print(nama)
# type(nama)





# # alay badaki translator

def kalimat_spok(kalimat):
    #daftar huruf alay
    normal="aAiIeEsSgGoOBb"
    upnormal="44113355990086"
    hasil=""
    for karakter in kalimat:
        if karakter in normal:
            #direplace
            ind3x=normal.index(karakter)
            hasil=hasil+upnormal[ind3x]
        else:
            hasil=hasil+karakter
    return hasil 


kalimat=input("masukan kalimat : ")

hasil=kalimat_spok(kalimat)

print(hasil)

kalimat="marcell furler"
kalimat[0:6]












# # hitung huruf vocal dikalimat

# def hitung_vocal(kalimat):
#     vocal="aAiIuUeEoO"
#     jumlah=0
#     for karakter in kalimat:
#         if karakter in vocal:
#             jumlah+=1
#     return jumlah
# def hitung_unvocal(kalimat):
#     vocal="aAiIuUeEoO"
#     jumlah=0
#     for karakter in kalimat:
#         if karakter not in vocal and karakter.isalpha():
#             jumlah+=1
#     return jumlah 
# def hitung_digit(kalimat):
#     digit="0123456789"
#     jumlah=0
#     for karakter in kalimat:
#         if karakter in digit:
#             jumlah+=1
#     return jumlah
# def tanda_baca(kalimat):
#     taba=".,?!@#$%^&*()_+-={}[]:;/"
#     jumlah=0
#     for karakter in kalimat:
#         if karakter in taba:
#             jumlah+=1
#     return jumlah
# def tanda_whitespace(kalimat):
#     jumlah=0
#     for karakter in kalimat:
#         if karakter.isspace():
#             jumlah+1
#     return jumlah


# kalimat=input("masukan kalimat : ")

# hasil=hitung_vocal(kalimat)
# hasil2=hitung_unvocal(kalimat)
# hasil3=hitung_digit(kalimat)
# hasil4=tanda_baca(kalimat)
# hasil5=tanda_whitespace(kalimat)

# print(f"jumlah huruf vocal adalah {hasil} biji")
# print(f"jumlah huruf unvocal adalah {hasil2} biji")
# print(f"jumlah huruf dalam kalimat adalah {hasil3} biji")
# print(f"jumlah tanda baca dalam kalimat adalah {hasil4} biji")
# print(f"jumlah tanda whitespace dalam kalimat adalah {hasil5} biji")


















# tanggal="2005-06-05"
# hasil=tanggal.split()
# print(hasil)


# def ubah_tanggal(tanggal):
#     return tanggal[-2:] + "-" + tanggal[5:7] + "-" + tanggal[:4]

# tanggal="2005-06-05"

# hasil=ubah_tanggal(tanggal)

# print(f"tanggal berdasarkan dd-mm-yyyy adalah {hasil}")
















# palindrome


def palindrome(kalimat):
    kalimat=kalimat.lower()
    hasil=""
    for karakter in kalimat:
        if karakter.isalpha():
            hasil=hasil+karakter
    balik=kalimat[::-1] #mulai dari belakang, tapi langkahnya mundur (kaya reverse)
    if kalimat==balik:
        print("palindrome!")
    else:
        print("unpalindrome!")




kalimat=input("masukan kalimat : ")
palindrome(kalimat)



