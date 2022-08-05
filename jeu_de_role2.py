#!/usr/bin/env python3

#Thanks to Thibh, the best Python teacher I know (French Language)
#https://www.docstring.fr/blog/
#Follow Thibh on Twitter : @DocstringFr
#This script come from https://www.youtube.com/watch?v=2r04G8qj6Bw
# same

from random import randint

health_player, health_ennemy = 50, 50
available_choices = ["1", "2"]
stock_potion = 3
menu = "souhaitez-vous attaquer (1) ou utiliser une potion (2) ?"
skip_turn = False

print('''\n Règles du jeu :
    - le jeu comporte 2 joueurs. 
    - chaque joueur dispose de 50 points de vie chacun.
    - vous disposez de 3 potions pour récupérer des points de vie, aucune pour l'ennemi.
    - chaque potion permet de récupérer un nombre aléatoire de point de vie compris entre 15 et 50.
    - votre attaque inflige à l'ennemi des dégats aléatoires compris entre 5 et 10 points de vie.
    - l'attaque de l'ennemi vous inflige des dégats aléatoires compris entre 5 et 15 points vie.
    - Lorsque vous utilisez une potion, vous sautez votre tour.
    ''')

while health_ennemy > 0 and health_player >0:
    damage_player = randint(5, 10)
    damage_ennemy = randint(5, 15)

    if not skip_turn and (user_choice := input(menu)) in available_choices:          # be carefull with operator precedence
        if user_choice == "1":
            print(f"Vous avez infligé {damage_player} points de dommage à l'ennemi")
            health_ennemy -= damage_player
        elif user_choice =="2":
            if stock_potion == 0:
                print("vous n'avez plus de potion...")
            else:
                potion_points = randint(15, 50)
                health_player += potion_points
                stock_potion -= 1
                skip_turn = True
                print(f"vous récupérez {potion_points} points de vie ({stock_potion} potion(s) restante)")
    elif skip_turn:
        print("vous passez votre tour")
        skip_turn = False
    else:
        print("Svp, Faites un choix valide")
    
    print(f"L'ennemi vous a infligé {damage_ennemy} points de dommages")
    health_player -= damage_ennemy

    print(f"il vous reste {health_player} points de vie.")
    print(f"L'ennemi a encore {health_ennemy} points de vie.")
    print( "-" * 60)

if health_ennemy <= 0:
    print("bravo !\nVous avez gagné !\nFin du jeu")
else:
    print("Dommage !\nVous avez perdu.")
