import random

welcome_message = "SELAMAT DATANG DI PROGRAM TIDAK JELAS SAYA"
hadiah_position = random.randint(0 , 4)

print("==========================")
print(f"==== {welcome_message} ====")
print("==========================")

name_user = input("Masukkan nama Anda: ")
print(f'''
    Halo {name_user}, pilih angka untuk mendapatkan hadiah
    |1| |2| |3| |4|
''')

print("Menurut kamu ada di nomor berapa? [1 / 2 / 3 / 4]")
pilihan = int(input("Pilihan Angkamu: "))

konfirmasi = input("Apakah Anda yakin dengan jawaban Anda? (Y/n): ")
if konfirmasi.lower() == "n":
    print("Terima Kasih")
    exit()
elif konfirmasi.lower() == "y":

    if pilihan == hadiah_position:
        print("Selamat Kamu Mendapatkan Hadiah 2 Juta Rupiah")
    else:
        print("Maaf, kamu tidak mendapatkan hadiahnya")
else:
    print("Input tidak valid. Program berakhir.")
