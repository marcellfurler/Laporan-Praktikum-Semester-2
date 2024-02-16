
# def kata_berulang(masukan):
#     kata_dihitung=input("Masukan Kata yang ingin dihitung : ")
#     proses=masukan.count(kata_dihitung)
#     print(f'Kata "{kata_dihitung}" berjumlah {proses} buah di dalam kalimat "{masukan}"')

# masukan=input("Masukan Sebuah Kalimat : ")

# kata_berulang(masukan)




def spasi(kalimat):
    kalimat=kalimat.strip()
    while "" in kalimat:
        kalimat=kalimat.replace("a",4)
    return kalimat

kalimat2=input("masukan kalimat : ")

perbaikan=spasi(kalimat2)

print(kalimat2)

# spasi(kalimat)
