#!/usr/bin/env python3

#Thanks to Thibh, the best Python teacher I know (French Language)
#https://www.docstring.fr/blog/
#Follow Thibh on Twitter : @DocstringFr
#This script come from https://www.youtube.com/watch?v=2r04G8qj6Bw

import random
from typing import List

class Player:
    def __init__(self, name: str, health: int = 50, number_of_flasks: int = 3):
        self.name = name
        self.health = health
        self.number_of_flasks = number_of_flasks

    def __str__(self):
        return f"{self.name} : ({self.health} points de vie)"

    @property
    def damage(self) -> int: 
        return random.randint(1, 10)

    @damage.setter
    def damage(self, value: int) -> int:
        raise ValueError("vous ne pouvez pas modifier les points de vie")

    def attack(self, ennemy: "Player") -> str:
        damage_inflicted = self.damage
        ennemy.health -= damage_inflicted
        print(f"{self.name}, vous avez infligé {damage_inflicted} points de vie à {ennemy.name}")
        return damage_inflicted

    def take_flask(self) -> bool:
        #s'il n'y a plus de potion
        if not self.number_of_flasks:                                
            print("\n  * Désolé, vous ne pouvez plus prendre de potion car elles ont toutes été utilisées !")
            return False

        flask_health = random.randint(5, 50)
        self.health += flask_health
        number_of_flasks = self.number_of_flasks
        self.number_of_flasks -= 1
        print(f"\n {self.name} a récupéré {flask_health} points de vie et il lui reste {self.number_of_flasks} potions\n")
        return True

def _show_instructions(player: Player, ennemy: Player):
    print('''\n Règles du jeu :
    - le jeu comporte 2 joueurs. 
    - chaque joueur dispose de 50 points de vie chacun.
    - vous disposez de 3 potions pour récupérer des points de vie, aucune pour l'ennemi.
    - chaque potion permet de récupérer un nombre aléatoire de point de vie compris entre 15 et 50.
    - votre attaque inflige à l'ennemi des dégats aléatoires compris entre 5 et 10 points de vie.
    - l'attaque de l'ennemi vous inflige des dégats aléatoires compris entre 5 et 15 points vie.
    - Lorsque vous utilisez une potion, vous sautez votre tour.
    ''')

def _create_players() -> List[Player]:
    name_player_1 = input("entrez votre nom :")
    name_player_2 = input("entrez le nom de votre adversaire :")
    return Player(name=name_player_1), Player(name=name_player_2, number_of_flasks=0)

def _start_game(player: Player, ennemy: Player):
    skip_turn = False
    #on boucle tant que le joueur ou l'ennemi ont des points de vie
    while player.health > 0 and ennemy.health > 0:                   
        if skip_turn:
            print("\n vous passez votre tour")
            ennemy.attack(player)
            skip_turn = False
            print(f"{player} après avoir sauté votre tour.")
            continue

        action = input("\n -> quelle est votre action ? (1: Attaquer / 2: prendre une potion): ")

        #On attaque
        if action == "1":                                                                    
            player.attack(ennemy)

        #On prend une potion
        elif action == "2":                                          
            if player.take_flask():
                #passer un tour
                skip_turn = True
        
        #Attaque de l'ennemi
        ennemy.attack(player)
        print(player)
        print(ennemy)

    print(f"bravo, {player.name if player.health > 0 else ennemy.name} à gagné !")

def start(show_instructions: bool = True):
    player, ennemy = _create_players()
    if show_instructions:
        _show_instructions(player, ennemy)
    _start_game(player, ennemy)

if __name__ == '__main__':
    start()