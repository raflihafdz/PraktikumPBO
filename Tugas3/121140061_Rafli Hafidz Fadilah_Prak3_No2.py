class AkunBank:
    list_pelanggan = []

    def __init__(self, no_pelanggan, nama_pelanggan, jumlah_saldo):
        self.__no_pelanggan = no_pelanggan
        self.__nama_pelanggan = nama_pelanggan
        self.__jumlah_saldo = jumlah_saldo
        self.__class__.list_pelanggan.append(self)

    def lihat_menu(self):       
        print("Selamat Datang di Bank ABC")     
        print("Pilihan Menu:")
        print("1. Lihat Saldo")
        print("2. Tarik Tunai")
        print("3. Transfer")
        print("4. Keluar")
        

    def lihat_saldo(self):
        print(f"Saldo Anda saat ini: {self.__jumlah_saldo:,}")

    def tarik_tunai(self, jumlah):
        if jumlah > self.__jumlah_saldo:
            print("Saldo Anda tidak cukup")
        else:
            self.__jumlah_saldo -= jumlah
            print(f"Berhasil melakukan penarikan tunai sebesar {jumlah:,}")
            print(f"Saldo Anda saat ini adalah {self.__jumlah_saldo:,}")

    def transfer(self, no_pelanggan_tujuan, jumlah):
        pelanggan_tujuan = None
        for pelanggan in self.__class__.list_pelanggan:
            if pelanggan._AkunBank__no_pelanggan == no_pelanggan_tujuan:
                pelanggan_tujuan = pelanggan
                break
        if pelanggan_tujuan is None:
            print("Nomor rekening tujuan tidak ditemukan")
        elif jumlah > self.__jumlah_saldo:
            print("Saldo Anda tidak cukup")
        else:
            self.__jumlah_saldo -= jumlah
            pelanggan_tujuan._AkunBank__jumlah_saldo += jumlah
            print(f"Transfer sebesar Rp{jumlah:,} berhasil dilakukan ke nomor rekening {no_pelanggan_tujuan}")
            print(f"Saldo Anda saat ini adalah Rp{self.__jumlah_saldo:,}")
            
    def main_menu(self):
        while True:
            self.lihat_menu()
            input_menu = input('Masukkan nomor input: ')
            if input_menu == '1':
                self.lihat_saldo()
            elif input_menu == '2':
                self.tarik_tunai()
            elif input_menu == '3':
                self.transfer()
            elif input_menu == '4':
                break
            else:
                print('Nomor rekening tidak ditemukan')

#  instansi AkunBank
Akun1 = AkunBank(1234, "Rafli", 5000000000)
Akun2 = AkunBank(2345, "Ukraina", 6666666666)
Akun3 = AkunBank(3456, "Elon Musk", 9999999999)

# penggunaan fungsi
Akun1.main_menu()