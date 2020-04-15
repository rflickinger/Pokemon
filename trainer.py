import Pokemon
class Trainer:
    def __init__(self, name, team, active, potions):
        self.name = name
        self.team = team
        self.active = active
        self.potions = potions
    def __repr__(self):
        return self.name
    
    #Heals active pokemon for 20 HP
    def use_potion(self):
        if self.active.max_health > self.active.current_health:
            if self.potions >= 1:
                self.potions = self.potions -1
                print(f"{self.name} used a potion on {self.active.name}.")
                self.active.gain_health(20)
            else:
                print(f"{self.name} is out of potions!")
        else:
            print(f"{self.active.name} is already at full health!")
