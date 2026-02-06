#=============================================================================
# Praktikum 2 : Konsep ADT dan File Handling (Studi Kasus) 
# Latihan 1   : Membuat Fungsi Load Data
#=============================================================================

#variabel menyimpan data file
nama_file = "data_mahasiswa.txt"

def baca_data(nama_file):
    data_dict = {} #inisialisasu data dictionary kosong
    with open(nama_file, "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip() #ambil data per baris dan hilangkan new line
            nim, nama, nilai = baris.split(",") #ambil data per item data
            data_dict[nim] = {"nama": nama, "nilai": int(nilai)} #masukan dalam dictionary
    return data_dict

#buka_data = baca_data(nama_file) #memanggil dungsi load data dan menyimpannya dalam variabel
#print("Jumlah data terbaca", len(buka_data)) #melihat berapa data yang di load 

#=============================================================================
# Praktikum 2 : Konsep ADT dan File Handling (Studi Kasus) 
# Latihan   2 : Membuat Fungsi Menampilkan Data
#=============================================================================

def tampilkan_data(data_dict):
    #membuat header tabel
    print("\n========= DAFTAR MAHASISWA =========")
    print(f"{'NIM' : <10} | {'Nama' : <12} | {'Nilai' : >5}")
    '''
    untuk tampilan yang rapi, 
    {'NIM' : <10} artinya rata kiri dengan lebar 10 karakter
    {'Nama' : <12} artinya rata kiri dengan lebar 12 karakter
    {'Nilai' : >5} artinya rata kanan dengan lebar 5 karakter
    '''
    print("-" * 36) #membuat garis

    #menampilkan isi datanya
    for nim in sorted(data_dict.keys()): #mengurutkan data berdasarkan NIM
        nama = data_dict[nim]["nama"]
        nilai = data_dict[nim]["nilai"]
        print(f"{nim : <10} | {nama : <12} | {int(nilai) : >5}")

#tampilkan_data(buka_data) #memanggil fungsi untuk menampilkan data

#=============================================================================
# Praktikum 2 : Konsep ADT dan File Handling (Studi Kasus)
# Latihan   3 : Membuat Fungsi Mencari Data
#=============================================================================

#membuat fungsi pencarian dara
def cari_data(data_dict):
    #pencarian data berdasarkan NIM sebagai key dictionary
    #membuat input NIM Mahasiswa yang akan dicari
    nim_cari = input("Masukan NIM Mahasiswa yang ingin dicari: ")

    if nim_cari in data_dict:
        nama = data_dict[nim_cari]["nama"]
        nilai = data_dict[nim_cari]["nilai"]
        
        print("======= Data Mahasiswa Ditemukan ========")
        print(f"NIM     : {nim_cari}")
        print(f"Nama    : {nama}")
        print(f"Nilai   : {nilai}")
    else:
        print("Data tidak ditemukan. Pastikan NIM yang dimasukan benar.")

#memanggil fungsi cari data
#cari_data(buka_data)

#=============================================================================
# Praktikum 2 : Konsep ADT dan File Handling (Studi Kasus)
# Latihan   4 : Membuat Fungsi Update Data
#=============================================================================

#membuat fungsi update data
def update_data(data_dict):

    #awali dulu dengan mencari NIM / data mahasiswa yang ingin di update
    nim = input("Masukan NIM Mahasiswa yang ingin diubah datanya: ").strip()

    if nim not in data_dict:
        print("NIM tidak ditemukan. Proses update dibatalkan.")
        return
    
    try:
        nilai_baru = int(input("Masukan nilai baru 0-100 : ").strip())
    except ValueError:
        print("Nilai harus berupa angka. Proses update dibatalkan.")
        return

    if nilai_baru < 0 or nilai_baru > 100:
        print("Nilai harus antara 0-100. Proses update dibatalkan.")
        return

    nilai_lama = data_dict[nim]["nilai"]
    data_dict[nim]["nilai"] = nilai_baru

    print(f"Update berhasil. Nilai {nim} berubah dari {nilai_lama} menjadi {nilai_baru}.")

#update_data(buka_data)

#=============================================================================
# Praktikum 2 : Konsep ADT dan File Handling (Studi Kasus)
# Latihan   5 : Membuat Fungsi Menyimpan Data pada File
#=============================================================================

#membuat fungsi menyimpan data ke file
def simpan_data(nama_file, data_dict):
    with open(nama_file, "w", encoding="utf-8") as file:
        for nim in sorted(data_dict):
            nama = data_dict[nim]["nama"]
            nilai = data_dict[nim]["nilai"]
            file.write(f"{nim},{nama},{nilai}\n")

#memanggil fungsi simpan data
#simpan_data(nama_file, buka_data)    
#print("\nData berhasil disimpan ke file: ", nama_file)


#=============================================================================
# Praktikum 2 : Konsep ADT dan File Handling (Studi Kasus)
# Latihan   6 : Membuat Menu
#=============================================================================

def main():
    nama_file = "data_mahasiswa.txt"
    buka_data = baca_data(nama_file)

    while True:
        print("\n===== MENU DATA MAHASISWA =====")
        print("1. Tampilkan Data Mahasiswa")
        print("2. Cari Data Berdasarkan NIM")
        print("3. Ubah Nilai Mahasiswa")
        print("4. Simpan Data ke File")
        print("0. Keluar")
        
        pilihan = input("Pilih Menu : ").strip()

        if pilihan == "1":
            tampilkan_data(buka_data) #memanggil fs 2 menampilkan data

        elif pilihan == "2":
            cari_data(buka_data) #memanggil fs 3 mencari data

        elif pilihan == "3":
            update_data(buka_data) #memanggil fs 4 mengubah data

        elif pilihan == "4":
            simpan_data(nama_file, buka_data) #memanggil fs 5 menyimpan data ke file
            print("Data berhasil disimpan.")

        elif pilihan == "0":
            print("Keluar dari program.")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
            
if __name__ == "__main__":
    main()
exit()