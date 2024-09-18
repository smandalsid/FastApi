from enemy import *

class Zombie(Enemy):
    def __init__(self, health, attack):
        super().__init__(type="Zombie", health=health, attack=attack)

    def talk(self):
        print("GRRRRRR....")

    def spread_disease(self):
        print("I spread infection")