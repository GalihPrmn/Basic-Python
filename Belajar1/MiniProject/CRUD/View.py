from . import  Operasi
from .Util import validasi_tahun

def read_console():
    data_file = Operasi.read()
    
    index = "No"
    judul = "Judul"
    penulis = "Penulis"
    tahun = "Tahun"

    
    #Header
    print("\n" + "="*100)
    print(f"{index:4} | {judul:40} | {penulis:30} | {tahun:5}")
    print("-"*100)

    #Data
    for index, data in enumerate(data_file):
        data_break = data.split(",")
        pk = data_break[0]
        date_add = data_break[1]
        judul = data_break[2]
        penulis = data_break[3]
        tahun = data_break[4]

        print(f"{index+1:4} | {judul:.40} | {penulis:.30} | {tahun:4}", end="")
        

    #Footer
    print("="*100 + "\n")
    

def create_console():
    print("\n\n"+"="*100)
    print("Silahkan tambah data buku\n")


    judul = input("Judul\t: ")
    penulis = input("Penulis\t: ")
    tahun = validasi_tahun()

    Operasi.create(judul, penulis, tahun)
    print("\nBerikut data baru anda")
    read_console()


def update_console():
    read_console()
    while True:
        no_buku = int(input("Pilih Nomor dari Data yang mau di update : "))
        data_buku = Operasi.read(index=no_buku)

        if data_buku:
            break
        else:
            print("Nomor tidak valid, silahkan masukan lagi")

    data_break = data_buku.split(",")
    pk = data_break[0]
    date_add = data_break[1]
    judul = data_break[2]
    penulis = data_break[3]
    tahun = data_break[4][:-1] # Enter nya gk diambil

    while True:
        # data yang ingin di update
        print("\n" + "="*100)
        print("Silahkan pilih data apa yang mau anda ubah")
        print(f"1. Judul\t: {judul:.40}")
        print(f"2. Penulis\t: {penulis:.40}")
        print(f"3. Tahun\t: {tahun:4}")

        # memilih mode untuk update
        userOpt = input("Pilih data [1,2,3]: ")
        match userOpt:
            case "1" : judul = input("Judul\t: ")
            case "2" : penulis = input("Penulis\t: ")
            case "3" : tahun = validasi_tahun()
            case _: print("Index yang anda pilih tidak cocok")
        
        isLanjut = input("Mau Lanjut Updatenya (y/n) ? ")
        if isLanjut.lower() == 'n':
            break
    
    Operasi.update(no_buku, pk, date_add, judul, penulis, tahun)




def delete_console():
    read_console()
    while True:
        no_buku = int(input("Pilih Nomor dari Data yang mau di hapus : "))
        data_buku = Operasi.read(index=no_buku)

        if data_buku:
            data_break = data_buku.split(",")
            pk = data_break[0]
            date_add = data_break[1]
            judul = data_break[2]
            penulis = data_break[3]
            tahun = data_break[4][:-1] # Enter nya gk diambil

                # data yang ingin di hapus
            print("\n" + "="*100)
            print("data apa yang ingin anda hapus")
            print(f"1. Judul\t: {judul:.40}")
            print(f"2. Penulis\t: {penulis:.40}")
            print(f"3. Tahun\t: {tahun:4}")

            isLanjut = input("Apakah anda yakin (y/n) ? ")
            if isLanjut.lower() == 'y':
                Operasi.delete(no_buku)
                break
        else:
            print("Nomor tidak valid, silahkan masukan lagi")

    print("Data Berhasil di Hapus")
