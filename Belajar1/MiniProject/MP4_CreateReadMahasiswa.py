# LATIHAN DICTIONARY
# Memasukan data melalui input ke dalam dictionary

import datetime as dt
import os
import string
import random

templateMahasiswa = { # → Jadi semacam “kerangka” dictionary mahasiswa. Supaya tiap mahasiswa selalu punya field yang sama.
    'nama':'nama',
    'nim':'nim',
    'sks_lulus':12,
    'lahir' : dt.datetime(1111,1,11)
}

dataMahasiswa = {}

while True:
    os.system("clear")

    print(f"{'SELAMAT DATANG':^30}")
    print(f"{'DATA MAHASISWA':^30}")
    print("="*40)

    mahasiswa = dict.fromkeys(templateMahasiswa.keys()) #→ membuat dictionary baru dengan key yang sama(template mahasiswa), tapi semua value diisi None (default).

    mahasiswa['nama'] = input("Nama Mahasiswa : ")
    mahasiswa['nim'] = int(input("NIM Mahasiswa : "))
    mahasiswa['sks_lulus'] = int(input("SKS Yang Ditempuh : "))
    TAHUN_LAHIR = int(input("Tahun Lahir (YYYY): "))
    BULAN_LAHIR = int(input("Bulan Lahir (1-12): "))
    TANGGAL_LAHIR = int(input("TANGGAl Lahir (1-31): "))
    mahasiswa['lahir'] = dt.datetime(TAHUN_LAHIR, BULAN_LAHIR, TANGGAL_LAHIR)


    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(5))) # Membuat 5 Karakter String Random (Kayak jadi primary/unique)
    dataMahasiswa.update({KEY:mahasiswa}) # → Data mahasiswa masuk ke dictionary utama dengan KEY sebagai identitas unik.


    print(f"{'KEY':<5} {'Nama':<15} {'NIM':<10} {'SKS':<5} {'Lahir':<10}")
    print(f"="*55)

    for mhs in dataMahasiswa:
        KEY = mhs

        NAMA = dataMahasiswa[KEY]['nama']
        NIM = dataMahasiswa[KEY]['nim']
        SKS = dataMahasiswa[KEY]['sks_lulus']
        LAHIR = dataMahasiswa[KEY]['lahir'].strftime('%x')
        
        print(f"{KEY:<5} {NAMA:<15} {NIM:<10} {SKS:<5} {LAHIR:<10}")

    isTanya = input("Lanjut? (y/n) : ")

    if isTanya != 'y':
        break

print("AKHIR PROGRAM")