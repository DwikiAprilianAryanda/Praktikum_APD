#Menu Login

batas_login = 3
username = 'Lian'
password = '1'

while batas_login > 0:
    user_input = input("Masukkan Username: ")
    pass_input = input("Masukkan Password: ")

    if user_input == username and pass_input == password:
        print("Login Berhasil!")
        break
    else:
        batas_login -= 1
        print(f"Login Gagal! Sisa percobaan: {batas_login}")

if batas_login == 0:
    print("Login Gagal 3 kali. Silahkan ulangi dari awal le.")
    exit()


#Menu Kebutuhan Kalori

while True:
    print('''Pilih Jenis Kelamin
        1. Pria
        2. Wanita''')
    pilihan = input('Masukkan Pilihan(1/2) ')

    if pilihan != '1' and pilihan != '2':
        print('Pilihan tidak valid')
        exit()

    berat_badan = int(input('Masukkan Berat Badan(kg) '))
    print(f'Berat Badan Adalah {berat_badan*1000} gr') 
    tinggi_badan = int(input('Masukkan Tinggi Badan(cm) '))
    print(f'Tinggi Badan Adalah {tinggi_badan/100000} km')
    umur = int(input('Masukkan Umur '))
    print(f'Umur Adalah {umur}')

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
        bmr = (10 * berat_badan) + int(6.25 * tinggi_badan) - (5 * umur) + 5
    elif pilihan == '2':
        bmr = (10 * berat_badan) + int(6.25 * tinggi_badan) - (5 * umur) - 161

    kalori_harian = bmr * aktivitas_harian
    print('Jadi kebutuhan kalori harian anda adalah sebanyak ' + str(kalori_harian) + ' kalori')


    #Menu Berhenti atau lanjut
    
    lanjutkan = input("Apakah Anda ingin melanjutkan? (iya/gak): ")
    if lanjutkan == 'gak':
        print("Program berhenti. Terima kasih!")
        exit()
    