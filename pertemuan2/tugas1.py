#=============================================================================
# Praktikum 2: Tugas 2
# Tugas Hands-On : Stok Barang Kantin
#=============================================================================
# Tugas 2:
# Program membaca data stok barang dari file teks,
# menyimpannya ke dictionary, memproses data,
# dan menyimpan kembali ke file.
#=============================================================================

# nama file data
nama_file = "stok_barang.txt"

#=============================================================================
# Latihan 1 : Membaca Data dari File
#=============================================================================

def baca_data(nama_file):
    data_barang = {}  # dictionary kosong untuk menyimpan data

    with open(nama_file, "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip()  # menghilangkan karakter newline
            kode, nama, stok = baris.split(",")  # memisahkan data
            data_barang[kode] = {
                "nama": nama,
                "stok": int(stok)
            }

    return data_barang


#=============================================================================
# Latihan 2 : Menampilkan Semua Barang
#=============================================================================

def tampilkan_data(data_barang):
    print("\n========= DATA STOK BARANG KANTIN =========")
    print(f"{'Kode' : <10} | {'Nama Barang' : <15} | {'Stok' : >5}")
    print("-" * 40)

    for kode in sorted(data_barang.keys()):
        nama = data_barang[kode]["nama"]
        stok = data_barang[kode]["stok"]
        print(f"{kode : <10} | {nama : <15} | {stok : >5}")


#=============================================================================
# Latihan 3 : Mencari Barang Berdasarkan Kode
#=============================================================================

def cari_barang(data_barang):
    kode = input("Masukkan kode barang: ").strip()

    if kode in data_barang:
        print("\nBarang ditemukan")
        print(f"Kode Barang : {kode}")
        print(f"Nama Barang : {data_barang[kode]['nama']}")
        print(f"Stok        : {data_barang[kode]['stok']}")
    else:
        print("Barang tidak ditemukan")


#=============================================================================
# Latihan 4 : Menambah Barang Baru
#=============================================================================

def tambah_barang(data_barang):
    kode = input("Masukkan kode barang baru: ").strip()

    if kode in data_barang:
        print("Kode sudah digunakan")
        return

    nama = input("Masukkan nama barang: ").strip()

    try:
        stok = int(input("Masukkan stok awal: ").strip())
    except ValueError:
        print("Stok harus berupa angka")
        return

    if stok < 0:
        print("Stok tidak boleh negatif")
        return

    data_barang[kode] = {
        "nama": nama,
        "stok": stok
    }

    print("Barang berhasil ditambahkan")


#=============================================================================
# Latihan 5 : Update Stok Barang
#=============================================================================

def update_stok(data_barang):
    kode = input("Masukkan kode barang: ").strip()

    if kode not in data_barang:
        print("Barang tidak ditemukan")
        return

    print("1. Tambah Stok")
    print("2. Kurangi Stok")
    pilihan = input("Pilih menu: ").strip()

    try:
        jumlah = int(input("Masukkan jumlah stok: ").strip())
    except ValueError:
        print("Jumlah harus berupa angka")
        return

    if jumlah < 0:
        print("Jumlah tidak boleh negatif")
        return

    stok_sekarang = data_barang[kode]["stok"]

    if pilihan == "1":
        data_barang[kode]["stok"] += jumlah
        print("Stok berhasil ditambahkan")

    elif pilihan == "2":
        if stok_sekarang - jumlah < 0:
            print("Stok tidak boleh negatif")
        else:
            data_barang[kode]["stok"] -= jumlah
            print("Stok berhasil dikurangi")

    else:
        print("Pilihan tidak valid")


#=============================================================================
# Latihan 6 : Menyimpan Data ke File
#=============================================================================

def simpan_data(nama_file, data_barang):
    with open(nama_file, "w", encoding="utf-8") as file:
        for kode in data_barang:
            nama = data_barang[kode]["nama"]
            stok = data_barang[kode]["stok"]
            file.write(f"{kode},{nama},{stok}\n")

    print("Data berhasil disimpan ke file")

#=========================================
#Tampilan : Menu Stok Barang
#=========================================

#tampilan awal program ->  menampilkan menu

def main():
    #baca data file
    data_barang = baca_data(nama_file)
    
    while True:
        print("\n=== MENU STOK BARANG KANTIN ===")
        print("1. Tampilkan semua barang")
        print("2. Cari barang berdasarkan kode")
        print("3. Tambah barang baru")
        print("4. Update stok barang")
        print("5. Simpan ke file")
        print("0. Keluar")

        pilihan = input("pilih menu: ").strip()
        if pilihan == "1":
            tampilkan_data(data_barang)
            
        elif pilihan == "2":
            cari_barang(data_barang)

        elif pilihan == "3":
            tambah_barang(data_barang)
            
        elif pilihan == "4":
            update_stok(data_barang)
            
        elif pilihan == "5":
            simpan_data(nama_file, data_barang)
            
        elif pilihan == "0":
            print("program selesai")
            break
        
        else:
            print("pilihan tidak tersedia")
            
if __name__ == "__main__":
    main()