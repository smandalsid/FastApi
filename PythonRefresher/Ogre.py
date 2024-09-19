from enemy import Enemy

import random

class Ogre(Enemy):
    def __init__(self, health, attack_points):
        super().__init__(type="Ogre", health=health, attack_points=attack_points)

    def talk(self):
        print("HU HA HU HA")
    
    def special_attack(self):
        did_special_attack_work=random.random()<0.20
        if did_special_attack_work:
            self.attack_points+=4
            print("Ogre get angry and attack damage has increased by 4!")
