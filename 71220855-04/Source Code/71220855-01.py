# def cek_angka(a, b, c):
#     if a != b and b != c and c != a:
#         if a + b == c or b + c == a or c + a == b:
#             return True
#     return False


# a = int(input("Masukkan nilai a: "))
# b = int(input("Masukkan nilai b: "))
# c = int(input("Masukkan nilai c: "))


# if cek_angka(a, b, c):
#     print("True")
# else:
#     print("False")




# def penjumlahan(x,y):
#     rumus=x+y
#     return(rumus)

# x=int(input("masukan : "))
# y=int(input("masukan : "))

# print(penjumlahan(x,y))



# def ayam(laki, cewe):
#     x=laki-cewe
#     return(x)

# laki1=input("coc")
# cewe2=input("lambda")


def cek_angka(a, b, c):
    if a!=b and b!=c and a!=c:
        if a+b==c or b+c==a or c+a==b:
            return True
    else:
        return False

a=int(input("Masukan angka pertama : "))
b=int(input("Masukan angka kedua : "))    
c=int(input("Masukan angka ketiga : "))

print(cek_angka(a, b, c))

