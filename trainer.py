from pokemon import Pokemon
from pokemon import pokemon_list
class Trainer:
    def __init__(self, name, team, active, potions):
        self.name = name
        self.team = team
        self.active = active
        self.potions = potions
    def __repr__(self):
        return f"Name: {self.name}\nPokemon:\n{self.team[0]}\n{self.team[1]}\n{self.team[2]}\n{self.team[4]}\n{self.team[5]}\nCurrently selected Pokemon is {self.team[self.active]}\nPotions: {self.potions}"
    
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
print(ryan)
# #Set up user trainer
# user_name = input("Hello Trainer! What is your name?")
# user_choices = []
# iterato = 0
# while iterato > 6
#     user_choices.append(int(input("Please enter your Pokemon value, check the README for instructions!")))
#     iterato += 1
# print(f"Thanks {user_name}, one moment while we collect your Pokemon!")
# user_trainer = Trainer(user_name, [], 0, 3)
# user_trainer.make_team(user_choices)

# #Choose trainer to battle
# trainer_choice = input("Great! Who would you like to battle? Enter \"Ryan\" or \"Gary\". Be careful, this is case sensitive!")
# chosen_trainer = 0
# if trainer_choice = "Ryan":
#     chosen_trainer = 1
#     print("Great choice!")


