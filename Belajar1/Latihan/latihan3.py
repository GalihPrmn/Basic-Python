#Mengatur Tampilan Hasil Koding Python Di Terminal Supaya Lebih Bagus

dataNama = "Ari Zulham"
dataUmur = 19
dataTinggi = 179.2
dataNomorSepatu = 42

#String Standar
dataString = f"Nama = {dataNama}, Umur = {dataUmur}, Tinggi = {dataTinggi}, Sepatu = {dataNomorSepatu}"
print(7*"=" + "DATA STANDAR"+"="*7)
print(dataString)


#String MultiLine -> Menggunakan enter/new line \n
dataString = f"Nama = {dataNama},\nUmur = {dataUmur},\nTinggi = {dataTinggi},\nSepatu = {dataNomorSepatu}"
print("\n"+7*"=" + "DATA MULTILINE NewLine"+"="*7)
print(dataString)


#String MultiLine -> Kutip Triple
dataString = f"""
=========================================
        DATA MULTILINE TRIPLE
=========================================
Nama            : {dataNama:>10}
Umur            : {dataUmur:>4} tahun
Tinggi Badan    : {dataTinggi:>7.1f} cm
Nomor Sepatu    : {dataNomorSepatu:>10}
=========================================
"""
# print("\n"+7*"=" + "DATA MULTILINE Triple"+"="*7)
print(dataString)


