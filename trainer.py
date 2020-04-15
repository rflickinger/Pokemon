from pokemon import Pokemon
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

    #Switches active pokemon
    def switch(self, index):
        if self.team[index].ko == False:
            print(f"Come back {self.team[self.active].name}!")
            self.active = index
            print(f"I choose you {self.team[self.active].name}")
        else:
            print(f"{self.team[index].name} has fainted and cannot fight, try again!")
    
    #Trainer's active pokemon attacks other trainer's active pokemon
  #  def attack_trainer(self, victim):

        