dict_hours = dict()
lst = list()

fname = input('Masukkan file name : ')
try:
    fhand = open(fname)
except:
    print('File tidak ditemukan:',fname)
    quit()

for line in fhand:
    kata = line.split()
    if len(kata) < 2 or kata[0] != 'From':
        continue

    col_pos = kata[5].find(':')
    hour = kata[5][:col_pos]
    if hour not in dict_hours:
        dict_hours[hour]=1
    else:
        dict_hours[hour]+=1

for key, val in list(dict_hours.items()):
    lst.append((key,val))

lst.sort()

for key, val in lst:
    print(key,val)
