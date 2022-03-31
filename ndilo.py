import sys


def menu() :
    print("Pilih program yang akan dijalankan:")
    print("1. Konversi Suhu")
    print("2. Bilangan Terbesar")
    print("3. Bilangan Terkecil")
    print("4. Konversi Jarak")
    print("5. Keluar")
    try:
        program = int(input("Masukkan pilihan anda: "))
    except ValueError:
        print("Masukkan pilihan yang benar!")
        menu()
    if program == 1:
        konversiSuhu()
        wantExit()
    elif program == 2:
        bilanganTerbesar()
        wantExit()
    elif program == 3:
        bilanganTerkecil()
        wantExit()
    elif program == 4:
        konversiJarak()
        wantExit()
    elif program == 5:
        wantExit()
    else:
        print("Masukkan pilihan yang benar!")
        menu()
def konversiSuhu() :
    try:
        suhu = float(input("Masukkan nilai temperatur: "))
    except ValueError:
        print("Masukkan nilai yang benar!")
        konversiSuhu()
        return
    satuan = input("Celcius atau Fahrenheit? (C/F): ")
    if satuan == "C":
        print("Nilai suhu dalam Fahrenheit: ", suhu * 9/5 + 32)
    elif satuan == "F":
        print("Nilai suhu dalam Celcius: ", (suhu - 32) * 5/9)
    else:
        print("Masukkan satuan yang benar!")
def bilanganTerbesar() :
    try:
        a = int(input("Masukkan nilai a: "))
        b = int(input("Masukkan nilai b: "))
        c = int(input("Masukkan nilai c: "))
    except ValueError:
        print("Masukkan nilai yang benar!")
        bilanganTerbesar()
        return
    if a >= b and a >= c:
        print("Nilai terbesar adalah: ", a)
    elif b >= a and b >= c:
        print("Nilai terbesar adalah: ", b)
    else:
        print("Nilai terbesar adalah: ", c)
def bilanganTerkecil() :
    try:
        a = int(input("Masukkan nilai a: "))
        b = int(input("Masukkan nilai b: "))
        c = int(input("Masukkan nilai c: "))
    except ValueError:
        print("Masukkan nilai yang benar!")
        bilanganTerkecil()
        return
    if a <= b and a <= c:
        print("Nilai terkecil adalah: ", a)
    elif b <= a and b <= c:
        print("Nilai terkecil adalah: ", b)
    else:
        print("Nilai terkecil adalah: ", c)
def konversiJarak() :
    try:
        jarak = float(input("Masukkan jarak: "))
    except ValueError:
        print("Masukkan nilai yang benar!")
        konversiJarak()
        return
    satuan = input("Km atau M? (K/M): ")
    if satuan == "K":
        print("Jarak dalam M: ", jarak * 1000)
    elif satuan == "M":
        print("Jarak dalam Km: ", jarak / 1000)
    else:
        print("Masukkan satuan yang benar!")
def wantExit() :
    ex = input("Apakah anda ingin keluar? (Y/N): ")
    if ex == "Y":
        print("Terima kasih telah menggunakan program ini!")
        sys.exit()
    elif ex == "N":
        menu()
    else:
        print("Masukkan pilihan yang benar!")
        wantExit()
menu()