import os

def header():
    os.system('clear')

    print(f"{'DAFTAR MAHASISWA':^40}", end="")
    print(f"{'BESERTA BERKAS BERKASNYA':^40}", end="")
    print(f"{'='*40:^40}")

def tampilkan_menu():
    os.system('clear')
    print("\n===== MENU KONTAK =====")
    print("1. Tambah Kontak")
    print("2. Hapus Kontak")
    print("3. Cari Kontak")
    print("4. Tampilkan Semua Kontak")
    print("5. Keluar")


# Kenapa? 
'''Membedakan script utama dan modul
-> Kalau file dijalankan langsung → bagian di dalam if __name__ == "__main__": akan dieksekusi.
-> Kalau file di-import ke file lain → bagian itu tidak dieksekusi.
➝ Jadi kode tetap rapi, tidak bikin efek samping saat di-import.'''

'''Bisa Juga di dalam folder package dibuat file __main__
-> ini akan di eksekusi saat dijalankan pake terminal (kayak dokumentasi nya lah)'''

if __name__ == "__main__":
    header()
    print(f"Ini Adalah Templating nya ~~~~")
