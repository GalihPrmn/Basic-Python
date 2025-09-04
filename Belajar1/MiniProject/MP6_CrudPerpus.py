import os
import CRUD as CRUD

if __name__ == "__main__":

    sistemOperasi = os.name


    match sistemOperasi:
        case 'posix': os.system('clear')
        case 'nt' : os.system('cls')


    print(f"{'SELAMAT DATANG DI PROGRAM':^40}")
    print(f"{'DATABASE PERPUSTAKAAN':^40}")
    print("="*40 , "\n")


    ## Cek apakah database nya ada atau tidak
    CRUD.init_console()



    while True:
        match sistemOperasi:
            case 'posix': os.system('clear')
            case 'nt' : os.system('cls')


        print(f"{'SELAMAT DATANG DI PROGRAM':^40}")
        print(f"{'DATABASE PERPUSTAKAAN':^40}")
        print("="*40 , "\n")

        print(f"1. Read Data")
        print(f"2. Create Data")
        print(f"3. Update Data")
        print(f"4. Delete Data\n")

        userOpt = input("Masukan Opsi : ")



        match userOpt:
            case "1" : CRUD.read_console()
            case "2" : CRUD.create_console()
            case "3" : CRUD.update_console()
            case "4" : CRUD.delete_console()
            case _: print("Error : Masukan Opsi Yang Sudah Ada!!")


        isLanjut = input("Mau Lanjut Kelola Perpustakaannya (y/n) ? ")
        if isLanjut.lower() == 'n':
            break

    print("Program Selesai!!!")