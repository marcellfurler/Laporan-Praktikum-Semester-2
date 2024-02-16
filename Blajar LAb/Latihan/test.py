# for i in range(1,15):
#     print(i)

# for i in range(1501, 20000):
#     print(i)

# for i in range(1500, 20001, 50):
#     print(i)

# for i in range(15, 0, -1):
#     print(i)



# for i in range(15, 0, -1):
#     if i%2==0:
#         print(f"{i} genap")
#     else:
#         print(f"{i}ganjil")



# # print("ganjil")


# for i in range(1, 101):
#     print("marcell")

# end="\t"


# def fibo(batas):
#     bil1 = 1
#     bil2 = 1
# # tampilkan dua suku fibonacci pertama
#     if bil1 < batas:
#         print(bil1, end='\t')
#         print(bil2, end='\t')
# # suku-suku berikutnya dari bil1 + bil2
#     suku_baru = bil1 + bil2
#     while suku_baru < batas:
#         print(suku_baru, end='\t')
# # geser bil1 dan bil2
#         bil1 = bil2
#         bil2 = suku_baru
# # hitung lagi suku berikutnya
#         suku_baru = bil1 + bil2
# batas = int(input('Masukkan batas dari deret fibonacci: '))
# fibo(batas)




# def prime(number):
#     pembagi=0
#     for i in range(1,number+1):
#         if number%i==0: 
#             pembagi+=1
#     if pembagi==2:
#         return True
#     else:
#         return False
        
# number=int(input("Masukan angka : "))
# hasil=prime(number)
# if hasil:
#     print("prime")
# else:
#     print("primeless")






# def prime(number):
#     pembagi=0
#     for i in range(1,number+1):
#         if number%i==0: 
#             pembagi+=1
#     if pembagi==2:
#         return True
#     else:
#         return False
    
# bawah=int(input("Masukan batas bawah : "))
# atas=int(input("Masukan batas atas : "))

# for i in range(bawah, atas+1):
#     hasil=prime(i)
#     if hasil:
#         print(i)





import random

def check_angka(bawah, atas):
    angka_kom=random.randrange(bawah, atas)
    return angka_kom

angka_kom=check_angka(0, 20)
tebakan=False

langkah=6
level=int(input("masukan level mu ferguso 1/2/3 : "))
if level==1:
    print("level easy ygy (1-100)")
    angka_kom=check_angka(0,100)
    langkah=6
elif level==2:
    print("level medium ygy (101-500)")
    angka_kom=check_angka(101,500)
elif level==3:
    print("level hard ygy (501-1000)")
    angka_kom=check_angka(501,1000)
hasil=False

while tebakan==False:
    if langkah==0:
        break
    tebakkanmu=int(input(f"Masukan tebakan anda : {angka_kom}"))
    langkah=langkah-1
    if tebakkanmu==angka_kom:
        tebakan=True
        hasil=True
        break
    else:
        if tebakkanmu > angka_kom:
            print("kegedean")
        else:
            print("kekecilan")
        print("anda salah, coba lagi")


if hasil==True:
    print(f"selamat, anda menang dari komputer. sisa nyawa anda {langkah}")
else:
    print("Kalah, anda kurang beruntung")








# def cetak(a,b):

# cetak(5,9)









