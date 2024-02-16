# # Nomor 1

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




# # Nomor 2

import re
import random

def baca_email_regex(email):
    regex=r"\b([A-Za-z]+)@([A-Za-z]+)\.(com|co\.id)\b"
    hasil=re.findall(regex, email)
    for email_pengguna in hasil:
        email=(f"{email_pengguna[0]}@{email_pengguna[1]}.{email_pengguna[2]}")
        username=email_pengguna[0]
        karakter_password="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        password= ''.join(random.choice(karakter_password) for x in range(8))
        
        print(f"Email Anda : {email}\nusername : {username}\npassword : {password}")
        print()

email="Berikut adalah daftar email dan nama pengguna dari mailing list: anton@mail.com dimiliki oleh antonius budi@gmail.co.id dimiliki oleh budi anwari slamet@getnada.com dimiliki oleh slamet slumut matahari@tokopedia.com dimiliki oleh toko matahari"
baca_email_regex(email)
