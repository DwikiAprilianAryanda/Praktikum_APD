#Kalkulator Kebutuhan Kalori Harian

print('''Pilih Jenis Kelamin
      1. Pria
      2. Wanita''')
pilihan = input('Masukkan Pilihan(1/2) ')

if pilihan != '1' and pilihan != '2':
    print('tidak valid')
    exit()
   
berat_badan = float(input('Masukkan Berat Badan(gr) '))
print('Berat Badan Adalah ' + str(berat_badan) + 'gr') 
tinggi_badan = float(input('Masukkan Tinggi Badan(km) '))
print('Tinggi Badan Adalah ' + str(tinggi_badan) + 'km')
umur = int(input('Masukkan Umur '))
print('Umur Adalah ' + str(umur))

print('''Masukkan Level Aktivitas Harian
        1. Aktivitas Minimal (jarang bergerak)
        2. Aktivitas Sedang (olahraga 1-3 kali seminggu)
        3. Aktivitas Tinggi (olahraga 4-7 kali seminggu)''')
aktivitas = input('Masukkan Pilihan(1/2/3) ')

if aktivitas == '1':
    aktivitas_harian = 1.25
elif aktivitas == '2':
    aktivitas_harian = 1.36
elif aktivitas == '3':
    aktivitas_harian = 1.72
else:
    print('Pilihan tidak valid')
    exit()

if pilihan == '1':
    bmr = (10*berat_badan) + int(6.25*tinggi_badan) - (5*umur) + 5
elif pilihan == '2':
    bmr = (10*berat_badan) + int(6.25*tinggi_badan) - (5*umur) - 161
    
kalori_harian = bmr*aktivitas_harian
print('Jadi kebutuhan kalori harian anda adalah sebanyak ' + str(kalori_harian) + ' kalori')
