from . import Database
from .Util import random_string, validasi_tahun
import time
import os

def create_first_data():
    judul = input("Judul : ")
    penulis = input("Penulis : ")
    tahun = validasi_tahun()

    data = Database.TEMPLATE.copy()

    data['pk'] = random_string(6)
    data['date_add'] = time.strftime('%Y-%m-%d-%H-%M-%S%z', time.gmtime())
    data['judul'] = judul + Database.TEMPLATE['judul'][len(judul):]
    data['penulis'] = penulis + Database.TEMPLATE['penulis'][len(penulis):]
    data['tahun'] = str(tahun)

    data_str = f"{data['pk']}, {data['date_add']}, {data['judul']}, {data['penulis']}, {data['tahun']}\n"
    try:
        with open(Database.DB, 'w', encoding="utf-8") as file:
            file.write(data_str)
    except Exception as e:
        print(f"Error : {e}")


def read(**kwargs):
    try:
        with open(Database.DB, mode="r") as file:
            content = file.readlines()
            jumlah_buku = len(content)
            if "index" in kwargs:
                index_buku = kwargs['index']-1
                if index_buku < 0 or index_buku > jumlah_buku:
                    return False
                else:
                    return content[index_buku]
            else: 
                return content
    except Exception as e:
        print(f"Error: {e}")
        return False
    

def create(judul, penulis, tahun):
    data = Database.TEMPLATE.copy()

    data['pk'] = random_string(6)
    data['date_add'] = time.strftime('%Y-%m-%d-%H-%M-%S%z', time.gmtime())
    data['judul'] = judul + Database.TEMPLATE['judul'][len(judul):]
    data['penulis'] = penulis + Database.TEMPLATE['penulis'][len(penulis):]
    data['tahun'] = str(tahun)

    data_str = f"{data['pk']},{data['date_add']},{data['judul']},{data['penulis']},{data['tahun']}\n"

    try:
        with open(Database.DB, 'a', encoding="utf-8") as file:
            file.write(data_str)
    except Exception as e:
        print(f"Error : {e}")


def update(no_buku, pk, date_add, judul, penulis, tahun):
    data = Database.TEMPLATE.copy()

    data['pk'] = pk
    data['date_add'] = date_add
    data['judul'] = judul + Database.TEMPLATE['judul'][len(judul):]
    data['penulis'] = penulis + Database.TEMPLATE['penulis'][len(penulis):]
    data['tahun'] = str(tahun)

    data_str = f"{data['pk']},{data['date_add']},{data['judul']},{data['penulis']},{data['tahun']}\n"

    try:
        with open("data.txt", mode="r") as file:
            data_sementara = file.readlines() 
            data_sementara [no_buku-1]  =   data_str
        with open("data.txt", mode="w") as file:
            file.writelines(data_sementara) 

    except Exception as e:
        print(f"Error : {e}")


def delete(no_buku):
    # Cara readlines() → baca semua data jadi list, hapus item, lalu tulis ulang.
    # try:
    #     with open(Database.DB, mode="r") as file:
    #         data_sementara = file.readlines() 
    #     print(no_buku)
    #     no_buku = int(input("Pilih Nomor dari Data yang mau di hapus : "))
        
    #     # hapus baris sesuai index
    #     del data_sementara[no_buku-1]

    #     with open("data.txt", mode="w") as file:
    #         file.writelines(data_sementara)  

    #     print("Data berhasil dihapus!")

    # except Exception as e:
    #     print(f"Error : {e}")


    # Cara file temp → langsung tulis data satu per satu ke file sementara, tanpa harus simpan semua isi file ke memori.
    # Jadi cara file temp lebih aman & hemat memori kalau data besar (ribuan/jutaan baris).
    try:
        with open(Database.DB,'r') as file:
            counter = 0

            while(True):
                content = file.readline()
                if len(content) == 0: # Jika data nya gak ada, keluar
                    break
                elif counter == no_buku - 1: # Data Yang mau di hapus akan di lewat
                    pass
                else:
                    with open("data_temp.txt",'a',encoding="utf-8") as temp_file:
                        temp_file.write(content)    # Simpan baris lain ke file sementara
                counter += 1
    except:
        print("database error")
    
    os.rename("data_temp.txt",Database.DB) 
    # Setelah semua selesai, file lama (data.txt) ditimpa/rename dengan data_temp.txt.
    # Hasilnya: data.txt sekarang berisi semua data kecuali baris yang dihapus.