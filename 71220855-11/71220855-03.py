# jam=dict()
# isi_list=list()

# inputan_nama_file=input("Masukan Nama File : ")
# inputan_nama_file=open(inputan_nama_file, "r")

# for baris in inputan_nama_file:
#     kata = baris.split()
#     if len(kata) < 2 or kata[0] != 'From':
#         continue
#     col_pos = kata[5].find(':')
#     uur = kata[5][:col_pos]
#     if uur not in jam:
#         jam[uur]=1
#     else:
#         jam[uur]+=1

# for key, val in list(jam.items()):
#     isi_list.append((key,val))

# isi_list.sort()

# for key, val in isi_list:
#     print(key,val)



# cara 2

# jam=dict()
# isi_list=list()

# inputan_nama_file=input("Masukan Nama File : ")
# inputan_nama_file=open(inputan_nama_file, "r")

# for baris in inputan_nama_file:
#     weerd = baris.split()
#     if len(weerd) < 2 or weerd[0] != 'From':
#         continue    
#     karakter = weerd[5].find(':')
#     uur = weerd[5][:karakter]
#     jam[uur] = jam.get(uur, 0) + 1

# isi_list = sorted(jam.items())

# for key, val in isi_list:
#     print(key, val)

