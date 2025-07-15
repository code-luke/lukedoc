#Tanpa KAbisat
print("===NO KABISAT===")
def jumlah_haridari_1_1_1900(d,m,y):

#jumlah hari berdasarkan tahun
    tahun=(y-1900)*365

#jumlah hari berdasarkan bulan
    if m==1:
        bulan= 0
    elif m==2:
        bulan= 31
    elif m==3:
        bulan= 31+28
    elif m==4:
        bulan= 31+28+31
    elif m==5:
        bulan= 31+28+31+30
    elif m==6:
        bulan= 31+28+31+30+31
    elif m==7:
        bulan= 31+28+31+30+31+30
    elif m==8:
        bulan= 31+28+31+30+31+30+31
    elif m==9:
        bulan= 31+28+31+30+31+30+31+31
    elif m==10:
        bulan= 31+28+31+30+31+30+31+31+30
    elif m==11:
        bulan= 31+28+31+30+31+30+31+31+30+31
    elif m==12:
        bulan= 31+28+31+30+31+30+31+31+30+31+30

#rumus
    rumus=int(d+bulan+tahun)
    return rumus

#run program
print (jumlah_haridari_1_1_1900(31,12,1900))
print (jumlah_haridari_1_1_1900(1,1,1901))
print(jumlah_haridari_1_1_1900(1,3,1904))
print(jumlah_haridari_1_1_1900(1,3,1908))
print(jumlah_haridari_1_1_1900(1,3,2100))

#Kabisat
print("===KABISAT===")
def jumlah_haridari_1_1_1900(d,m,y):
    #tahun
    tahun=(y-1900)*365 
    kabisat= (y%4==0 and y%100!=0) or y%400==0 #rumus kabisat
    selang=((y-1900)/4)-((y-1900)/100) #mencegah jika tahun yang dimasukkan bukan kabisat, maka dalam tahun-tahun kabisat sebelumnya tetap terhitung

    #bulan
    if m==1:
        bulan= 0
    elif m==2:
        bulan= 31
    elif m==3:
        if kabisat:
            bulan=31+28+1
            #jumlahkabisat=(y-1900)/4
        else:
            bulan= 31+28
    elif m==4:
        bulan= 31+28+31
    elif m==5:
        bulan= 31+28+31+30
    elif m==6:
        bulan= 31+28+31+30+31
    elif m==7:
        bulan= 31+28+31+30+31+30
    elif m==8:
        bulan= 31+28+31+30+31+30+31
    elif m==9:
        bulan= 31+28+31+30+31+30+31+31
    elif m==10:
        bulan= 31+28+31+30+31+30+31+31+30
    elif m==11:
        bulan= 31+28+31+30+31+30+31+31+30+31
    elif m==12:
        bulan= 31+28+31+30+31+30+31+31+30+31+30
    rumus= int(d+bulan+tahun+selang)#integer agar tidak ada koma
    return rumus

print(jumlah_haridari_1_1_1900(1,3,1904))
print(jumlah_haridari_1_1_1900(1,3,1908))
print(jumlah_haridari_1_1_1900(1,3,2100))
print(jumlah_haridari_1_1_1900(1,3,2104))


#buat fungsi untuk menghitung detik pada jam yang kita masukkan(pada tanggal itu)
#jam tersebut kita ubah menjadi bentuk pm/am
print("\n===KABISATTTTT===")
def jumlah_hari_dari_1900(h,b,t):
    #menghitung tahun kabisat
    dari=1899
    banyak_kabisat=(t//4-dari//4)-(t//100-dari//100)+(t//400-dari//400)
    jumlah_tahun=t-dari
    banyak_biasa=jumlah_tahun-banyak_kabisat-1 #-1 karena tahun terakhir tidak ikut
    jumlah_hariperrtahun= (banyak_biasa*365)+(banyak_kabisat*366)
    kabisat= t//4==0 and t//100!=0 or t//400==0
    if b==1:
        jumlah_hariperrbulan=0
        if kabisat:
            jumlah_hariperrbulan-=1
        else:
            pass
    elif b==2:
        jumlah_hariperrbulan=31
        if kabisat:
            jumlah_hariperrbulan-=1
        else:
            pass
    elif b==3:
        jumlah_hariperrbulan=31+28
    elif b==4:
        jumlah_hariperrbulan=31+28+31
    elif b==5:
        jumlah_hariperrbulan=31+28+31+30
    elif b==6:
        jumlah_hariperrbulan=31+28+31+30+31
    elif b==7:
        jumlah_hariperrbulan=31+28+31+30+31+30
    elif b==8:
        jumlah_hariperrbulan=31+28+31+30+31+30+31
    elif b==9:
        jumlah_hariperrbulan=31+28+31+30+31+30+31+31
    elif b==10:
        jumlah_hariperrbulan=31+28+31+30+31+30+31+31+30
    elif b==11:
        jumlah_hariperrbulan=31+28+31+30+31+30+31+31+30+31
    elif b==12:
        jumlah_hariperrbulan=31+28+31+30+31+30+31+31+30+31+30
    
    rumus= h+jumlah_hariperrbulan+jumlah_hariperrtahun
    return rumus
print(jumlah_hari_dari_1900(1,3,1904))
print(jumlah_hari_dari_1900(1,3,1908))
print(jumlah_hari_dari_1900(1,3,2100))
print(jumlah_hari_dari_1900(1,3,2104))


print("\n===KABISATTTTT + WAKTU===")
def jumlah_hari_dari_1900(h,b,t,waktu):
    #menghitung tahun kabisat
    dari=1899
    banyak_kabisat=(t//4-dari//4)-(t//100-dari//100)+(t//400-dari//400)
    jumlah_tahun=t-dari
    banyak_biasa=jumlah_tahun-banyak_kabisat-1 #-1 karena tahun terakhir tidak ikut
    jumlah_hariperrtahun= (banyak_biasa*365)+(banyak_kabisat*366)
    kabisat= t//4==0 and t//100!=0 or t//400==0
    j,m,s= waktu

    #Menghitung Hari
    if b==1:
        jumlah_hariperrbulan=0
        if kabisat:
            jumlah_hariperrbulan-=1
        else:
            pass
    elif b==2:
        jumlah_hariperrbulan=31
        if kabisat:
            jumlah_hariperrbulan-=1
        else:
            pass
    elif b==3:
        jumlah_hariperrbulan=31+28
    elif b==4:
        jumlah_hariperrbulan=31+28+31
    elif b==5:
        jumlah_hariperrbulan=31+28+31+30
    elif b==6:
        jumlah_hariperrbulan=31+28+31+30+31
    elif b==7:
        jumlah_hariperrbulan=31+28+31+30+31+30
    elif b==8:
        jumlah_hariperrbulan=31+28+31+30+31+30+31
    elif b==9:
        jumlah_hariperrbulan=31+28+31+30+31+30+31+31
    elif b==10:
        jumlah_hariperrbulan=31+28+31+30+31+30+31+31+30
    elif b==11:
        jumlah_hariperrbulan=31+28+31+30+31+30+31+31+30+31
    elif b==12:
        jumlah_hariperrbulan=31+28+31+30+31+30+31+31+30+31+30
    
    banyak_hari= int(h+jumlah_hariperrbulan+jumlah_hariperrtahun)
    #hitung jamperhari ke detik
    jam_perrhari=24*3600
    #ubah semua waktu ke detik
    jam=j*3600
    menit=m*60
    detik= s
    #jumlah semua detik
    jumlah_detik= int((banyak_hari-1)*jam_perrhari+jam+menit+detik)
    print (f"Jumlah hari nya adalah: {banyak_hari:,} hari")
    print (f"Jumlah detik sampai tanggal tersebut adalah: {jumlah_detik:,} detik")

    #Membuat pukul AM dan PM
    if j>=12 and m>=0:
        Jam_PM= j-12
        print(f"Pukul yang dimasukkan: {Jam_PM,m,s} PM")
    else:
        print(f"Pukul yang dimasukkan: {j,m,s} AM")
jumlah_hari_dari_1900(1,3,1904,(12,10,32))
print("\n")
jumlah_hari_dari_1900(1,3,1904,(11,59,59))