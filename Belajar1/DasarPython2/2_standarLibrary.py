import datetime as dt

dataWaktu = dt.datetime.now()

print(f"Now  = {dataWaktu}")
print(f"Year = {dataWaktu.year}")
print(f"Hari = {dataWaktu.strftime('%A')}")


from collections import Counter

dataPenjualan = ["A", "B", "c", "A", "A"]

juamlahAngka = dataPenjualan.count("A")
dataCount = Counter(dataPenjualan)
print(f"Count = {juamlahAngka}\nCounter = {dataCount}")


import io

# bukaFile = io.open("Belajar1/DasarPython1/Materi_txt/Materi.txt", "r")
# print(bukaFile.read())

import pkg