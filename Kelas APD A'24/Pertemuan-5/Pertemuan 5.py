# nama = ['Celio' , 'Shandy' , 'Afrizal' , 'Farrel' , 'Ahnaf' , 'Fajar' , 'Lian' , 'Rusdi' , 'Rasyid']

# print('sebelum: ')
# print(nama[3:5])
# print('')
# print('sesudah')
# nama.append('afrizal')
# print(nama)
# nama.insert(2, 'afrizal')
# print(nama)


    #Update
# nama[3]= 'fufufafa'


    #Delete
# del nama[2]
# hapus = nama.pop(2)
# print(nama)
# print(hapus)


    #Slice
# print(nama[0:2])
# print(nama[1:9:2])


    #Menambahkan List
# matkul = ['APD' , 'APL' , 'BASDAT' , 'STRUKDAT' , 'WEB' , 'JARKOM']

# data = nama + matkul

# print(data)

# print(data*3)


    #nested list
# data = ['farrel' , 'celio',[1,2,['hai' , 23.3 , 2, True]]]

# print(data[2][2][::1])
# print(data[::-1])


    #looping dalam nested list
# matkul = [[1,2,3,4] , ['halo' , 'hai'] , [0.1 , 0.2]]

# for i in matkul:
#     print(i)
    
# for i in matkul:
#     print(i, end=' ')

# for i in matkul:
#     for j in i:
#          print(j)


    #tuple
# nama = ('farrel' , 'vito' , 'shandy' , 'rijal')
# print(nama[1])

# mahasiswa = (69, "Informatika", "2209106044", "Aldy septian ")

# absen, prodi, nim, nama = mahasiswa
# print(mahasiswa)


print( 
"""
===========================
|   DATA MAHASISWA A24    |
===========================
|    1. TAMBAH DATA       |           
|    2. TAMPILKAN DATA    |          
|    3. UBAH DATA         |     
|    4. HAPUS DATA        |      
|    5. KELUAR            |  
===========================
"""
)

data_mahasiswa = []
while True:
    pilih = int(input("PILIH : "))
    if pilih == 1:
        nama = input("NAMA : ")
        nim = input("NIM : ")
        kelas = input("KELAS : ")
        data_mahasiswa.append([nama,nim,kelas])
    elif pilih == 2:
        for i in range(len(data_mahasiswa)):
            print(f"\n Data Mahasiswa ke-{i+1}\nNAMA : {data_mahasiswa[i][0]}\nNIM : {data_mahasiswa[i][1]}\nKELAS : {data_mahasiswa[i][2]}")
    elif pilih == 3:
        nama_lama = input("Nama Baru : ")
        for i in range(len(data_mahasiswa)):
            if data_mahasiswa[i][0] == nama_lama:
                nama_baru = input("NAMA : ")
                nim_baru = input("NIM : ")
                kelas_baru = input("KELAS : ")
                data_mahasiswa[i][0] = nama_baru
                data_mahasiswa[i][1] = nim_baru
                data_mahasiswa[i][2] = kelas_baru
    elif pilih == 4:
        nama_lama = input("Nama yang ingin dihapus")
        for i in range(len(data_mahasiswa)):
            if data_mahasiswa[i][0] == nama_lama:
                del data_mahasiswa[i]
    elif pilih == 5:
        print("Terima Kasih Telah Mengakses Data Mahasiswa")
        break
    else:
        print("Anda Salah Input")