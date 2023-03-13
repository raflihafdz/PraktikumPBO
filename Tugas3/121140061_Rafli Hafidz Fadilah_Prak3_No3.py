class Karyawan:
    #variable kelas untuk hitung jumlah karyawan
    jumlah_karyawan = 0
    
    #inisiasi var objek
    def __init__(self, nama, gaji, posisi):
        self.nama = nama
        self.gaji = gaji
        self.posisi = posisi
        #tambah jumlah karyawan +1
        Karyawan.jumlah_karyawan += 1

    # nambah nama karyawan    
    def get_nama(self):
        return self.nama
    
    # ubah nama karyawan
    def set_nama(self, nama_baru):
        self.nama = nama_baru

    # gaji awal   
    def get_gaji(self):
        return self.gaji
    
    # gaji baru
    def set_gaji(self, gaji_baru):
        self.gaji = gaji_baru

    # posisi awal    
    def get_posisi(self):
        return self.posisi
    
    #posisi baru
    def set_posisi(self, posisi_baru):
        self.posisi = posisi_baru

    #rumus perhitungan naik gaji    
    def naik_gaji(self, persen):
        self.gaji += self.gaji * persen / 100
    
    #output
    def info(self):
        print(f"Nama: {self.nama}")
        print(f"Posisi: {self.posisi}")
        print(f"Gaji: {self.gaji}")
        print()
# membuat objek karyawan pertama
karyawan1 = Karyawan("John", 5000000, "Manager")
karyawan1.naik_gaji(10)
karyawan1.info()

# mengubah nama karyawan pertama
karyawan1.set_nama("John Doe")
print("Nama karyawan 1 setelah diubah:", karyawan1.get_nama())

# membuat objek karyawan kedua
karyawan2 = Karyawan("Jane", 3000000, "Staff")
karyawan2.naik_gaji(5)
karyawan2.info()

# mengubah posisi karyawan kedua
karyawan2.set_posisi("Senior Staff")
print("Posisi karyawan 2 setelah diubah:", karyawan2.get_posisi())
print()

# mencetak jumlah karyawan yang telah dibuat
print("Jumlah karyawan:", Karyawan.jumlah_karyawan)

