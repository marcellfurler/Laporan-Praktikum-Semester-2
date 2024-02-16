# def is_anagram(word1, word2):
#     # Menghilangkan spasi dan mengubah huruf menjadi lowercase
#     word1 = word1.replace(' ', '').lower()
#     word2 = word2.replace(' ', '').lower()

#     # Mengecek apakah kedua kata memiliki jumlah huruf yang sama
#     if len(word1) != len(word2):
#         return False

#     # Menghitung frekuensi setiap huruf pada kedua kata
#     freq1 = {}
#     freq2 = {}
#     for letter in word1:
#         freq1[letter] = freq1.get(letter, 0) + 1
#     for letter in word2:
#         freq2[letter] = freq2.get(letter, 0) + 1

#     # Mengecek apakah kedua kata memiliki frekuensi huruf yang sama
#     if freq1 == freq2:
#         return True
#     else:
#         return False

# # Meminta input dari pengguna
# word1 = input("Masukkan kata pertama: ")
# word2 = input("Masukkan kata kedua: ")

# # Mengecek apakah kedua kata adalah anagram atau bukan
# if is_anagram(word1, word2):
#     print(word1, "adalah anagram dari", word2)
# else:
#     print(word1, "bukan anagram dari", word2)


# def kata_anagram(kata1, kata2):
#     # mengubah huruf dalam kata menjadi lowercase dan menghapus whitespace
#     kata1 = kata1.lower().replace(" ", "")
#     kata2 = kata2.lower().replace(" ", "")
    
# #     # mengecek jumlah huruf dalam kedua kata
#     if len(kata1) != len(kata2):
#         print(f"Kata {kata1} tidak anagram dengan {kata2}")
#         return False
    
#     # mengecek setiap huruf dalam kedua kata
#     for huruf in kata1:
#         if huruf not in kata2:
#             print(f"Kata {kata1} tidak anagram dengan {kata2}")
#             return False
#         kata2 = kata2.replace(huruf, "", 1)
    
#     print(f"Kata {kata1} adalah anagram dengan {kata2}")
#     return True






# def kata_anagram(kata1, kata2):
#     if kata1.split():
#         print(kata1)
#     for huruf in
#     return kata_anagram(kata1, kata2)

# kata1=input("Masukan kata pertama : ")
# kata2=input("Masukan kata kedua : ")

# kata_anagram(kata1, kata2)



# def kata_anagram(kata1, kata2):
#     for huruf in kata1 and kata2:
#         if huruf:
#             print(huruf)
#         sama=kata1==kata2
#         if sama:
#             print("anagram")
#         else:
#             print("bukan")

    

# kata1=input("masukan : ")
# kata2=input("Masukan : ")

# kata_anagram(kata1, kata2)


# kata_anagaram(kata1)



# def kata_anagram(kata1, kata2):
#     for huruf in kata1 and kata2:
        
#         if huruf not in kata1 or kata2:
#             print("bukan Anagram")
#                 #return True
#         else:
#             print("ana")
#     return kata_anagram

# kata1=input("masukan : ")
# kata2=input("masukan : ")

# kata_anagram(kata1, kata2)

# #### Nomor 1
# def kata_anagram(kata1, kata2):
#     ubah_set_kata1 = set(kata1)
#     ubah_set_kata2 = set(kata2)
#     if ubah_set_kata1 == ubah_set_kata2:
#         print(f"Kata {kata1} anagram dengan {kata2}")
        
#     else:
#         print(f"Kata {kata1} tidak anagram dengan {kata2}")
       

# kata1=input("Masukan Kata Pertama : ")
# kata2=input("Masukan Kata Kedua : ")

# kata_anagram(kata1, kata2)

# #  # return False # return True

# angka=[1, 2, 3, 4]
# angkat=[5,6,7]
# set1=set(angka)
# set2=set(angkat)
# # set(set1)
# print(set1)
# print(set2)



#proses

def kata_anagram(kata1, kata2):
    ubah_set_kata1 = set(kata1)
    ubah_set_kata2 = set(kata2)
    if ubah_set_kata1 == ubah_set_kata2:
        output1=print(f"Kata '{kata1}' anagram dengan kata '{kata2}'")
        
    else:
        output2=print(f"Kata '{kata1}' tidak anagram dengan kata '{kata2}'")
       
# inputan

kata1=input("Masukan Kata Pertama : ")
kata2=input("Masukan Kata Kedua : ")

#panggilan def
kata_anagram(kata1, kata2)