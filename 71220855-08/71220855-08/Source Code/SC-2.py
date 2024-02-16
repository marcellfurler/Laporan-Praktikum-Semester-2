folder_soal=open("pertanyaan.txt")

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