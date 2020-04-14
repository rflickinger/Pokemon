class Pokemon:
    def __init__(self, name, level, type, max_health, current_health, ko):
        self.name = name                     #str name
        self.level = level                   #int level
        self.pType = type                    #str type ie: water, fire, etc
        self.max_health = max_health         #int maximum health
        self.current_health = current_health #int current health
        self.ko = ko                         #bool is knocked out
    def __repr__(self):                      #set object name to pokemon name
        return self.name
    
    #Method to take damage
    def lose_health(self, dmg):
        if dmg > self.current_health:
            self.current_health = 0
            self.ko = True                   #Possibly change this to a method
            print(f"Massive hit! {self.name} took {self.current_health} damage!")
            print(f"{self.name} has fainted.")#If ko is changed to a method remove this
        elif dmg == self.current_health:
            self.current_health = 0
            self.ko = True
            print(f"{self.name} took {dmg} damage.")
            print(f"{self.name} has fainted.")
        else:
            self.current_health = self.current_health - dmg
            print(f"{self.name} took {dmg} damage.")
    
    #Method to gain health
    def gain_health(self, amount):
        difference = self.max_health - self.current_health
        if amount >= difference:
            self.current_health = self.max_health
            print(f"{self.name} gained {difference} HP!")
        else:
            self.current_health = self.current_health + amount
            print(f"{self.name} gained {amount} HP!")
    



