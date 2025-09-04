# Latihan Function
# Membuat Program Menghitung Luas dan Keliling Persegi Panjang

import os


# Header Program
def header():
    os.system('clear')

    print(f"{'PROGRAM MENGHITUNG LUAS':^40}", end="")
    print(f"{'DAN KELILING PERSEGI PANJANG':^40}", end="")
    print(f"{'='*40:^40}")

def pemisah():
    print(f"{'='*40:^40}")

# Mengambil Input User
def inputUser():
    lebar = int(input("Masukan Lebar   : "))
    panjang = int(input("Masukan Panjang : "))
    return lebar, panjang


# Menghitung Luas dan Keliling
def hitungLuas(lebar, panjang):
    return lebar * panjang

def hitungKeliling(lebar, panjang):
    return 2*(lebar+panjang)

# Menampilkan Hasil
def display(message, value = ""):
    print(f"Hasil Perhitungan {message} = {value}")


# Pilih Hitung Yang Mana
def pilihanUser():
    option = int(input("1. Hitung Luas \n2. Hitung Keliling \n3. Hitung Luas dan Keliling \nPilih Opsi = "))
    return option

# Pilihan user di proses
def optPilihan(userOpt, lebar, panjang):
    if userOpt == 1:
        LUAS = hitungLuas(lebar, panjang)
        display("Luas", LUAS)
    elif userOpt == 2:
        KELILING = hitungKeliling(lebar, panjang)
        display("Keliling", KELILING)
    elif userOpt == 3:
        LUAS = hitungLuas(lebar, panjang)
        KELILING = hitungKeliling(lebar, panjang)
        display("Luas", LUAS), display("Keliling", KELILING)


# Program Utama
while True:
    header()
    piluser = pilihanUser()

    if piluser not in [1,2,3]: # Akan Kembali Ke awal program jika pilihan nya tidak ada
        input("Pilih Opsi Yang Sudah Ada (tekan ENTER untuk lanjut)") # dipakai supaya program berhenti sebentar, user baca pesan dulu.
        continue

    pemisah()

    LEBAR, PANJANG = inputUser() # mengambil inputan dari user

    pemisah()

    optPilihan(piluser, lebar=LEBAR, panjang=PANJANG) # Pilihan Hitungan User, dan Eksekusi Programnya

    pemisah()

    isLanjut = input("Lanjut (y/n)? ")
    if isLanjut.lower() == "n":
        break

print(f"{'PROGRAM SELESAI':^40}")