import random
import sys


print('=' *38)
print('#####jeu de rôle dans le terminal#####')
print('=' *38)

player = input('Quel est votre pseudo ? ')
potion = 3
player_lifepoints = 50
ennemy_lifepoints = 50
ennemy = 'ennemy'

while True :
    try :
        choice = int(input('Souhaitez-vous attaquer🔪 (1) ou utiliser une potion🧪 (2) ?'))
        potion_health = random.randrange(15, 51)
        player_attack = random.randrange(5, 11)
        ennemy_attack = random.randrange(5, 16)
        if choice != 1 and choice != 2: 
            raise ValueError()
    except ValueError:
        print(' \n', '~' *50, ' \n')
        print('Il faut taper 1 ou 2!!')
        print(' \n', '~' *50, ' \n')
        continue

    if choice == 1 :
        player_lifepoints = player_lifepoints - ennemy_attack
        ennemy_lifepoints = ennemy_lifepoints - player_attack
        print(' \n', '~' *50, ' \n')
        print(f'{player} a infligé {player_attack} points de dégâts à l\'ennemi')
        print(f'l\'ennemi a infligé {ennemy_attack} points de dégâts à {player}\n')
        print(f'Il reste {player_lifepoints} points de vie à {player}!!!')
        print(f'Il reste {ennemy_lifepoints} points de vie à l\'ennemi!!!')
        print(' \n', '~' *50, ' \n')
        if player_lifepoints <= 0 or ennemy_lifepoints <= 0 :
            if player_lifepoints <= 0 :
                print(f'l\'ennemi a gagné, dommage {player} ')
            elif ennemy_lifepoints <= 0 :
                print(f'{player} a gagné, bravo {player} ')
            print ('partie terminée❌')
            sys.exit()

    elif choice == 2 : 
        if potion<=3 and  potion > 0 :
            player_lifepoints += potion_health
            potion -= 1
            print(f'{player} gagne {potion_health} points de vie, {player} a désormais {player_lifepoints} points de vie')
            player_lifepoints -= ennemy_attack
            print(' \n', '~' *50, ' \n')
            print('Vous passez votre tour...\n')
            print(f'l\'ennemi a infligé {ennemy_attack} points de dégâts à {player}\n')
            player_lifepoints -= ennemy_attack
            print(f'l\'ennemi a infligé {ennemy_attack} points de dégâts à {player}\n')
            print(f'Il reste {player_lifepoints} points de vie à {player}!!!')
            print(f'Il reste {ennemy_lifepoints} points de vie à l\'ennemi!!!')
            print(' \n', '~' *50, ' \n')
        elif potion == 0 :
            potion = 0
            potion_health = 0
            print(' \n', '~' *50, ' \n')
            print(f'{player} n\'a plus de potions ')
            print(' \n', '~' *50, ' \n')
        if player_lifepoints <= 0 or ennemy_lifepoints <= 0 :
            if player_lifepoints <= 0 :
                print(f'L\'ennemi a gagné, dommage {player} ')
            elif ennemy_lifepoints <= 0 :
                print(f'{player} a gagné, bravo {player} ')
            print ('partie terminée❌')
            print(' \n', '~' *50, ' \n')
            sys.exit()