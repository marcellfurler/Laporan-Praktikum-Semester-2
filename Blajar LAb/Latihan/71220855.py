# nomor 1

def perkalian(x, y):
    hasil=0
    print(f"{x} x {y} = ", end="")
    for i in range(1, x+1):
        if i==x:
            print(f"{y} = ", end="")
        else:
            print(f"{y} + ", end="")
        hasil=hasil+y
    print(f"{hasil}")
    
print(perkalian(6,5))



# nomor 2
batas_bawah=int(input("Masukan batas bawah : "))
batas_atas=int(input("Masukan batas atas : "))

if batas_bawah>batas_atas:
    for i in range(batas_bawah, batas_atas-1, -1):
        if i%2==1:
            if i==batas_atas or i==batas_atas +1: 
                print(i)
            else:
                print(i, end=", ")

    # batas_atas, batas_bawah = batas_bawah, batas_atas

else:
    for i in range(batas_bawah, batas_atas + 1):
        if i%2==1:
            if i==batas_atas or i==batas_atas-1:
                print(i)
            else:
                print(i, end=", ")






# nomor 3
matkul=int(input("Masukan jumlah matkul : "))
kum_nilai=[]
jum_nilai=0

for i in range(matkul):
    nilai=(input(f"Masukan Matkul {i+1} :"))
    kum_nilai.append(nilai)
for i in range(matkul):
    if kum_nilai[i] == "A":
        jum_nilai=jum_nilai+4
    elif kum_nilai[i] == "B":
        jum_nilai=jum_nilai+3
    elif kum_nilai[i] == "C":
        jum_nilai=jum_nilai+2
    elif kum_nilai[i] == "D":
        jum_nilai=jum_nilai+1

print(f"IPSnya adalah : {float((((jum_nilai*3)/matkul/3)))}")
