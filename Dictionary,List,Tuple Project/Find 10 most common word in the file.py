#METOD 1
print('- METOD 1')
file= open('latihan_kata_terbanyak.txt')
dcty= dict()
lst=list()

for line in file:
    line=line.split()
    for word in line:
        dcty[word]=dcty.get(word, 0)+1

for key,val in dcty.items():
    tup=(val,key)
    lst.append(tup)

lst=sorted(lst, reverse=True)
for val,key in lst[:10]:
    print(key,'=',val)

#METOD2
print('\n- METOD 2')
file= open('latihan_kata_terbanyak.txt')
dcty= dict()
lst=list()

for line in file:
    line=line.split()
    for word in line:
        dcty[word]=dcty.get(word, 0)+1

lst=sorted([(val,key) for key,val in dcty.items()], reverse=True) #whats the program said?(look on the next line)
#membuat list-> membuat tuple yang berisi val,key->lalu mengurutkan(sorted)

print('=== TOP 10 MOST COMMON WORD ===')
for val,key in lst[:10]:
    print(f'{key}= {val}')