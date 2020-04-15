class Pokemon:
    def __init__(self, name, level, type, max_health, current_health, ko):
        self.name = name                     #str name
        self.level = level                   #int level
        self.type = type                    #str type ie: water, fire, etc
        self.max_health = max_health         #int maximum health
        self.current_health = current_health #int current health
        self.ko = ko                         #bool is knocked out
    def __repr__(self):                      #set object name to pokemon name
        return f"{self.name}, {self.level}, {self.type}, {self.max_health}, {self.current_health}, {self.ko}"
   
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
    #tuple list to see if that works
    fi_fi = ("Fire", "Fire")
    fi_gr = ("Fire", "Grass")
    fi_wa = ("Fire", "Water")
    gr_fi = ("Grass", "Fire")
    gr_gr = ("Grass", "Grass")
    gr_wa = ("Grass", "Water")
    wa_fi = ("Water", "Fire")
    wa_gr = ("Water", "Grass")
    wa_wa = ("Water", "Water")
    #Type advantage dictionary. Dictionary reads as self --> victim
    matchups = {fi_fi:1.0, fi_gr:2.0, fi_wa:0.5, gr_fi:0.5, gr_gr:1.0, gr_wa:2.0, wa_fi:2.0, wa_gr:0.5, wa_wa:1.0}
    #Method to attack
    def attack(self, victim):
        tup = (self.type, victim.type)
        attack_damage = 0.0 + self.level
        attack_damage = attack_damage * self.matchups[tup]
        dmg_to_return = round(attack_damage)
        print(f"{self.name} attacked {victim.name}!")
        if self.matchups[tup] == 2.0:
            print("The attack was super effective!")
        elif self.matchups[tup] == 0.5:
            print("The attack was not very effective...")
        victim.lose_health(dmg_to_return)

#Creating Pokemon and other useful tools to make it easier to create teams


charmander = Pokemon("Charmander", 4, "Fire", 20, 20, False)
squirtle = Pokemon("Squirtle", 4, "Water", 20, 20, False)
bulbasaur = Pokemon("Bulbasaur", 4, "Grass", 20, 20, False)
vulpix = Pokemon("Vulpix", 4, "Fire", 20, 20, False)
oddish = Pokemon("Oddish", 4, "Grass", 20, 20, False)
psyduck = Pokemon("Psyduck", 4, "Water", 20, 20, False)
growlithe = Pokemon("Growlithe", 4, "Fire", 20, 20, False)
poliwag = Pokemon("Poliwag", 4, "Water", 20, 20, False)
bellsprout = Pokemon("Bellsprout", 4, "Grass", 20, 20, False)
ponyta = Pokemon("Ponyta", 4, "Fire", 20, 20, False)
slowpoke = Pokemon("Slowpoke", 4, "Water", 20, 20, False)
exeggcute = Pokemon("Exeggcute", 4, "Grass", 20, 20, False)

pokemon_list = [charmander, squirtle, bulbasaur, vulpix, oddish, psyduck, growlithe, poliwag, bellsprout, ponyta, slowpoke, exeggcute]

