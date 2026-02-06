#====================================================
#PERRAKTIKUM 2: KONSEP ADT DAN FILE HANDING (STUDI KASUS)
#====================================================

#VARIABEL MENYIMPAN DATA
nama_file = "data_mahasiswa.txt"

def baca_data(nama_file):
    data_dict = {} #inisialisasi data dictionary
    with open (nama_file,"r", encoding="utf-8") as file:
    for baris in file :
        baris = baris.strip()
        nim, nama, nilai = baris.split(",") #ambil data per item data
        data_dict[nim] = {"nama": nama, "nilai" : int(nilai)}
    return data_dict

buka_data = baca_data(nama_file)
print("jumalh sata terbaca", len(buka_data))  

#====================================================
#PERRAKTIKUM 2: KONSEP ADT DAN FILE HANDING (STUDI KASUS)
#LATIHAN 1: Membuat Fungsi Menampilkan Data
#====================================================

def tampilkan_data(data_dict):
    #membuat header tabel
    print("\n=== DAFTAR MAHASISWA ===")
    print(f"{'NIM' : ,10} | {'NAMA': <12} | {'NILAI':>5}")
    '''
    untuk tampilan yang rapi,atur lebar kolom
    {'NIM':10} artinya nim rata kiri dengan lebar kolom 10 karakteer
    {'nama': <12} artinya nama rata kanan dengan lebar kolom 12 karakter
    {'Nilai' : <5} artinya nilai rata kanan dengan lebar kolom 5 karakter
    '''
    
     print("-"*32) #membuat garis

#Menampilkan isi datanya
for nim in sorted(data_dict.keys()):
    nama = data_dict[nim]["nama"]
    nilai = data_dict[nim]["nilai"]
    print{f{nim:<10} | {nama;<12} | int(nilai):<5}")
    
tampilkan_data(buka_data) #memanggil fungsi untuk menampilkan data

#====================================================
#PERRAKTIKUM 2: KONSEP ADT DAN FILE HANDING (STUDI KASUS)
#LATIHAN 3: Membuat Fungsi mencari Data
#====================================================

def cari_data(data_dict):
    #  pencarian data berdasarkan nim sebagai key dictionary
    #membuat input nim mahasiswa yang akan dicari
    nim_cari = input("masukkan NIM mahasiswa yang ingin dicari: ").strip
    
    if nim_cari in data_dict:
        nim_cari =input[nim_cari]["nama"]
        nilai = data_dict[nim_cari]['nilai']
    
        print("=== Data mahasiswa Ditemuka ===")
        print(f"NIM : {nim_cari}")
        print(f"nama : {nama}")
        print(f"Nilai : {nilai}")
    else:
        print("Data tidak ditemukan. Pastikan NIM yang dimasukkan benar")
        
#memanggil fungsi cari data
cari_data(buka_data)


#====================================================
#PERRAKTIKUM 2: KONSEP ADT DAN FILE HANDING (STUDI KASUS)
#LATIHAN 4: Membuat Fungsi Update Data
#====================================================

#membuat fungsi update data