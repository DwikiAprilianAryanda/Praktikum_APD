# def salam():
#     print('Selamat datang mahasiswa baru 2024')
    
# salam()



# def salam(salam):
#     print(salam)
  
# iso = 'salam iso'  
# salam(iso)


# sisi = 2
# luas = sisi * sisi

# def luas_persegi(sisi):
#     luas = sisi * sisi 
#     return luas

# print(luas_persegi(3))
# print(luas)




# def luas_persegi(sisi):
#     luas = sisi * sisi 
#     return luas

# luas = luas_persegi(2)
# print(luas)




# # membuat variabel global
# Nama = "Informatika" 
# Mata_Kuliah = "Algoritma dan Pemrograman Dasar"
# # membuat variabel lokal
# def info():
#     Nama = "Teknik Elektro"
#     Mata_Kuliah = "Pengantar Teknik ELektro"
#     # mengakses variabel lokal
#     print("Prodi:", Nama)
#     print("Mata Kuliah:", Mata_Kuliah)
# # mengakses variabel global
# print("Prodi:", Nama)
# print("Mata Kuliah:", Mata_Kuliah)
# # memanggil fungsi info
# info()




# buku =[]
# def show_data():
#     if len(buku) <= 0:
#         print ("Belum Ada data")
#     else:
#         print("ID", "Nama Buku")
#         for indeks in range(len(buku)):
#             print (indeks, buku[indeks])
            
# def insert_data():
#     buku_baru = input('Judul Buku : ')
#     buku.append(buku_baru)
    
# def edit_data():
#     show_data()
#     indeks = int(input('Masukkan ID Buku : '))
#     if indeks >= len(buku) or indeks < 0 :
#         print('ID Salah')
#     else:
#         judul_buku = input('Masukkan Judul Baru Buku : ')
#         buku[indeks] = judul_buku
        
# def delete_data():
#     show_data()
#     indeks = int(input('Masukkan ID Buku : '))
#     if indeks >= len(buku) or indeks < 0 :
#         print('ID Salah')
#     else:
#         buku.remove(buku[indeks])
    
# def show_menu():
#     print('Menu')   
#     print('1. Read')        
#     print('2. Create')        
#     print('3. Update')        
#     print('4. Delete')
#     print('5. Keluar')        
#     pilihan = int(input('Masukkan Pilihan : '))
#     if pilihan == 1:
#         show_data
#     elif pilihan == 2:
#         insert_data()
#     elif pilihan == 3:
#         edit_data()
#     elif pilihan == 4:
#         delete_data()
#     elif pilihan == 5:
#         exit()
#     else:
#         print('Pilihan Tidak Valid')
        
# while(True):
#     show_menu




# def luas_segitiga():
#     alas = float(input('Masukkan Alas : '))
#     tinggi = float(input('Masukkan Tinggi : '))
#     luas = 0.5 * alas * tinggi
#     return luas

# print(luas_segitiga())



# def luas_persegi_panjang():
#     panjang = int(input('Masukkan Panjang : '))
#     lebar = int(input('Masukkan Lebar : '))
#     luas = panjang * lebar
#     return luas

# print(luas_persegi_panjang())




                            #LIBRARY

# import math
# angka = 49
# print(math.sqrt(angka))



#Cara install library adalah, di terminal ketik " pip install (nama library)" lalu enter