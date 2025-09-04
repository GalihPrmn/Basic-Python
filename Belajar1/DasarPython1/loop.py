#Perulangan (Loop)

# FOR

# angka2 = [0,2,4,6,8,10] #Ini List, Kayak Array

# for i in angka2: #Di Loop Berdasarkan Index
#     print(f"i sekarang -> {i}")


# for i in range(1):
#     print(i)

# Jika range(x) nya 1 angka -> akan menjalankan berdasarkan index(mulai dari 0)
# jika range(x, y) nya 2 angka -> dijalankan berdasarkan angka x, diakhiri dengan y dikurang 1 
# jika range(x, y, z) nya 3 angka -> sama kayak 2, tapi langkahnya berdasarkan z (contoh z = 2, maka hasilnya akan ditambah 2)

# dataHu = "Anak Anak Himaksi"

# for i in range(10):
#     print(dataHu)


### WHILE LOOP

# while kondisi:
#     aksi ini
#     aksi untuk mengubah kondisi ->bisa juga dibalik

# i = 1

# while i <= 10:
#     i += 1
#     print(f"Angka Ke -> {i}")

# print("Akhir Program")

#======================================================================================


### Continue, Pass and Break


#Pass
# angka = 0
# while angka < 5:
#     print(f"Walawe -> {angka}")
#     if angka == 3:
#         pass # Ini Adalah data dummy, tidak akan dieksekusi (mungkin cuman buat inisialisasi) -> bisa juga di function/class
#     angka += 1


#Continue
# angka = 0
# while angka < 5:
#     angka += 1
#     print(f"Angka Sekarang -> {angka}")

#     if angka == 3:
#         print("Nice!!!!!!")
#         continue #Akan membuat loop loncat ke awal lagi, tidak akan ngeksekusi coding di bawah
    
#     print("===LOL===") #ini akan ke skip jika ada continue
# print("Finish!!")



#Break
dataInt = int(input("Mau Berhitung Sampai Mana? "))
angka = 0
while True:
    angka += 1
    print(f"Angka Sekarang -> {angka}")

    if angka == dataInt:
        print("Nice!")
        break # Akan membuat loop berhenti, 
    print("==LOL===")

print("Finish!!")