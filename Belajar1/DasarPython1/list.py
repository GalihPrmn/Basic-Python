# --- LIST ---

data = [1, 2, True, False, "Galih", "Python", 3.14, 2.71]

# dataRange = range(0, 10, 2) #range(start, stop, step)
# dataList = list(dataRange)
# print(dataList)

# # Membuat List dengan for loop, list comprehension
# dataListFor = [i for i in range(1, 10, 2)]
# print(dataListFor)

# # Membuat List dengan For If
# dataListForIf = [i for i in range(0, 10) if i not in dataListFor]
# print(dataListForIf)

# dataListForIf = [i for i in range(0, 10) if i%2 == 1] # 1 = Ganjil, 0 = Genap
# print(dataListForIf)

# NewData = ["Fitri", "Andiva", 1925, False]

#MANIPULASI ~~~~~~~~~~~~~~~~~~~~~~~
# print(f"Data Pertama adalah {data[0]}, dan data terakhir adalah {data[-1]}, panjangnya {len(data)}")
# data.extend(NewData)
# data.remove("Andiva")
# print(data)

dataAngka = [1,2,2,2,3,7,8,9,7,5,4,56,7,5,4,2,3,4]

#OPERASI ~~~~~~~~~~~~~~~~~~~~~~~
# dataAngka.sort()
# dataAngka.reverse()
# print(f"Angka = {dataAngka}")


#COPY LIST ~~~~~~~~~~~~~~~~~~~~~~~
# a = ["Galih", "Dimas", "Adit"]
# b = a

# b.append("Zahra") # List a juga akan ke ubah,

# print(f"Data a = {a}") 
# print(f"Data b = {b}")

# c = a.copy() # jika dibuah, tidak akan berpengaruh ke list lain
# c.append("Faisal")
# print(f"Data c = {c}")


#NESTED LIST ~~~~~~~~~~~~~~~~~~~~~~~~~~
# data1 = [1,2]
# data2 = [3,4]
# dataCopy = [data1, data2]

# dataCopyPertama = dataCopy.copy() # Jika kita rubah di data1/data2, maka akan merubah ini juga (deep copy di nested list)

# from copy import deepcopy
# dataCopyKedua = deepcopy(dataCopy) # pengganti .copy() di nested list

dataBersarang = [
    ["Galih", 18, "Membaca"],
    ["Dimas", 19, "Main Game"],
    ["Ari", 20, "Olahraga"]
]

# print(f"Data Mahasiswa")

# for mahasiswa in dataBersarang:
#     print(f"""
# Nama : {mahasiswa[0]}
# Umur : {mahasiswa[1]}
# Hobi : {mahasiswa[2]}
# """)
    

#LOOPING LIST ~~~~~~~~~~~~~~~~~~~~

dataAngka.sort()
# for var in list
for angka in dataAngka: pass
    # print(f"Data Nya -> {angka}")

# For loop dengan range
panjang = len(dataAngka)
for i in range(panjang): pass
    # print(f"Angka Ke -> {dataAngka[i]}")

#while loop
dataAngka.reverse()
# panjang = len(dataAngka)
# i = 0
# while i < panjang:
#     print(f"Angka Ke -> {dataAngka[i]}")
#     i += 1

#List Comprehension
[print(f"Data Random Nya = {i}") for i in data]

#Enumerate
for index, data in enumerate(data):
    print(f"Index-{index}, Data = {data}")


    