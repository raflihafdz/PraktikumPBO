import random as pilih

class Robot:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage
        self.jumlah_turn = 0
    
    def lakukan_aksi(self):
        print(f"{self.name} menyerang lawan dengan damage {self.damage}")
        if self.jumlah_turn % self.get_balas() == 0 and self.jumlah_turn != 0:
            self.aksi()
        self.jumlah_turn += 1
    
    def terima_aksi(self, damage_lawan):
        self.health -= damage_lawan
    
    def get_balas(self):
        pass
    
    def aksi(self):
        pass

class Antares(Robot):
    def __init__(self):
        super().__init__("Antares", 50000, 5000)
        self.multiplier = 1
    
    def get_balas(self):
        return 3
    
    def aksi(self):
        print(f"{self.name} meningkatkan damage sementara menjadi {self.damage*self.multiplier}")
        self.damage *= self.multiplier
        self.multiplier = 1.5

class Alphasetia(Robot):
    def __init__(self):
        super().__init__("Alphasetia", 40000, 6000)
    
    def get_balas(self):
        return 2
    
    def aksi(self):
        print(f"{self.name} menambah health sebanyak 4000 menjadi {self.health+4000}")
        self.health += 4000

class Lecalicus(Robot):
    def __init__(self):
        super().__init__("Lecalicus", 45000, 5500)
        self.multiplier = 1
    
    def get_balas(self):
        return 4
    
    def aksi(self):
        print(f"{self.name} meningkatkan damage sementara menjadi {self.damage*self.multiplier} dan menambah health sebanyak 7000 menjadi {self.health+7000}")
        self.damage *= self.multiplier
        self.multiplier = 2
        self.health += 7000

def main():
    robots = [Antares(), Alphasetia(), Lecalicus()]
    while len(robots) > 1:
        pilihan_robot = {}
        for robot in robots:
            pilihan = pilih.choice(["gunting", "batu", "kertas"])
            pilihan_robot[robot.name] = pilihan
        print(pilihan_robot)

        pilihan_tertinggi = max(pilihan_robot, key=pilihan_robot.get)
        pilihan_terendah = min(pilihan_robot, key=pilihan_robot.get)

        print(f"{pilihan_tertinggi} menang melawan {pilihan_terendah}")
        for robot in robots:
            if robot.name == pilihan_tertinggi:
                robot.lakukan_aksi()
            else:
                robot.terima_aksi(robot.damage)
                if robot.health <= 0:
                    print(f"{robot.name} kalah")
                    robots.remove(robot)
                    break
        print()

    print(f"{robots[0].name} adalah robot terkuat dengan health {robots[0].health}")

if __name__ == "__main__":
    main()
