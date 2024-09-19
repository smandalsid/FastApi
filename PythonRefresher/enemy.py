class Enemy:
    def __init__(self, type, health, attack_points):
        self.__type=type
        self.health=health
        self.attack_points=attack_points

    def talk(self):
        print(f"I am {self.__type} of enemy")

    def get_type_of_enemy(self):
        return self.__type
    
    def attack(self):
        print("Enemy has no special attack")
    