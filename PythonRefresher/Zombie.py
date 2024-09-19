from enemy import *
import random

class Zombie(Enemy):
    def __init__(self, health, attack_points):
        super().__init__(type="Zombie", health=health, attack_points=attack_points)

    def talk(self):
        print("GRRRRRR....")

    def spread_disease(self):
        print("I spread infection")

    def special_attack(self):
        did_special_attack_work = random.random()<.50
        if did_special_attack_work:
            self.health+=2
            print("Zombie regenerated 2 HP!")