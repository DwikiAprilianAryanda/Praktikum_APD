username = 'admin'
password = '12345678'
profil = {}

def tampilkan_menu():
    print(
    """
    =============================================
    |              SELAMAT DATANG!              |
    |   SILAHKAN MEMILIH PILIHAN DI BAWAH INI!  |
    =============================================
    |    1. LOGIN SEBAGAI ADMIN                 |           
    |    2. REGISTER SEBAGAI PENGGUNA BARU      |
    |    3. LIHAT JUMLAH PENGGUNA               |
    |    4. KELUAR                              |
    =============================================
    """)


def tampilkan_profil():
    if len(profil) == 0:
        print("Belum ada profil yang terdaftar.")
    else:
        i = 1
        for nick, data in profil.items():
            print(f"\nProfil Game Ke-{i}\nNick Game : {nick}\nTanggal Lahir : {data['Tanggal Lahir']}\nGender : {data['Gender']}\nEmail : {data['Email']}\nNo. Telepon : {data['Telepon']}")
            i += 1


def update_profil():
    try:
        i = 1
        for nick in profil.keys():
            print(f"{i}. Nick Game : {nick}")
            i += 1

        pilih_profil = int(input("\nPilih Nomor Profil Yang Ingin Diubah: "))
        if pilih_profil < 1 or pilih_profil > len(profil):
            print("Nomor Profil Tidak Valid.")
            return

        nick_dipilih = list(profil.keys())[pilih_profil - 1]
        print('''  
            =====================================
            |   Pilih Data Yang Ingin Di ganti  |
            =====================================
            |         1. Nick Game              |           
            |         2. Tanggal Lahir          |          
            |         3. Gender                 |  
            |         4. Email                  |
            |         5. No. Telepon            |
            =====================================
        ''')
        data_update = input("Masukkan Pilihan: ")

        if data_update == '1':
            nick_baru = input("Masukkan Nick Baru: ")
            profil[nick_baru] = profil.pop(nick_dipilih)
            print('Nick Game Berhasil Diubah')
        elif data_update == '2':
            tanggal_lahir_baru = input("Masukkan Tanggal Lahir Baru (Tanggal Bulan Tahun): ")
            profil[nick_dipilih]['Tanggal Lahir'] = tanggal_lahir_baru
            print('Tanggal Lahir Berhasil Diubah')
        elif data_update == '3':
            gender_baru = input("Masukkan Gender Baru: ")
            if gender_baru != 'l' and gender_baru != 'p':
                print('Pilih Antara l(Laki-laki) Atau p(Perempuan)')
            else:
                profil[nick_dipilih]['Gender'] = gender_baru
                print('Gender Berhasil Diubah')
        elif data_update == '4':
            email_baru = input("Masukkan Email Baru: ")
            profil[nick_dipilih]['Email'] = email_baru
            print('Email Berhasil Diubah')
        elif data_update == '5':
            telepon_baru = input("Masukkan No. Telepon Baru: ")
            profil[nick_dipilih]['Telepon'] = telepon_baru
            print('No. Telepon Berhasil Diubah')
        else:
            print('Pilihan Tidak Valid')
    except ValueError:
        print("Masukkan angka yang valid!")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")


def hapus_profil():
    try:
        nick_lama = input("Masukkan Nick Yang Ingin Dihapus: ")
        if nick_lama in profil:
            del profil[nick_lama]
            print(f'Profil Dengan Nick {nick_lama} Berhasil Dihapus')
        else:
            print('Nick Yang Anda Maksud Tidak Ditemukan')
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")


def lihat_statistik_pengguna():
    try:
        jumlah_pengguna = len(profil)
        print(f"\nJumlah pengguna yang terdaftar: {jumlah_pengguna}\n")
        if jumlah_pengguna > 0:
            tampilkan_profil()
        else:
            print('Tidak Ada Pengguna Yang Tedaftar')
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")


def login_admin():
    try:
        username_input = input('Masukkan Username : ')
        password_input = input('Masukkan Password : ')
        if username_input == username and password_input == password:
            print("Login Berhasil!")
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
                try:
                    pilih_admin = int(input('PILIH : '))
                    if pilih_admin == 1:
                        tampilkan_profil()  
                    elif pilih_admin == 2:
                        update_profil()  
                    elif pilih_admin == 3:
                        hapus_profil()  
                    elif pilih_admin == 4:
                        print("Terima Kasih Telah Mengisi Data")
                        break
                    else:
                        print("Pilihan Anda Tidak Valid")
                except ValueError:
                    print("Masukkan angka yang valid!")
        else: 
            print("Login Gagal!")
            return
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")


def register():
    try:
        print('Isi Untuk Profil Game Anda')
        nick_game = input('Nick Game : ')
        tanggal_lahir = input('Tanggal Lahir (Tanggal Bulan Tahun): ')
        gender = input('Jenis Kelamin(l/p) : ')
        if gender != 'l' and gender != 'p':
            print('Pilih Antara l(Laki-laki) Atau p(Perempuan)')
            return
        email = input('Masukkan Email Anda: ')
        telepon = input('Masukkan No. Telepon Anda: ')
        konfirmasi = input('Apakah Anda Yakin Dengan Data Yang Sudah Anda Isi?(y/n) : ')
        if konfirmasi == 'y':
            profil[nick_game] = {'Tanggal Lahir': tanggal_lahir, 'Gender': gender, 'Email': email, 'Telepon': telepon}
            print('Registrasi Berhasil!')
        elif konfirmasi == 'n':
            print('Silahkan Mengisi Ulang Data Yang Tidak Sesuai')
        else:
            print('Pilih Antara y(Yes) atau n(No)')
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")


def menu_register():
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
        try:
            pilih_user = int(input("PILIH : "))
            if pilih_user == 1:
                register()
            elif pilih_user == 2:
                tampilkan_profil()  
            elif pilih_user == 3:
                print("Terima Kasih Telah Mengisi Data")
                break
            else:
                print("Pilihan Anda Tidak Valid")
        except ValueError:
            print("Masukkan angka yang valid!")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")


while True:
    try:
        tampilkan_menu()
        pilih = int(input("PILIH : "))
        
        if pilih == 1:
            login_admin()         

        elif pilih == 2:
            menu_register()

        elif pilih == 3:
            lihat_statistik_pengguna()
        
        elif pilih == 4:
            print("Terima Kasih Telah Berpartisipasi")
            break
        
        else:
            print("Pilihan Anda Tidak Valid")
    except ValueError:
        print("Masukkan angka yang valid!")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
