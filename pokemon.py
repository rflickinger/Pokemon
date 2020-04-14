class Pokemon:
    #Type advantage dictionary. Dictionary reads as self --> victim
    type_matchups = {["Fire", "Fire"]: 1.0, ["Fire", "Grass"]: 2.0, ["Fire", "Water"]: 0.5, ["Water", "Fire"]: 2.0, ["Water", "Grass"]: 0.5, ["Water", "Water"]: 1.0, ["Grass", "Fire"]: 0.5, ["Grass", "Grass"]: 1.0, ["Grass", "Water"]: 2.0}
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
            print(f"Massive hit! {self.name} took {self.current_health} damage!")
            self.knock_out()
        elif dmg == self.current_health:
            self.current_health = 0
            print(f"{self.name} took {dmg} damage.")
            self.knock_out()
        else:
            self.current_health = self.current_health - dmg
            print(f"{self.name} took {dmg} damage.")
    
    #Method to gain health
    def gain_health(self, amount):
        difference = self.max_health - self.current_health
        if amount >= difference:
            self.current_health = self.max_health
            print(f"{self.name} gained {difference} HP! {self.name} is fully healed!")
        else:
            self.current_health = self.current_health + amount
            print(f"{self.name} gained {amount} HP! Total {self.current_health}")
    
    #Method to knock out a pokemon
    def knock_out(self):
        self.ko = True
        print(f"{self.name} has fainted.")
    
    #Method to revive a pokemon
    def revive(self):
        self.ko = False
        self.current_health = 1
        print(f"{self.name} has been revived!")
    
    #Method to attack
    def attack(self, victim):
        attack_damage = 0.0 + self.level
        attack_damage = attack_damage * type_matchups.get([self.type, victim.type])
        dmg_to_return = round(attack_damage)
        print(f"{self.name} attacked {victim.name}!")
        if type_matchups.get([self.type, vicitim.type]) == 2.0:
            print("The attack was super effective!")
        elif: type_matchups.get([self.type, vicitim.type]) == 0.5:
            print("The attack was not very effective...")
        victim.lose_health(dmg_to_return)