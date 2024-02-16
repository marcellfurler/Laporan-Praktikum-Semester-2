# persegi=lambda sisi :sisi**2

# sisi=int(input("MAsukan sisi : "))
# print persegi

# benar
# fahrenheit=lambda C_F:round(1.8*C_F+32)
# reamur=lambda C_R:round(0.8*C_R)


# C_F=int(input("Masukan suhu dalam Celcius : "))
# C_R=int(input("Masukan suhu dalam Celcius : "))

# print(f"Suhu {C_F} derajat Celcius sama dengan {str(fahrenheit(C_F))} derajat fahrenheit")
# print(f"Suhu {C_F} derajat Celcius sama dengan {str(reamur(C_R))} derajat reamur")


# print(fahrenheit(100))
# print(reamur(0))
# print(fahrenheit(0))



# bentuk lain

fahrenheit=lambda C_F:round(1.8*C_F+32)
reamur=lambda C_R:round(0.8*C_R)

print("1. Fahrenheit")
print("2. Reamur")
pilihan=int(input("Masukan pilihan anda : "))

if pilihan==1:
    print("Anda memilih Konversi suhu dari Celcius ke Fahrenheit")
    C_F=int(input("Masukan suhu dalam Celcius : "))
    print(f"Suhu {C_F} derajat Celcius sama dengan {fahrenheit(C_F)} derajat fahrenheit")
elif pilihan==2:
    print("Anda memilih Konversi suhu dari Celcius ke Reamur")
    C_R=int(input("Masukan suhu dalam Celcius : "))
    print(f"Suhu {C_R} derajat Celcius sama dengan {reamur(C_R)} derajat reamur")
else:
    print("Ada kesalahan input")