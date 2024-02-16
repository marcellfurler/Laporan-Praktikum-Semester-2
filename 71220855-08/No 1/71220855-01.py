# file_pertama=input("Masukan File Pertama : ")
# file_kedua=input("Masukan File Kedua : ")

# buka_file_pertama=open(file_pertama, "r")
# buka_file_kedua=open(file_kedua, "r")

# print(buka_file_pertama.readline())
# print(buka_file_kedua.readline())

# for i, line in enumerate(buka_file_pertama):
#     if line!=file_kedua[i]:
#         print(f"Baris {i+1} pada file {file_pertama} : {line}")
#         print(f"Baris {i+1} pada file {file_kedua} : {file_kedua[i]}")




file_pertama="D:\\Materi Kuliah\\semester 2\\prak AlPro\\laprak\\71220855-08\\No 1\\file1.txt"
file_kedua="D:\\Materi Kuliah\\semester 2\\prak AlPro\\laprak\\71220855-08\\No 1\\file2.txt"

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



# file_pertama=open("D:\\Materi Kuliah\\semester 2\\prak AlPro\\laprak\\71220855-08\\No 1\\file1.txt")
# file_kedua=open("D:\\Materi Kuliah\\semester 2\\prak AlPro\\laprak\\71220855-08\\No 1\\file2.txt")

# buka_file1=print(file_pertama.readline())
# buka_file2=print(file_kedua.readline())


# for baris in file_pertama:
#     if baris != buka_file2:
#         print("tidak sama")
#     else:
#        print("sama")
