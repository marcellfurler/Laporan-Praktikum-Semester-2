kartu_keluarga={
    "nomor":3275110106070203,
    "Orang":["Sudarto", "Usmar Anliesari Sit", "Afrida Saputra", "Yosse Saputra", "Jul Usmar Djumena"],
    "Kepala_Keluarga":"Sudarto",
    "Istri":"Usmar Anliesari Sit",
    "Anak":["Afrida Saputra", "Yosse Saputra"],
    "Family Lain":"Jul Usmar Djumena",
    "Belum Kawin":["Afrida Saputra", "Yosse Saputra", "Jul Usmar Djumena"],
    "Agama":"Islam",
    "Status Kawin":["Kawin", "Belum Kawin"],
    "Kewarganegaraan":["WNI", "WNA"],
    "Tahun Lahir":[1965,1977,2000,2004,1961]

}

print(f"1. Kepala keluarganya adalah {kartu_keluarga['Orang'][0]}")
print(f"2. Orang di dalam KK berjumlah {len(kartu_keluarga['Orang'])}")
for i in range(len(kartu_keluarga['Orang'])):
    print(f"Nama : {kartu_keluarga['Orang'][i]}, beragama {kartu_keluarga['Agama']}")
for x in range(len(kartu_keluarga["Belum Kawin"])):
    print(f"Yang belum Kawin adalah : {kartu_keluarga['Belum Kawin'][x]}")
for y in range(len(kartu_keluarga['Anak'])):
    print(f"5. Anaknya adalah {kartu_keluarga['Anak'][y]}")
print(f"6. Yang belum kawin tidak ada")
for a in kartu_keluarga["Tahun Lahir"]:
    if a>2000:
        print(f"7. yang tahun lahirnya diatas 2000 adalah : {kartu_keluarga['Belum Kawin'][1]}")










#"3275111002860003","Pria", "Jakarta", "10 oktober 1965", "Islam"]
