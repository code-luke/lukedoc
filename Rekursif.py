#FAKTORIAL
def fctrial(x):
    if x==1:
        return x
    else:
        return fctrial(x-1)*x
print(fctrial(5))

# 1. TAMBAH
def tambah(x,y):
    if y==0:
        return x
    else:
        return 1+ tambah(x,y-1)
print(tambah(3,100))

# 2. KURANG
def kurang(x,y):
    if y==0:
        return x
    else:
        return kurang(x,y-1) -1
print(kurang(0,100))

# 3. KALI
def kali(x,y):
    if y==0:
        return y
    else:
        return x+ kali(x,y-1)

print(kali(4,5))

# 4. BAGI FLOOR
def bagi(x,y):
    if x<y:
        return 0
    else:
        return 1+bagi(x-y,y)
print(bagi(9,2))

# 5. PANGKAT
def pangkat(x,y):
    if y==0:
        return 1
    else:
        return x*pangkat(x,y-1)
    
print(pangkat(3,1))

# 6. Perkalian 3
def kali3(x):
    if x==0:
        return 0
    else:
        return 3+kali3(x-1)

print(kali3(12))

# 7. DERET INTEGER
def dint(x):
    if x==0:
        return 0
    else:
        return x+dint(x-1)
    
print(dint(10))

# 8. DERET 3,6,9
def dart369(x):
    if x==1:
        return 3
    else:
        return 3*x+dart369(x-1)
    
print(dart369(2))

# 9. DERET GEOMETRI (1,3,9)
def geo(x):
    if x==0:
        return 0
    else:
        return 3**(x-1) + geo(x-1)
    
print(geo(4))

# 10. DERET 1,4,9,16 (+3,+5,+7)
def der(x):
    if x==0:
        return 0
    else:
        return x**2 + der(x-1)
print(der(2))
print(der(3))
print(der(4))