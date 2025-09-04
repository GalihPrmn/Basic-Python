# Global dan Local Scope

# Global Scope
nama = "Dimas" #-> Variable Global

def sayHello():
    print(f"Haloo {nama}")

sayHello()

# Local Scope

def sayGoodbye():
    nama2 = "Ari"
    print(f"Selamat Tinggal {nama2}")

sayGoodbye()
# print(nama2) -> Ini gak bisa, karena nama2 hanya bisa diakses di function sayGoodbye

def sayIlham():
    print(f"Halo {nama3}")

nama3 = "Ilham" #-> Ini bisa, karena variable ini dijalankan terlebih dahulu sebelum memanggil function nya (enterpreter)
sayIlham()


# Membuat Var local menjadi global
namaLama = "Indra"
def ubahNama(namabaru):
    global namaLama  # -> dengan meng inialisasi kan variable local ke global, kita bisa mengubah isinya
    namaLama = namabaru

ubahNama("Taufiq")
print(namaLama)