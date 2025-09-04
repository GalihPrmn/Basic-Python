# Program Daftar Kontak Sederhana

def tampilkan_menu():
    print("\n===== MENU KONTAK =====")
    print("1. Tambah Kontak")
    print("2. Hapus Kontak")
    print("3. Cari Kontak")
    print("4. Tampilkan Semua Kontak")
    print("5. Keluar")

# Dictionary untuk menyimpan kontak
kontak = {}

while True:
    tampilkan_menu()
    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":  # Tambah kontak
        nama = input("Masukkan nama: ")
        nomor = input("Masukkan nomor HP: ")
        kontak[nama] = nomor
        print(f"Kontak {nama} berhasil ditambahkan!")

    elif pilihan == "2":  # Hapus kontak
        nama = input("Masukkan nama yang ingin dihapus: ")
        if nama in kontak:
            del kontak[nama]
            print(f"Kontak {nama} berhasil dihapus!")
        else:
            print("Kontak tidak ditemukan!")

    elif pilihan == "3":  # Cari kontak
        nama = input("Masukkan nama yang dicari: ")
        if nama in kontak:
            print(f"{nama} : {kontak[nama]}")
        else:
            print("Kontak tidak ditemukan!")

    elif pilihan == "4":  # Tampilkan semua kontak
        if len(kontak) == 0:
            print("Belum ada kontak.")
        else:
            print("\nDaftar Kontak:")
            for nama, nomor in kontak.items():
                print(f"{nama} : {nomor}")

    elif pilihan == "5":  # Keluar
        print("Program selesai. Terima kasih!")
        break

    else:
        print("Pilihan tidak valid, coba lagi.")
