khs={
    "71220855":["Bahasa Belanda", "Matematika", "Musik", "Musik pop", "Teknik Musik"],
    "71220856":["Agama Islam", "Pendidikan Bahasa Planet", "Pendidikan Galaxy Internasional NASA"]
}

for matkul in khs.keys():
    print(f"NIM : {matkul}, matkul : {khs[matkul]}")

print() 

khs["71220855"].append("International Netherland Tour")
print(khs)


print()

print("kedua")
del khs["71220856"][0]
print(khs)