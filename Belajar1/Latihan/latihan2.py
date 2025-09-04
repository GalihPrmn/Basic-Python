#Latihan logika dan komparasi

#Membuat gabungan area rentang dari angka

#+++++3---------10+++++

# inputUser = float(input("Masukan angka kurang dari 3\n ATAU \n lebih dari 10\n :"))

# ++++++3-------------
# isKurangDari = inputUser < 3
# print("Kurang dari 3 =",isKurangDari)

# -------10++++++++++++
# isLebihDari = inputUser > 10
# print("Lebih Dari 10 =",isLebihDari)

#+++++3---------10+++++
# isHasil = isKurangDari or isLebihDari
# print("Angka yang anda masukan =", isHasil)

###Kasus Irisan
#-----3+++++++++10-------

# inputUser1 = float(input("Masukan angka lebih dari 3\n DAN \n kurang dari 10\n :"))

# #-----3++++++++++
# isLebihDari = inputUser1 > 3
# print("Lebih Dari 3 =",isLebihDari)

# #+++++10----------
# isKurangDari = inputUser1 < 10
# print("Kurang dari 10 =",isKurangDari)

# #-----3+++++++++10-------
# isHasil = isKurangDari and isLebihDari
# print("Angka yang anda masukan =", isHasil)


###LATIHAN MANDIRI

#Soal 1 = -----0+++++5-----8+++++11-----

# inputUser = float(input("Masukan angka lebih dari 0\natau\nkurang dari 5\natau\nlebih dari 8\natau\nkurang dari 11\n:"))

# isLebihDari0    = inputUser > 0
# isKurangDari5   = inputUser < 5
# isLebihDari8    = inputUser > 8
# isKurangDari11  = inputUser < 11

# isHasil = (isLebihDari0 and isKurangDari5) or (isLebihDari8 and isKurangDari11)
# print(isHasil) 

#soal 2 +++++0-----5+++++8-----11+++++

# inputUser = float(input("Masukan angka kurang dari 0\natau\nlebih dari 5\natau\nkurang dari 8\natau\nlebih dari 11\n:"))

# isKurangDari0    = inputUser < 0
# isLebihDari5   = inputUser > 5
# isKurangDari8    = inputUser < 8
# isLebihDari11  = inputUser > 11

# isHasil = (isKurangDari0 or isLebihDari5) and (isKurangDari8 or isLebihDari11)
# print(isHasil)



###Cara Ringkas ala Matematis (Diambil Di Komen YT)

x = float(input('Masukan Angka\n:'))

#Soal 1 = -----0+++++5-----8+++++11-----
y = 0 < x < 5 or 8 < x < 11
# jika 0 kurang dari x, jika x kurang dari 5  ->true
# jika 8 kurang dari x, jika x kurang dari 11 ->true
print(y)


#Soal 2 +++++0-----5+++++8-----11+++++
y2 = 0 > x or 5 < x < 8 or x > 11
# jika x kurang dari 0
# jika 5 kurang dari x, jika x kurang dari 8
# jika x lebih dari 11
print(y2)   


#sendiri -------10+++++-5------0++++++3------8+++++10------

y3 = -10 < x < -5 or 0 < x < 3 or 8 < x < 10
print(y3)