# numero uno

def perkalian(a, b):
    result = 0
    for i in range(b):
        result += a
    return result

# contoh penggunaan fungsi perkalian()
print(perkalian(5, 3)) # Output: 15



# numero duo
def ganjil(batas_bawah, batas_atas):
    if batas_atas < batas_bawah:
        batas_bawah, batas_atas = batas_atas, batas_bawah
        
    for i in range(batas_bawah, batas_atas + 1):
        if i % 2 != 0:
            print(i)

# Input batas bawah dan batas atas dari pengguna
batas_bawah = int(input("Masukkan batas bawah: "))
batas_atas = int(input("Masukkan batas atas: "))

# Memanggil fungsi ganjil()
ganjil(batas_bawah, batas_atas)


# numero dos

def hitung_ips(jumlah_matkul, nilai):
    total_sks = jumlah_matkul * 3
    total_bobot = 0
    
    for i in range(jumlah_matkul):
        if nilai[i] == 'A':
            total_bobot += 4 * 3
        elif nilai[i] == 'B':
            total_bobot += 3 * 3
        elif nilai[i] == 'C':
            total_bobot += 2 * 3
        elif nilai[i] == 'D':
            total_bobot += 1 * 3
    
    ips = total_bobot / total_sks
    return ips

# Input jumlah mata kuliah dan nilai dari pengguna
jumlah_matkul = int(input("Masukkan jumlah mata kuliah: "))
nilai = []
for i in range(jumlah_matkul):
    nilai.append(input(f"Masukkan nilai untuk mata kuliah ke-{i+1}: "))
    
# Memanggil fungsi hitung_ips() dan mencetak hasilnya
ips = hitung_ips(jumlah_matkul, nilai)
print(f"Indeks Prestasi Semester Anda: {ips:.2f}")



