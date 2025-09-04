# Membaca File Eksternal

print("\n", 3*"=", " Membaca File .txt ", 3*"=")

fileData = open("Belajar1/DasarPython2/data.txt", mode="r")

print(f"Status Read = {fileData.readable()}")
print(f"Status Write = {fileData.writable()} \n")

### Baca Seluruh File
print(fileData.read())

### Baca Baris Per Baris
# print(fileData.readline(), end="") # | Baris Pertama
# print(fileData.readline(), end="") # | Baris Kedua


### Baca Semua Baris sebagai List
# print(fileData.readlines()) # | Hasilnya List


### Harus di Close
# print(f"Apakah File sudah Di Close = {fileData.closed}") # Belum ditutup/false
fileData.close()
# print(f"Apakah File sudah Di Close = {fileData.closed}") # sudah ditutup/true



### Salah satu teknik membuka file di Pyhton
print("\n", 3*"=", " Membaca File .txt dengan with", 3*"=")
with open("Belajar1/DasarPython2/data.txt", mode="r") as file:
    content = file.readline()
    print(content, end="")
    print(f"Apakah File sudah Di Close = {file.closed}") # Belum ditutup/false
    
print(f"Apakah File sudah Di Close = {file.closed}") # Sudah ditutup/true
