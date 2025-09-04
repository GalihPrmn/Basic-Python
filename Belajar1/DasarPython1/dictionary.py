data = {
    "nama" : "Ari Zulham",
    "kelas" : "Akuntansi A",
    "nilai" : 99
}

# Panjang Dictionary ~~~~~~~~~~~~~~~~~
# LENDICT = len(data)
# print(LENDICT)

# Cek key ada atau tidak ~~~~~~~~~~~~~~~``
# KEY = "nilai"
# cekKey = KEY in data
# print(cekKey)

# Ambil Data ~~~~~~~~~~~~~~~~
# print(data.get('nama'))
# print(data.get('nim', 'Key Tidak Ditemukan')) #-> Hasilnya None, Karena key tidak ada di dalam dictionary, kalo cara biasa akan error

# Update Data~~~~~~~~~~~~
data.update({'nama':'Dimas'}) # Jika key sudah ada, maka akan di update
data.update({'nim':'4122424120019'}) # jika ket tidak ada, maka akan di tambah
# print(data)

# Delete Data~~~~~~~~~~~~~~~~~~
# del data['nama']
# print(data)


# LOOPING DICTIONARY~~~~~~~~~~~~~~~~~~~
#Operator untuk Mengambil Item / Iterables
# for i in data.keys(): #-> mengambil Key
#     print(data.get(i))
# print("!!!!!!!!!!!!!!!")
# for man in data.values(): #-> mengambil value
#     print(man)
# print("!!!!!!!!!!!!!!!")
# for wom in data.items(): #-> mengambil key and value
#     print(wom)
    
# for key,value in data.items():
#     print(f"Key = {key}, Value = {value }")



# NESTING DICTIONARY ~~~~~~~~~~~~~~~~~~~~~
import datetime as dt
Mahasiswa1 = {
    'nama' : "Dimas Alkahfi",
    'nim' : "2212212211",
    'sks_lulus' : 120,
    'beasiswa' : False,
    'lahir' : dt.datetime(2000, 10, 10),
    'lainnya' : {
        'alamat' : 'Garut',
        'nama_ayah' : 'Indom',
        'nama_ibu' : 'Lily',
        'No_telp' : '99288302832'
    }
}
Mahasiswa2 = {
    'nama' : "Adit Riyawan",
    'nim' : "9828827732",
    'sks_lulus' : 133,
    'beasiswa' : True,
    'lahir' : dt.datetime(2002, 9, 10),
    'lainnya' : {
        'alamat' : 'Garut',
        'nama_ayah' : 'Aknam',
        'nama_ibu' : 'Mili',
        'No_telp' : '992772321'
    }
}

dataMahasiswa = {
    'MAH01' : Mahasiswa1,
    'MAH02' : Mahasiswa2,
}

print(f"{'KEY':<5} {'Nama':<15} {'NIM':<10} {'SKS':<5} {'Beasiswa':<9} {'Lahir':<10}")
print(f"="*57)

for mhs in dataMahasiswa:
    KEY = mhs

    NAMA = dataMahasiswa[KEY]['nama']
    NIM = dataMahasiswa[KEY]['nim']
    SKS = dataMahasiswa[KEY]['sks_lulus']
    BEASISWA = dataMahasiswa[KEY]['beasiswa']
    LAHIR = dataMahasiswa[KEY]['lahir'].strftime('%x')
     
    print(f"{KEY:<5} {NAMA:<15} {NIM:<10} {SKS:<5} {BEASISWA:^9} {LAHIR:<10}")