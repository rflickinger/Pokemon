from pokemon import Pokemon
from pokemon import pokemon_list
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
        if self.team[self.active].max_health > self.team[self.active].current_health:
            if self.potions >= 1:
                self.potions = self.potions -1
                print(f"{self.name} used a potion on {self.team[self.active].name}.")
                self.team[self.active].gain_health(20)
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
    def attack_trainer(self, victim):
        if self.team[self.active].ko == True:
            print(f"{self.team[self.active].name} has fainted and cannot battle, switch Pokemon!")
            return
        if victim.team[victim.active].ko == True:
            print(f"{victim.team[victim.active].name} has fainted and cannot battle, switch Pokemon!")
            return
        self.team[self.active].attack(victim.team[victim.active])
    
    #Makes team creation easier
    def make_team(self, choices):
        i = 0
        pokemon1 = Pokemon("", 0, "", 0, 0, True)
        pokemon2 = Pokemon("", 0, "", 0, 0, True)
        pokemon3 = Pokemon("", 0, "", 0, 0, True)
        pokemon4 = Pokemon("", 0, "", 0, 0, True)
        pokemon5 = Pokemon("", 0, "", 0, 0, True)
        pokemon6 = Pokemon("", 0, "", 0, 0, True)
        temp_pokemon_dict = {0: pokemon1, 1: pokemon2, 2: pokemon3, 3: pokemon4, 4: pokemon5, 5: pokemon6}
        while i < 6:
            temp_pokemon_dict[i] = Pokemon(pokemon_list[choices[i]].name, pokemon_list[choices[i]].level, pokemon_list[choices[i]].type, pokemon_list[choices[i]].max_health, pokemon_list[choices[i]].current_health, pokemon_list[choices[i]].ko)
            self.team.append(temp_pokemon_dict[i])
            i+= 1
        print("Team Created!")
        print(f"You have chosen: {self.team[0].name}, {self.team[1].name}, {self.team[2].name}, {self.team[3].name}, {self.team[4].name}, and {self.team[5]}!")

#Creating trainers and their teams
ryan = Trainer("Ryan", [], 0, 3)
ryan.make_team([6, 7, 8, 9, 10, 11])
gary = Trainer("Gary", [], 0, 3)
gary.make_team([0, 1, 2, 3, 4, 5])    

#Commence battle testing
ryan.attack_trainer(gary)
ryan.attack_trainer(gary)
ryan.attack_trainer(gary)
ryan.attack_trainer(gary)
gary.use_potion()
ryan.switch(4)
ryan.attack_trainer(gary)
ryan.attack_trainer(gary)
ryan.attack_trainer(gary)
