def kata_anagram(kata1, kata2):
    ubah_set_kata1 = set(kata1)
    ubah_set_kata2 = set(kata2)
    if ubah_set_kata1 == ubah_set_kata2:
        print(f"Kata {kata1} anagram dengan {kata2}")
        
    else:
        print(f"Kata {kata1} tidak anagram dengan {kata2}")
       

kata1=input("Masukan Kata Pertama : ")
kata2=input("Masukan Kata Kedua : ")

kata_anagram(kata1, kata2)