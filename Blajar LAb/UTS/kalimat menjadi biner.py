kalimat=input("Masukan sebuah kalimat/kata : ")
vokal="aiueo"
hasil=""
for karakter in kalimat:
    if karakter in vokal:
        hasil=hasil+"0"
    else:
        hasil=hasil+"1"
print(hasil)