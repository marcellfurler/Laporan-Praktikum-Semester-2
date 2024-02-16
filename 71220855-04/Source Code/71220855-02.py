def cek_digit_belakang(a, b, c):
    a=a%10
    b=b%10
    c=c%10
    if a==b or a==c or b==a or c==a:
        return True
    else:  
        return False

a=int(input("Masukan angka pertama : "))
b=int(input("Masukan angka kedua : "))
c=int(input("Masukan angka ketiga : "))

print(cek_digit_belakang(a, b, c))