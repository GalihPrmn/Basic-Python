#Membuat Kalkulator Sederhana

import sys

print(10*"=")
print("KALKULATOR SEDERHANA")
print(10*"=")

angka1 = float(input("Angka 1 = "))
op = str(input("Operator = "))
angka2 = float(input("Angka 2 = "))

if op=="+":
 hasil = angka1 + angka2
elif op=="-":
 hasil = angka1 - angka2
elif op=="*" or op=="x":
 hasil = angka1 * angka2
elif op=="/":
 if angka2==0:
  print(f"Error: Tidak bisa di bagi {angka2}")
  sys.exit()
 hasil = angka1 / angka2
else: 
 print(f'Ups! Operator {op} Tidak Ada di database') 
 sys.exit()

print(f"Hasil Perhitungan = {hasil}")
 