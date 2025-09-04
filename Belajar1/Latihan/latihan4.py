# Latihan Loop/Perulangan

# Membuat Segitiga

sisi = 9

# dummy variable
count = 1
# for i in range(sisi):
#     print("*"*count)
#     count += 1

# while True:
#     print("*"*count)
#     count += 1
#     if count > sisi:
#         break



# while True:
#     if count % 2:
#         # print jika ganjil
#         print("*"*count)
#         count += 1
#     else:
#         # akan kembali ke atas jika genap
#         count += 1
#         continue

#         # akan break jika count melebihi sisi 
#     if count > sisi:
#         break


# spasi = int(sisi/2)
# while True:
#     if count % 2:
#         # print jika ganjil
#         print(" "*spasi, "+"*count)
#         count += 1
#         spasi -= 1
#     else:
#         # akan kembali ke atas jika genap
#         count += 1
#         continue

#         # akan break jika count melebihi sisi 
#     if count > sisi:
#         break

# sisi = 9  # Harus bilangan ganjil
# for count in range(1, sisi + 1, 2):
#     spasi = (sisi - count) // 2
#     print(" " * spasi + "+" * count)



for i in range(1, sisi + 1, 2): # → menghasilkan: 1, 3, 5, 7, 9
    spasi = (sisi - i) // 2 # → agar teks tetap di tengah
    print(" "*spasi + "+" * i)

for i in range(sisi - 2, 0, -2): #  → menghasilkan: 7, 5, 3, 1
    spasi = (sisi - i) // 2 
    print(" "*spasi + "+" * i) 
