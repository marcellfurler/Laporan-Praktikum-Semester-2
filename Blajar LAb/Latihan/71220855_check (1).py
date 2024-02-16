# # n=int(input("Masukan n : "))

# # riumus=n*"#"

# # print(riumus)







# #gambar segitigaan
# # pak Yuan
# n=int(input("Masukan n : "))

# # horizone
# def pagar_rata(n):
#     for i in range(n):
#         print("*")
#     print()
        
# # verticale
# def pagar_naik(n):
#     for i in range(n):
#         print("*", end="")
#     print()
        
# pagar_rata(n)
# pagar_naik(n)








# #urutan x*x
# def persegi(a):
#     for x in range(a):
#         for y in range(a):
#             print("*", end="")
#         print()
    
        
# a=int(input("Masukan a : "))


# persegi(a)








# #segitiga 90 derajat

#kiri to kanan
def segitiga_90(y):
    for segitiga in range(1, y+1):
        for urutan in range(1, segitiga+1):
            print("x", end="")
        print()
        
        
# knan to kiri
def segitiga_kiri(y):
    for segitiga in range(1, y+1):
        for urutan in range(1, segitiga+1):
            print("*", end="")
        print()
        
        
        
        
# kiri to kanan
def segitiga_kanan(y):
    for baris in range(1, y+1):
        space=y-baris
        pagar=baris
        for kolom_spasi in range(space):
            print(" ", end="")
        for kolom_spasi in range(pagar):
            print("*", end="")
        print()            
    
    
y=int(input("Masukan y : "))


segitiga_kiri(y)
segitiga_kanan(y)








# bentuk bolong

# def segi_blubang(z):
#     for kolom in range(z):
#         print("*", end="")
#     print()
#     for baris in range(z-2):
#         space=z-2
#         print("*", end="")  
#         for kolom in range(space):
#             print(" ", end="")
#         print("*") 
#     for kolom in range(z):
#         print("*", end="")
#     print()
    
# z=int(input("masukan Z : "))   




# segi_blubang(z)











# SILANG X

# def huruf_X(l):
#     for baris in range(l):
#         for kolom in range(l):
#             if baris==kolom:
#                 print("*", end="")
#             elif baris+kolom==l-1:
#                 print("*", end="")
#             else:
#                 print(" ", end="") 
#         print()  
                
# l=int(input("Masukan : ")) 

# huruf_X(l)










# # x kotak tidak sempurna
# def s
#     for i in range(lebar_belah_ketupat):
#         for j in range(lebar_belah_ketupat-i):
#             print(' ',end='')
        
#     for k in range(i+1):
#         print('* ',end='')
#     print()
    
#     for i in range(1,lebar_belah_ketupat):
#         for j in range(i+1):
#             print(' ',end='')
        
#     for k in range(lebar_belah_ketupat-i):
#         print('* ',end='')
#     print()



        