penyanyi=[
    {"Sia":"Chandelier"},
    {"Jessie" : "Flashlight"},
    {"Billie":"Bad Guy"},
    {"Faouzia":"Minefields"},
    {"Marcell":"Love Story From The Chapel"},
]

hasil=[]
for a in penyanyi:
    for value in a.values():
        if hasil.count(value)==0:
            hasil.append(value)

print(hasil)