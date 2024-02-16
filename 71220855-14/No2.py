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



