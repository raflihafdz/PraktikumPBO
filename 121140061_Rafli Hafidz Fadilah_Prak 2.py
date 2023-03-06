class Mahasiswa:
    
    def __init__(self,nama,nim,kelas,sks):
        self.nama=nama
        self.nim=nim
        self.kelas=kelas
        self.sks=sks
    
    def data (self):
        print("Nama : ",self.nama)
        print("Nim  : ",self.nim)
        print("Kelas: ",self.kelas)
        print("Sks  : ",self.sks)
    
mhs=Mahasiswa("Rafli Hafidz Fadilah",121140061,"RB",22)
mhs.data()
