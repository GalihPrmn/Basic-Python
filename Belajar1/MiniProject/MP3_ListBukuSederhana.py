# LATIHAN LIST
# Membuat Program List Buku

list_buku = []

while True:
    print("\nMasukan Data Buku")
    judul = str(input("Nama Buku \t: "))
    penulis = str(input("Nama Penulis \t: "))

    buku_baru = [judul, penulis]
    list_buku.append(buku_baru)

    print("\n\n", "="*10, "Data Buku", "="*10)
    for index,buku in enumerate(list_buku):
        print(f"{index+1} | {buku[0]} | {buku[1]}")

    print("\n\n","="*31)
    isLanjut = input("Lanjutkan? (y/n) ")

    if isLanjut == "n":
        break
    
# Hapus buku (CHAT GPT)
isHapus = input("Mau Hapus Buku Gak? (y/n) ").lower()
if isHapus == "y":
    while True:
        print("\n", "="*10, "Data Buku", "="*10)
        for index, buku in enumerate(list_buku):
            print(f"{index+1} | {buku[0]} | {buku[1]}")

        try:
            noHapus = int(input("\nMasukkan nomor buku yang mau dihapus: "))
            if 1 <= noHapus <= len(list_buku):
                buku_dihapus = list_buku.pop(noHapus - 1)
                print(f"Buku '{buku_dihapus[0]}' berhasil dihapus!")
                for index, buku in enumerate(list_buku):
                    print(f"{index+1} | {buku[0]} | {buku[1]}")
            else:
                print("Nomor buku tidak valid!")
        except ValueError:
            print("Masukkan angka yang benar!")

        if not list_buku:
            print("Semua buku sudah dihapus!")
            break

        isLanjutHapus = input("Hapus lagi? (y/n) ").lower()
        if isLanjutHapus == "n":
            break

print("Program Selesai!!!")