from Zombie import *

obj=Zombie(100, 10)

print(f"{obj.get_type_of_health()} has {obj.health} points and can do attack of {obj.attack}")

obj.talk()
obj.spread_disease()