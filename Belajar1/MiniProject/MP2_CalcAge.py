#Latihan Membuat Kalkulator Umur

import datetime as dt
import os

def userInput():
    tanggal = int(input("Tanggal \t = "))
    bulan = int(input("Bulan \t\t = "))
    tahun = validasi_tahun()
    return tahun, bulan, tanggal

def cekUmur(tanggalLahir):
    hariIni = dt.date.today()

    umurTahun = hariIni.year - tanggalLahir.year
    umurBulan = hariIni.month - tanggalLahir.month

    if hariIni < tanggalLahir.replace(year=hariIni.year): # Cek apakah kamu sudah melewati ulang tahun pada tahun ini
        umurTahun -= 1                                    # Jika Belum Melewati, Maka Umur di Kurangi 1 (Karena tahun ini belum ultah)
        umurBulan = (12 + hariIni.month - tanggalLahir.month) % 12 
        return umurTahun, umurBulan

def validasi_tahun():
      while True:
        try:
            tahun = int(input("Tahun \t\t = "))
            if len(str(tahun)) == 4:
                return tahun
            else:
                print("Format tahun harus 4 digit, silahkan masukan lagi (yyyy)")
        except:
            print("Format tahun harus angka, silahkan masukan lagi (yyyy)")


while True:
    os.system('clear')
    print(60*"="+"""
    SILAHKAN MASUKAN TANGGAL, BULAN dan TAHUN LAHIR ANDA
="""+60*"=")

    tahun, bulan, tanggal = userInput()

    tanggalLahir = dt.date(tahun, bulan, tanggal)
    dataLahir = f"Kelahiran Kamu\t = {tanggal} {tanggalLahir:%B} {tahun}"
    print(dataLahir)

    umurTahun, umurBulan = cekUmur(tanggalLahir)

    print(f"Umur Kamu\t = {umurTahun} Tahun {umurBulan} Bulan")

    print(60*"="+"""
                TERIMA KASIH
="""+60*"=")

    isLanjut = input("Lanjut (y/n) ? ")
    if isLanjut == 'n' :
        break

print("Program Berakhir!!!")