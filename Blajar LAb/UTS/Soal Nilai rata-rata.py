# Fungsi
def nilai_akhir(quiz1, quiz2, quiz3, quiz4, uts, uas):
    rata_rata_quiz=(quiz1+quiz2+quiz3+quiz4)/4
    if rata_rata_quiz>=60:
        quiz1=quiz1*0.15
        quiz2=quiz2*0.10
        quiz3=quiz3*0.15
        quiz4=quiz4*0.20
        uts=uts*0.20
        uas=uas*0.20
        rata_rata_quiz=(quiz1+quiz2+quiz3+quiz4+uts+uas)
    elif rata_rata_quiz<=60:
        quiz1=quiz1*0.20
        quiz2=quiz2*0.10
        quiz3=quiz3*0.10
        quiz4=quiz4*0.10
        uts=uts*0.20
        uas=uas*0.30
        rata_rata_quiz=(quiz1+quiz2+quiz3+quiz4+uts+uas)
    print(f"Nilai Akhir adalah : {'%.2f'%rata_rata_quiz}")

# Inputan
quiz1=int(input("Masukan Nilai quiz 1 : "))
quiz2=int(input("Masukan Nilai quiz 2 : "))
quiz3=int(input("Masukan Nilai quiz 3 : "))
quiz4=int(input("Masukan Nilai quiz 4 : "))
uts=int(input("Masukan Nilai UTS : "))
uas=int(input("Masukan Nilai UAS : "))

# Pemanggilan Fungsi
nilai_akhir(quiz1, quiz2, quiz3, quiz4, uts, uas)