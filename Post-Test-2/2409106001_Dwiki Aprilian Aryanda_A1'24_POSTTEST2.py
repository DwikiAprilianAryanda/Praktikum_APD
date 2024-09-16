nama = input('Nama saya adalah ')              #tipe data string
nama_panggilan = input('Nama panggilan saya adalah ')    #tipe data stirng
nim = input('NIM saya adalah ')               #tipe data integer
umur = input('Umur saya adalah ')              #tipe data integer
tinggi = input('tinggi saya adalah ')            #tipe data float

p = 1
q = 6
r = p % q

print('Halo, perkenalkan nama saya adalah ' + nama + ', saya biasa dipanggil ' + nama_panggilan + ' dengan NIM ' + str(nim) + ', umur saya adalah ' + str(umur) + ' dan tinggi saya adalah ' + str(tinggi) + ', total NIM terakhir saya saat dimoduluskan dengan 6 adalah ' + str(r))