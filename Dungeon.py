'''
GOOD WHEEL:
Spin Bad Wheel
Gain 16 Power
Gain 8 Power
Other Players Spin Bad Wheel
Double your Power
Gain 4 Power
Gain 10 Power
Take 5 power from anyone
Get A Random Tier 1 Item

BAD WHEEL:
Die
Go Home
Sing for a WHOLE FRICKING 20 Seconds or lose all your power, gold, and go back home
-10 Gold
-10 Power
Spin Good Wheel
Monster Appears
Choose any square to teleport too
dellorkciR teG

BUTTON WHEEL:
Spin Good Wheel
All Space Fill with Enemies
Lose 5 Power
Nothing Happens
Teleport
Spin Bad Wheel
Halve Your Power
Gain 5 Power
Battle a Player
Double your Power
Swap All Characters

SHOP (location: Home):
Tier 3 Items(5 G):
PWR Potion! +10 Pwr
Teleport Device(Other Person) - Move any player

Tier 2 Items(3 G):
Teleport Device
Good Wheel Spin
Steroids +10 Pwr for the next fight(temporary)

Tier 1 Items(1 G):
 +1 PWR
Rob the bank +1 G
TP Any player to you
Take another turn

Demon:
Every 5 turns summon new monsters on the board

Attack System:
Winning and Losing is a probability proportional to power of enemy and player.
Ex: Player 1 has 5 power, Enemy (Demon) has 10 Power. Roll the probability. 33% Player 1 wins. 

Casino:
Double it or lose it
Blackjack against the house

Move System:
Can move once per turn unless they bought an extra turn from the shop.
'''
import random
from colored import Fore, Back, Style

class Player:
    def __init__(self, name):
        self.name = name
        self.power = 10
        self.gold = 10
class Game:
    def __init__(self):
        self.players = []
        self.current_player_index = 0
        self.demon_turn_counter = 0 
        self.enemies = {
            "Wizard": {"Power": 40},
            "Goblin1": {"Power": 7}, 
            "Goblin2": {"Power": 5},
            "Rat": {"Power": 1},
            "Golem": {"Power": 10},
            "Dragon": {"Power": 50},
            "Orc": {"Power": 15},
            "Troll": {"Power": 10}, 
            "Skeleton": {"Power": 4},
            "Zombie": {"Power": 3},
            "Mummy": {"Power": 6},
            "Vampire": {"Power": 20},
            "Werewolf": {"Power": 25},
            "Giant Spider": {"Power": 8},
            "Slime": {"Power": 2}
        }           

    def add_player(self, player):
        self.players.append(player)

    def next_turn(self):
        self.current_player_index = (self.current_player_index + 1)
        if self.current_player_index > len(self.players): self.current_player_index=0

    def spin_good_wheel(self):
        options = ["Spin Bad Wheel", 
                   "Gain 16 Power",
                   "Gain 8 Power",
                   "Other Players Spin Bad Wheel",  
                   "Double your Power", 
                   "Gain 4 Power",
                   "Gain 10 Power",
                   "Take 5 power from anyone",
                   "Get A Random Tier 1 Item"] 
        result = random.choice(options)
        print(f"{self.name} spun the good wheel and got: {result}")
        if result == "Gain 16 Power":
            self.power += 16
        elif result == "Gain 8 Power":
            self.power += 8 
        # And so on implementing the effects of each option

    def spin_bad_wheel(self):
        options = ["Die",  
                   "Go Home", 
                   "Sing for a WHOLE FRICKING 20 Seconds or lose all your power, gold, and go back home",
                   "-10 Gold",
                   "-10 Power",
                   "Spin Good Wheel",
                   "Monster Appears",
                   "Choose any square to teleport too"]
        result = random.choice(options)
        print(f"{self.name} spun the bad wheel and got: {result}")
        if result == "-10 Gold":
            self.gold -= 10
        # And so on implementing the effects of each option

    def button_wheel(self):
        # Implement actions for the button wheel
        pass

    def move_player(self, player, steps):
        # Implement player movement logic
        pass

    def check_demon(self):
        self.demon_turn_counter += 1
        if self.demon_turn_counter % 5 == 0:
            self.spawn_demon()

    def spawn_demon(self):
        enemy_name, enemy_stats = random.choice(list(self.enemies.items()))
        pass

    def attack(self, player, enemy):
        # Implement attack system
        pass

    def casino_game(self):
        # Implement casino game logic (e.g., blackjack)
        pass

    def buy_item(self, player, item):
        # Implement item purchasing logic
        pass

    def run_game(self):
        # Main game loop
        while True:
            current_player = self.players[self.current_player_index-1]
            # Game logic goes here based on player actions
            # Example: ask for player action, perform action, switch player turn
            self.next_turn()


game = Game()
while True:
    try:
        players = int(input('How many players would like to play? '))
    except ValueError:
        print('Cronge, ur so bad, put in a legit numero pls or u cant play.')
    else:
        if players > 5:
            print("Sorry, only 5 players can play at a time")
        elif players < 0:
            print("Wtf is wrong w/ u. Negativ Players! Srsly, ur stoopid!")
    for i in range(players):
        game.players.append(input(f'Name of Player {i+1}: '))
        i+=1
    break
for i in game.players:
    m="  "*game.players.index(i)
    print(m+i)
print(f"These {len(game.players)} players are about to embark on a journey that \ntries any man's will and durability, don't die!")
game.run_game()
