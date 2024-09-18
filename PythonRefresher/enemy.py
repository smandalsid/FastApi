class Enemy:
    def __init__(self, type, health, attack):
        self.__type=type
        self.health=health
        self.attack=attack

    def talk(self):
        print(f"I am {self.__type} of enemy")

    def get_type_of_health(self):
        return self.__type
    