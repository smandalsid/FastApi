from Weapon import *

class Hero():
    def __init__(self, health, attack_points):
        self.health=health
        self.attack_points=attack_points
        self.is_equipped=False
        self.weapon:Weapon=None

    def equip_weapon(self):
        if(self.weapon is not None and not self.is_equipped):
            self.attack_points+=self.weapon.attack_increase
            self.is_equipped=True

    def attack(self):
        print(f"Hero attacks for {self.attack_points} damage!")