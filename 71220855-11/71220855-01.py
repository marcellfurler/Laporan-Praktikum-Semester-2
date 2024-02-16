def tuple_kumpulan_angka(kumpulan_angka):
    if len(set(kumpulan_angka))==1:
        return True
    else:
        return False

kumpulan_angka=()
banyak_inputan=int(input("Masukan banyak tuple : "))

for banyak_tuple in range(banyak_inputan):
    masukan_tuple=int(input("Masukan Angka : "))
    kumpulan_angka += (masukan_tuple,)

print(kumpulan_angka)
tampilkan=tuple_kumpulan_angka(kumpulan_angka)
print(tampilkan)

# def tuplen(angka):
#     if len(set(angka))==1:
#         return True
#     else:
#         return False
    
# angka=(3,3,3,3,33)

# tampilkan=tuplen(angka)
# print(tampilkan)




# if len(set(kumpulan_angka))==1:
#     print("Semua angka sama!")
# else:
#     print("Ada yang tidak sama")
    
    
    
# if kumpulan_angka[1:(len(kumpulan_angka))] != kumpulan_angka[0]:
#     print("Ada yang tidak sama!")
# else:
#     print("Semua sama!")