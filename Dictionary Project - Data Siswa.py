data= {}
def daftar():
    print("PILIH SALAH SATU OPSI DIBAWAH")
    print('''1. Tambah Data
2. Ubah Data
3. Hapus Data
4. Lihat Data
5. Selesai''')

def Tambah():
    Nama=input('Masukkan Nama:\n')
    Kelas=input('Masukkan Kelas:\n')
    Absen=input('Masukkan Nomor Absen:\n')
    Nilai=input('Masukkan Nilai:\n')
    data[Nama]= {'Kelas': Kelas, 'Absen': Absen, 'Nilai': Nilai}
    print(f'{Nama} sudah ditambahkan ke Data Siswa')

def Ubah():
    siapa= input('Data siapa yang pengen diedit?\n')
    if siapa in data:
        print(f'Masukkan data {siapa} yang baru')
        Kelas2=input('Kelas:\n')
        Absen2=input('Absen:\n')
        Nilai2=input('Nilai:\n')
        data[siapa]= {'Kelas':Kelas2, 'Absen':Absen2, 'Nilai':Nilai2}
        print(f'Data {siapa} sudah diubah')
    else:
        print(f'{siapa} tidak ada di data siswa')

def Hapus():
    siapa= input('Data siapa yang pengen dihapus?\n')
    if siapa in data:
        del data[siapa]
        print(f'Data {siapa} sudah dihapus')
    else:
        print(f'{siapa} tidak ada di data siswa')

def Lihat():
    print('====DATA SISWA===')
    print(f"{'NAMA':<12}{'KELAS':<10}{'ABSEN':<8}{'NILAI':<5}")
    print("-"*38)
    for nama,datasiswa in data.items():
        Kelas=datasiswa['Kelas']
        Absen=datasiswa['Absen']
        Nilai=datasiswa['Nilai']
        print(f"{nama:<12}{Kelas:<10}{Absen:<8}{Nilai:^5}")

while True:
    daftar()
    opsi=int(input('Pilih salah satu opsi\n'))
    if opsi==1:
        Tambah()
    elif opsi==2:
        Ubah()
    elif opsi==3:
        Hapus()
    elif opsi==4:
        Lihat()
    if opsi==5:
        break
    else:
        print('Pilih salah satu nomor (1-4)!')