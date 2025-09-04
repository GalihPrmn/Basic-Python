import random
import string


def random_string(panjang:int)->str:
    hasilRandomString = ''.join(random.choice(string.ascii_letters) for i in range(panjang))
    return hasilRandomString


def validasi_tahun():
      while True:
        try:
            tahun = int(input("Tahun\t: "))
            if len(str(tahun)) == 4:
                return tahun
            else:
                print("Format tahun harus 4 digit, silahkan masukan lagi (yyyy)")
        except:
            print("Format tahun harus angka, silahkan masukan lagi (yyyy)")
