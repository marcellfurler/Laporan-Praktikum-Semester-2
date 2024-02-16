file_pertama="file1.txt"
file_kedua="file2.txt"

buka_file_pertama=open(file_pertama, "r")
buka_file_kedua=open(file_kedua, "r")

gabungan=""
urutan=1

for panggil_pertama in buka_file_pertama:
    gabungan+=panggil_pertama
daftar=gabungan.split("\n")

for panggil_kedua in buka_file_kedua:
    if panggil_kedua.strip() in daftar:
        urutan+=1
        continue
    else:
        print(f"Pada file pertama : \n {urutan}. {daftar[urutan-1]}")
        print(f"Pada file kedua : \n {urutan}. {panggil_kedua}", end="")
        urutan+=1
buka_file_pertama.close()
buka_file_kedua.close()