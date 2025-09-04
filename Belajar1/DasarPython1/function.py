# FUNCTION
import os
# os.system("clear")

# def helloWorld():
#     print("Halo Dunia")

# helloWorld()


# Function dengan Argument / Parameter / Input ~~~~~~~~~~~~~~~~``
# def tambah(angka1, angka2): 
#     hasil = angka1 + angka2
#     print(hasil)

# tambah(100, 50)

# def sayHello(listPeserta):
#     listPeserta[1] = "Iuno" # listPeserta dan anggota menunjuk ke list yang sama di memori. (jadi kalo ini berubah, yang lain juga berubah karena listPeserta = anggota)
#     dataAnggota = listPeserta.copy() # Kalo tidak mau berubah pake ini
#     for i in dataAnggota:
#         print(f"Hello Ms. {i}")

# anggota = ['Kurumi', 'Jinshi', 'Carlotta']

# sayHello(anggota)
# # print(anggota)



# Function dengan Return ~~~~~~~~~~~~~~~~
def kuadrat(x):
    hasil = x**2
    return hasil # -> Kalo Ini bisa di proses lebih lanjut, 

y = kuadrat(5) + kuadrat(2) # -> kalo pake return bisa di pakai lagi oleh operator ...
# print(y) 

def tambah(angka1, angka2):
    return angka1 + angka2

hasil = tambah(12, 12)
# print(hasil)


# Function dengan return banyak~~~~~~~~~~~~~
def op_mtk_banyak(x, y):
    tambah = x + y
    kurang = x - y
    kali = x * y
    bagi = x / y

    return tambah, kurang, kali, bagi

k,l,m,n = op_mtk_banyak(10, 5)

# print(f"Function Tambah = {k}")
# print(f"Function Kurang = {l}")
# print(f"Function Kali = {m}")
# print(f"Function Bagi = {n}")


# Functiom Default Argument ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def sayHello(nama = "User!"): #-> Membuat Default Argument
    print(f"Wellcome {nama}")

def hitungPangkat(angka, pangkat = 2):
    return angka**pangkat

hasil = hitungPangkat(angka=5) #-> Bisa Juga ambil argument nya supaya tidak membingungkan kalo argument nya banyak
# print(hasil)



# Type Hints ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def paraf(angka1:int) -> int:
    return angka1 #-> Default Output nya Any

def jail(nama):
    print(jail) #-> Default Output nya None

# jail()
# paraf(12121) # Arahkan kursor ke paraf


# *args ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def tambah(*args): # Tanda utamanya */bintang -> namanya bebas
    # Data Type nya Tuple, jadi bisa di iterasi
    output = 0
    for angka in args:
        output += angka
    return output

def kali(*angka):
    output = 0
    for i in angka:
        output *= i
    return output

def say(*name):
    print(name)

# say("Galih", "Dimas", "Ari")

hasil = tambah(2,2,2,2,2,2,2,2,2,2,2)
# print(f"Hasil = {hasil}")


# *kwargs ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
def gracias(**kwargs): #-> Versi named dari args biasa
    nama = kwargs['nama']
    umur = kwargs['umur']
    tinggi = kwargs['tinggi']
    print(f"Namanya {nama}, Umur {umur} Tahun, dengan tinggi {tinggi} cm")

# gracias(nama="Galih", umur=19, tinggi=180)


def math(*args, **kwargs):
    hasil = 0
    if kwargs['option'].lower() == 'tambah':
        for i in args:
            hasil += i
    elif kwargs['option'].lower() == 'kali':
        hasil = 1
        for kal in args:
            hasil *= kal
    return hasil


# hasil = math(5,5,5,5,5,5,option="TAMBAH")
hasil = math(2,2,2,option="KALI")
# print(hasil)



# LAMBDA Function ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# output = lambda argument:expression
# Kayak function versi ringkas
hasilPangkat = lambda angka:angka**2
# print(f"Hasil = {hasilPangkat(5)}")

hasilPangkat2 = lambda angka1,angka2: angka1**angka2
# print(f"Hasil = {hasilPangkat2(5, 3)}")

# Contoh Kegunaan -> Sort/Map/Filter/Reduce
dataList = ['Dimas', 'Ari Zulham', 'Adit', 'Taufiq', 'Ilham']
dataList.sort(key=lambda nama:len(nama)) # Len -> berdasarkan panjang angka

# print(f"Data List by Lambda = {dataList}")

dataAngka = [1,2,3,4,5,6,7,8,9,10]
genap = list(filter(lambda angka: angka % 3 == 0, dataAngka)) # 1 Ganjil, 0 Genap, Modulus 3=0 (Kelipatan 3)

# print(genap)



# ANONYMOUS FUNCTION ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Teknik Currying

# Kayak Nested Function
def pangkat(n):
    return lambda angka:angka**n

pangkat2 = pangkat(2)
pangkat3 = pangkat(3)

print(f"Pangkat 2 = {pangkat2(5)}")
print(f"Pangkat 3 = {pangkat3(5)}")
print(f"Pangkat Bebas = {pangkat(3)(3)}")