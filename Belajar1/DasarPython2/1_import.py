'''Import -> Mengambil Program dari file external'''
'''Module -> Satu File Python yang berisi function, variable, class'''
'''Package -> Kumpulan dari beberapa module dalam sebuah folder.'''
'''_pychace__ Berguna untuk waktu eksekusi dari import (jadi import nya ke pychace karena sudah bahasa mesin)'''

# from pkg import * # Harus Pake __all__ di ini nya (Gak disarankan)
import pkg

# import pkg.template as tmp

# # Menggunakan From (lebih anggun)
# from pkg.matematika  import tambah, pangkat #-> mengambil beberapa 
# from pkg.matematika import * # -> Mengambil semua isi nya
# from pkg import matematika # -> Ini juga Bisa (ngambil 1 module dalam package nya)

pkg.template.header()

hasil_tambah = pkg.matematika.basic.tambah(2,2,2,2,2)
hasilPangkat2 = pkg.matematika.scientific.pangkat(2)
hasilKali = pkg.matematika.basic.kali(5,5)
print(f"Hasil Tambah = {hasil_tambah}\nHasil Pangkat = {hasilPangkat2(10)}\nHasil Kali = {hasilKali}")


