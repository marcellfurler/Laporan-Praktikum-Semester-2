# def hapus_spasi(kalimat):
#     kalimat = kalimat.strip()
#     while "  " in kalimat:
#         kalimat = kalimat.replace("  ", " ")
#     return kalimat


# kalimat_inputan = input("Masukan Kalimat : ")

# kalimat_perbaikan= hapus_spasi(kalimat_inputan)

# print(kalimat_perbaikan)


def hapus_spasi(kalimat):
    kalimat = kalimat.strip()
    while "  " in kalimat:
        kalimat = kalimat.replace("  ", " ")
    return kalimat


kalimat_inputan = input("Masukan Kalimat : ")

kalimat_perbaikan= hapus_spasi(kalimat_inputan)

print(kalimat_perbaikan)