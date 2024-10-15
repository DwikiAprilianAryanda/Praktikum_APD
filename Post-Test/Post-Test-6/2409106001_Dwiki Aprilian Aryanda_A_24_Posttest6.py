username = 'admin'
password = '12345678'

profil = {}
while True:
    
    print( 
    """
    =============================================
    |              SELAMAT DATANG!              |
    |   SILAHKAN MEMILIH PILIHAN DI BAWAH INI!  |
    =============================================
    |    1. LOGIN SEBAGAI ADMIN                 |           
    |    2. REGISTER SEBAGAI PENGGUNA BARU      |
    |    3. KELUAR                              |
    =============================================
    """
    )

    pilih = int(input("PILIH : "))
    if pilih == 1:
        print('\nSilahkan Isi Username Dan Password')
        login_username = input('Masukkan Username Anda : ')
        login_password = input('Masukkan Password Anda : ')
        if login_username == username and login_password == password:
            print('Login Berhasil!')

            print( 
            """
            ===========================
            |    MENU KHUSUS ADMIN     |
            ===========================
            |    1. TAMPILKAN PROFIL   |           
            |    2. UPDATE PROFIL      |          
            |    3. HAPUS DATA PROFIL  |     
            |    4. KELUAR             |      
            ===========================
            """
            )
            
            while True:
                pilih_admin = int(input('PILIH : '))   
                if pilih_admin == 1:
                    i = 1
                    for nick, data in profil.items():
                        print(f"\n Profil Game Yang Ke-{i}\nNick Game : {nick}\nTanggal Lahir : {data['Tanggal Lahir']}\nGender : {data['Gender']}")
                        i += 1
                elif pilih_admin == 2:
                    print("\nProfil Yang Terdaftar : ")
                    i = 1
                    for nick in profil.keys():
                        print(f"{i}. Nick Game : {nick}")
                        i += 1
                        
                    pilih_profil = int(input("\nPilih Nomor Profil Yang Ingin Diubah: "))
                    if pilih_profil < 1 or pilih_profil > len(profil):
                        print("Nomor Profil Tidak Valid.")
                        continue
                    
                    nick_dipilih = list(profil.keys())[pilih_profil - 1]
                    print('''  
                        =====================================
                        |   Pilih Data Yang Ingin Di ganti  |
                        =====================================
                        |         1. Nick Game              |           
                        |         2. Tanggal Lahir          |          
                        |         3. Gender                 |  
                        =====================================
                        '''
                    )
                    data_update = input(" ")
                    if data_update == '1':
                        nick_baru = input("Masukkan Nick Baru : ")
                        profil[nick_baru] = profil.pop(nick_dipilih)
                        print('Nick Game Berhasil Diubah')
                    elif data_update == '2':
                        tanggal_lahir_baru = input("Masukkan Tanggal Lahir Baru : ")
                        profil[nick_dipilih]['Tanggal Lahir'] = tanggal_lahir_baru
                        print('Tanggal Lahir Berhasil Diubah')
                    elif data_update == '3':
                        gender_baru = input("Masukkan Gender Baru : ")
                        if gender != 'l' and gender != 'p':
                            print('Pilih Antara l(Laki-laki) Atau p(Perempuan)')
                        else:
                            profil[nick_dipilih]['Gender'] = gender_baru
                            print('Gender Berhasil Diubah')
                    else:
                        print('Pilihan Tidak Valid')
                elif pilih_admin == 3:
                    nick_lama = input("Masukkan Nick Yang Ingin Dihapus : ")
                    if nick_lama in profil:
                        del profil[nick_lama]
                        print(f'Profil Dengan Nick {nick_lama} Berhasil Dihapus')
                    else:
                        print('Nick Yang Anda Maksud Tidak Ditemukan')
                elif pilih_admin == 4:
                    print("Terima Kasih Telah Mengisi Data")
                    break
                else:
                    print("Pilihan Anda Tidak Valid")               
        else:
            print('Login Gagal!')
        
    elif pilih == 2:
        
        print( 
        """
        ====================================
        |   REGISTER PROFIL PENGGUNA BARU  |
        ====================================
        |    1. REGISTER                   |           
        |    2. TAMPILKAN DATA             |
        |    3. KELUAR  
        ====================================
        """
        )       
        while True:    
            pilih_user = int(input("PILIH : "))
            if pilih_user == 1:
                print('Isi Untuk Profil Game Anda')
                nick_game = input('Nick Game : ')
                tanggal_lahir = input('Tanggal Lahir : ')
                gender = input('Jenis Kelamin(l/p) : ')
                if gender != 'l' and gender != 'p':
                    print('Pilih Antara l(Laki-laki) Atau p(Perempuan)')
                    continue
                konfirmasi = input('Apakah Anda Yakin Dengan Data Yang Sudah Anda Isi?(y/n) : ')
                if konfirmasi == 'y':
                    profil[nick_game] = {'Tanggal Lahir': tanggal_lahir, 'Gender': gender}
                    print('Registrasi Berhasil!')
                elif konfirmasi == 'n':
                    print('Silahkan Mengisi Ulang Data Yang Tidak Sesuai')
                else:
                    print('Pilih  Antara y(Yes) atau n(No)')
            elif pilih_user == 2:
                i = 1
                for nick, data in profil.items():
                    print(f"\n Profil Game Yang Ke-{i}\nNick Game : {nick}\nTanggal Lahir : {data['Tanggal Lahir']}\nGender : {data['Gender']}")
                    i += 1
            elif pilih_user == 3:
                print("Terima Kasih Telah Mengisi Data")
                break
            else:
                print("Pilihan Anda Tidak Valid")
    
    elif pilih == 3:
        print("Terima Kasih Telah Berpartisipasi")
        break
    
    else:
        print("Pilihan Anda Tidak Valid")
