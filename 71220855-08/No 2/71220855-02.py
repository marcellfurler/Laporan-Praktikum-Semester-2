# folder_soal=open("D:\\Materi Kuliah\\semester 2\\prak AlPro\\laprak\\71220855-08\\No 2\\pertanyaan.txt")
# folder_jawaban=open("D:\\Materi Kuliah\\semester 2\\prak AlPro\\laprak\\71220855-08\\No 2\\jawaban.txt")

# for baris in folder_soal:
#     print(baris)
#     jawab=input("Jawaban : ")
#     jawab=jawab.lower()
#     if jawab in folder_jawaban.readline():
#         print(f"Jawaban '{jawab}' adalah jawaban yang Benar !")
#     else:
#         print(f"Jawaban '{jawab}' adalah jawaban yang Salah !")

# folder_soal.close()
# folder_jawaban.close()





# yang be
folder_soal=open("D:\\Materi Kuliah\\semester 2\\prak AlPro\\laprak\\71220855-08\\No 2\\pertanyaan.txt")

for baris in folder_soal:
    baris=baris.split("||")
    soal=baris[0]
    jawaban=baris[1]
    print(soal)
    jawab=input("Jawaban : ")
    jawab=jawab.lower()
    if jawab == jawaban.strip():
        print(f"Jawaban '{jawab}' adalah jawaban yang Benar !")
    else:
        print(f"Jawaban '{jawab}' adalah jawaban yang Salah !") 
    

folder_soal.close()

