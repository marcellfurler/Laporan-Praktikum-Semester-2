# # import re

# # def format_tanggal(kalimat):
# #     reg=r"(\d{4})-(\d{2})-(\d{2})"
# #     hasil=re.sub(reg, r"\3-\2-\1", kalimat)
# #     return hasil
    


# # print(format_tanggal("Pada tanggal 1945-08-17 Indonesia merdeka. Indonesia memiliki beberapa pahlawan nasional, seperti Pangeran Diponegoro (TL: 1785-11-11), Pattimura (TL: 1783-06-08) dan Ki Hajar Dewantara (1889-05-02)."))


# import re

# def format_tanggal(kalimat):
#     pattern = r"(\d{4})-(\d{2})-(\d{2})"
#     hasil = re.search(pattern, kalimat)
#     if hasil:
#         return hasil
#     else:
#         return None

# # Contoh penggunaan
# # kalimat = "Hari ini adalah tanggal 2023-06-09."
# # hasil = format_tanggal(kalimat)
# kalimat="Pada tanggal 1945-08-17 Indonesia merdeka. Indonesia memiliki beberapa pahlawan nasional, seperti Pangeran Diponegoro (TL: 1785-11-11), Pattimura (TL: 1783-06-08) dan Ki Hajar Dewantara (1889-05-02)."
# kalimat=format_tanggal(kalimat)
# print(kalimat)


# # for i in kalimat:
# #     print(i)
# # print(format_tanggal("Pada tanggal 1945-08-17 Indonesia merdeka. Indonesia memiliki beberapa pahlawan nasional, seperti Pangeran Diponegoro (TL: 1785-11-11), Pattimura (TL: 1783-06-08) dan Ki Hajar Dewantara (1889-05-02)."))





# import re
# import time

# def format_tanggal(kalimat):
#     regex=r"\d{4}-(\d{2})-(\d{2})"
#     waktu_sekarang=time.time()

#     hasil=re.findall(regex, kalimat)
#     for waktu in hasil:
#         tanggal_formatted = time.strftime("%d-%m-%Y", time.strptime(waktu, "%Y-%m-%d"))
#         selisih_hari = int((waktu_sekarang - time.mktime(time.strptime(tanggal_formatted, "%Y-%m-%d"))) / (24*60*60))
#         print(f"{tanggal_formatted} 00:00:00 selisih {selisih_hari} hari")

# kalimat = "Pada tanggal 1945-08-17 Indonesia merdeka. Indonesia memiliki beberapa pahlawan nasional, seperti Pangeran Diponegoro (TL: 1785-11-11), Pattimura (TL: 1783-06-08) dan Ki Hajar Dewantara (1889-05-02)."
# format_tanggal(kalimat)



import re
from datetime import datetime

def format_tanggal(kalimat):
    regex = r"(\d{4})-(\d{2})-(\d{2})"
    tanggal_sekarang = datetime.now()

    hasil = re.findall(regex, kalimat)
    for tanggal in hasil:
        tahun = int(tanggal[0])
        bulan = int(tanggal[1])
        hari = int(tanggal[2])

        bentuk_tanggal = (f"{hari:02d}-{bulan:02d}-{tahun}")
        jarak_hari = (tanggal_sekarang - datetime(tahun, bulan, hari)).days

        print(f"{bentuk_tanggal} 00:00:00 selisih {jarak_hari} hari")

kalimat = "Pada tanggal 1945-08-17 Indonesia merdeka. Indonesia memiliki beberapa pahlawan nasional, seperti Pangeran Diponegoro (TL: 1785-11-11), Pattimura (TL: 1783-06-08) dan Ki Hajar Dewantara (1889-05-02)."
format_tanggal(kalimat)


