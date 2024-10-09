# daftar_buku = {
#     #Key        #Value
# "Buku1" : "Harry Potter",
# "Buku2" : "Percy Jackson",
# "Buku3" : "Twillight"
# }

# print(daftar_buku["Buku1"])
# print(daftar_buku["Buku2"])
# print(daftar_buku["Buku3"])


# game = dict(sekiro = 'action', pokemon = 'adventure' , valorant = 'fps')

# print(game)


# Biodata = {
# "Nama" : "Aldy Ramadhan Syahputra", #string
# "NIM" : 2109106079, #integer
# "KRS" : ["Program Web", "Struktur Data", "Basis Data"], #list
# "Mahasiswa_Aktif" :True,    #bool
# "Social Media" : {  #dictionary
# "Instagram" : "@aldyrmdhns_",
# "Discord" : "\'Izanami#6848"
#     }
# }

# print(Biodata['KRS'][1])

# print(Biodata.get('Nama'))   #jika data kosong, maka otomatis akan print 'none'

# print(Biodata.get('alamat', 'kosong le'))   #jika data kosong, maka otomatis akan print 'kosong le'


#looping

# for i,j in Biodata.items():
#     print(f'key {i} dan Value = {j}')

# for i in Biodata:
#     print(Biodata[i])



# Film = {
# "Avenger Endgame" : "Action",
# "Sherlock Holmes" : "Mystery",
# "The Conjuring" : "Horror"
# }


#Menambah item

# Film['ZombieLand'] = 'Comedy'
# Film.update({'hour' : 'Thriller'})
# print(Film)


#Menghapus item

# del Film['The Conjuring']i
# print(Film)

# hapus = Film.pop('The Conjuring')
# print(Film)
# print(f'Key yang di hapus = {hapus}')

# Film.clear()
# print(Film)


# Biodata = {
# "Nama" : "Aldy Ramadhan Syahputra", #string
# "NIM" : 2109106079, #integer
# "KRS" : ["Program Web", "Struktur Data", "Basis Data"], #list
# "Mahasiswa_Aktif" :True,    #bool
# "Social Media" : {  #dictionary
# "Instagram" : "@aldyrmdhns_",
# "Discord" : "\'Izanami#6848"
#     }
# }

#Fungsi dalam dictionary

# print('Jumlah Data Dalam Dicitonary = ', len(Biodata))

# pinjamdict = Biodata.copy()
# print(pinjamdict)

# key = 'apel', 'jeruk', 'mangga'
# value = 1

# buah = dict.fromkeys(key, value)
# print(buah)

# Film = {
# "Avenger Endgame" : "Action",
# "Sherlock Holmes" : "Mystery",
# "The Conjuring" : "Horror"
# }

# # for i in Film.keys():
# #     print(i)

# # for i in Film.values():
# #     print(i)

# print('Film :', Film.setdefault('Oldbook', 'Horror'))
# print(Film)


#List

# Musik = {
# "The Chainsmoker" : ["All we Know", "TheParis"],
# "Alan Walker" : ["Alone", "Lily"],
# "Neffex" : ["Best of Me", "Memories"]
# }

# for i,j in Musik.items():
#     print(f'Musik milik {i} adalah : ')
#     for lagu in j:
#         print(lagu)
#     print('')


#Nested Dictionary

# mahasiswa = {
#     101 : {"Nama" : "Aldy", "Umur" : 19},
#     111 : {"Nama" : "Abdul", "Umur" : 18}
# }
# for i,j in mahasiswa.items():
#     print(f'ID : {i}')
#     for keynested, valuenested, in j.items():
#         print(f'{keynested} :  {valuenested}')

# print(f'sebelum : {mahasiswa}')
# mahasiswa[101]['Angkatan'] = 2023
# print(f' sesudah : {mahasiswa}')

# print(f'sebelum : {mahasiswa}')
# del mahasiswa[111]['Umur']
# print(f' sesudah : {mahasiswa}')


#Studi Kasus

# biodata = {
# "Nama" : "Dwiki Aprilian Aryanda",
# 'Umur'  : 18,
# "NIM" : 2409106001,
# 'Jurusan' : 'Informatika',
# 'Angkatan'  : 24
# }

# print(biodata.get('NIM'))
# biodata.update({'Umur' : '19'})
# print(biodata)



Biodata = {}

while True:
    print("1. Tambah")
    print("2. Tampilakan")
    print("3. Exit")
    pilihan =  int(input("(1/2/3) : "))

    if pilihan == 1:
        nama = input("Masukkan nama :")
        umur = input("Masukkan umur :")
        alamat = input("Masukkan alamat :")

        Biodata[nama] = { 
            'Umur' : umur,
            'Alamat' : alamat
        }

    elif pilihan == 2:
        for nama, info in Biodata.items():
            print(f"Nama : {nama}")
            print(f"Umur : {info['Umur']}")
            print(f"Alamat : {info['Alamat']}")

    elif pilihan == 3:
        print("exit ...")
        break

    else:
        print("Invalid ... ... ")