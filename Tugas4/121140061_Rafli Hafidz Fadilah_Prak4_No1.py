class Komputer:

    def __init__(self,nama,harga,versi,merk):
        self.nama=nama
        self.harga=harga
        self.versi=versi
        self.merk=merk

class Procesor(Komputer):
    def __init__(self,nama,harga,versi,merk,jumlah_core,kecepatan_core):
        super().__init__(nama,harga,versi,merk)
        self.jumlah_core=jumlah_core
        self.kecepatan_core=kecepatan_core

class RAM(Komputer):
    def __init__(self,nama,harga,versi,merk,capacity):
        super().__init__(nama,harga,versi,merk)
        self.capacity=capacity

class HDD(Komputer):
    def __init__(self, nama, harga, versi, merk,Hdd_Capacity,rpm):
        super().__init__(nama, harga, versi, merk)
        self.Hdd_Capacity=Hdd_Capacity
        self.rpm=rpm

class VGA(Komputer):
    def __init__(self, nama, harga, versi, merk,Vga_Capacity):
        super().__init__(nama, harga, versi, merk)
        self.Vga_Capacity=Vga_Capacity

class PSU(Komputer):
    def __init__(self, nama, harga, versi, merk,daya):
        super().__init__(nama, harga, versi, merk)
        self.daya=daya

p1 = Procesor('Processor','Intel','Core i7 7740X',4350000,4,'4.3GHz')
p2 = Procesor('Processor','AMD','Ryzen 5 3600',250000,4,'4.3GHz')
ram1 = RAM('RAM :','V-Gen','DDR4 SODimm PC19200/2400MHz',328000,'4GB')
ram2 = RAM('RAM :','G.SKILL','DDR4 2400MHz',328000,'4GB')
hdd1 = HDD('HDD :','Seagate','HDD 2.5 inch',295000,'500GB',7200)
hdd2 = HDD('HDD :','Seagate','HDD 2.5 inch',295000,'1000GB',7200)
vga1 = VGA('VGA :','Asus','VGA GTX 1050',250000,'2GB')
vga2 = VGA('VGA :','Asus','1060Ti',250000,'8GB')
psu1 = PSU('PSU :','Corsair','Corsair V550',250000,'500W')
psu2 = PSU('PSU :','Corsair','Corsair V550',250000,'500W')

rakit = [[p1,ram1,hdd1,vga1,psu1],[p2,ram2,hdd2,vga2,psu2]]

for i, komputer in enumerate(rakit):
    print()
    print("Komputer ", i+1)
    for objek in komputer:
        print(objek.nama,  " ", objek.versi, " produksi ", objek.merk)