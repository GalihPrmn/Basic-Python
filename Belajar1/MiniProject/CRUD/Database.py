from . import Operasi


DB = "data.txt"
TEMPLATE = {
    "pk" : "XXXXXX",
    "date_add" : "yyyy-mm-dd",
    "judul" : 255*" ",
    "penulis" : 255*" ",
    "tahun" : "yyyy"
}

def init_console():
    try:
        with open(DB, mode="r") as file:
            print("Data Tersedia, Init Done!")
    except:
        print("Database tidak ditemukan, silahkan membuat database baru!")
        Operasi.create_first_data()