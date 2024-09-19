from enemy import *
from Zombie import *
from Ogre import *
from Weapon import *
from Hero import *

def battle(e1: Enemy, e2: Enemy):
    e1.talk()
    e2.talk()

    while e1.health>0 and e2.health>0:
        print("----------")
        e1.special_attack()
        e2.special_attack()
        print(f"{e1.get_type_of_enemy()}: {e1.health} HP left!")
        print(f"{e2.get_type_of_enemy()}: {e2.health} HP left!")
        e1.attack()
        e2.attack()
        e1.health-=e2.attack_points
        e2.health-=e1.attack_points
        print("----------")
    
    if(e1.health>0):
        print(f"{e1.get_type_of_enemy} wins!")
    else:
        print(f"{e2.get_type_of_enemy()} wins!")

def hero_battle(hero: Hero, enemy:Enemy):
    while hero.health>0 and enemy.health>0:
        print("----------")
        enemy.special_attack()
        print(f"Hero: {hero.health} HP left!")
        print(f"{enemy.get_type_of_enemy()} HP left!")
        enemy.attack()
        hero.health-=enemy.attack_points
        hero.attack()
        enemy.health-=hero.attack_points
    print("----------")

    if hero.health>0:
        print("Hero wins!")
    else:
        print(f"{enemy.get_type_of_enemy()} wins!")


# obj1=Zombie(10, 1)
# obj2 = Ogre(20, 3)
# battle(obj1, obj2)

zombie = Zombie(10, 1)
hero = Hero(10, 1)
sword = Weapon("Sword", 5)
hero.weapon=sword
hero.equip_weapon()
hero_battle(hero, zombie)