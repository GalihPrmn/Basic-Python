# Exception akan terjadi saat program mengalami error saat runtime 

from numbers import Number

# while True:
#     angka = int(input("Masukan Angka Pembagi = "))
#     try:
#         hasil = 10/angka
#         print(f"Hasil = {hasil}")
#         isDone = input("Lanjutkan (y/n)? ")
#         if isDone == 'n':
#             break
#     except Exception as errorMessage:
#         print(f"Terjadi Kesalahan : {errorMessage}")
#     finally:
#         print("Pembagian Berakhir \n")        
# print(f"Program Berakhir")



# try:
#     with open("Belajar1/DasarPython2/data.txt", mode="r",) as file:
#         print(file.read())
# except:
#     print("File tidak ditemukan, membuat file baru!")
#     with open("Belajar1/DasarPython2/data.txt", mode="w", encoding="utf-8") as file:
#         file.write("New File\nDaftar Mahasiswa\n1. Desi\n2. Mia Azahra")


# print("Program Berakhir")



### Membuat Exception 

# def tambah(a:int, b:int)->int:
#     if not isinstance(a, Number) or not isinstance(b, Number):
#         raise "Inputan harus berupa Angka"
#     return a+b

# print(tambah(1,"3"))

# def bagi(a, b):
#     if b == 0:
#         raise ValueError("Pembagi tidak boleh nol!")
#     return a / b

# try:
#     print(bagi(10, 0))
# except ValueError as e:
#     print("Kesalahan:", e)




try:
    x = 10/1
except :
    print("Error konversi")
else: # else → dijalankan kalau tidak ada error.
    print("Berhasil, x ini berupa string =", x)
finally: # finally → dijalankan selalu, meskipun ada error.
    print("Program selesai")
