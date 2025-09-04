# 1. Mode Write 

# -> Akan membuat file baru jika tidak ada
# -> lalu akan menimpa atau overwrite isinya (isi sebelum nya di hapus dulu)

with open("Belajar1/DasarPython2/data.txt", mode="w", encoding="utf-8") as file:
    file.write("Mia Zahra\nSilvia\nDesi\n")


# 2. Mode Append

with open("Belajar1/DasarPython2/data.txt", mode="a", encoding="utf-8") as file:
    file.write("===Penambahan dengan Append===\n")
    file.write("Dina\n")
    file.write("Amelia\n")


# 3. Mode r+ 

# -> Menimpa isi text sesuai dengan panjang data yang diisi

with open("Belajar1/DasarPython2/data.txt", mode="r+", encoding="utf-8") as file:
    file.write("Lya") # Akan menimpa mia di baris 7



'''
| Mode   | Keterangan                                                      |
| ------ | --------------------------------------------------------------- |
| `"w"`  | Write → menulis file baru, kalau ada file lama akan **ditimpa** |
| `"a"`  | Append → menambah di akhir file, tidak menimpa                  |
| `"x"`  | Exclusive creation → membuat file baru, kalau sudah ada → error |
| `"w+"` | Write + Read                                                    |
| `"a+"` | Append + Read                                                   |
| `"r+"` | Read + Write (tanpa hapus isi file)                             |

'''