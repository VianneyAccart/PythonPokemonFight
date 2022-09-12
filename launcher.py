from sys import exit

from pokemons.Carapuce import Carapuce
from pokemons.Pokemon import random_draw_to_determine_first_player, display_pokemons_healpoints
from pokemons.Salameche import Salameche

if __name__ == '__main__':

    print('>> WELCOME TO POKEMON ARENA <<')

    player_one: str = ''
    player_two: str = ''
    fight_round: int = 1

    while player_one not in '12' or len(player_one) != 1:
        player_one = input(f'Player 1, choose your Pokemon : [1] Carapuce, [2] Salameche : '
                           )

        if player_one not in '12' or len(player_one) != 1:
            print('Invalid choice...')

        if player_one == '1':
            carapuce = Carapuce('Carapuce')
            player_one_pokemon = carapuce
            print(f'Player 1 choose {carapuce.name}')
        if player_one == '2':
            salameche = Salameche('Salameche')
            player_one_pokemon = salameche
            print(f'Player 1 choose {salameche.name}')

    while player_two not in '12' or len(player_two) != 1:
        player_two = input(f'Player 2, choose your Pokemon : [1] Carapuce, [2] Salameche : '
                           )

        if player_two not in '12' or len(player_two) != 1:
            print('Invalid choice...')

        if player_two == '1':
            carapuce = Carapuce('Carapuce')
            player_two_pokemon = carapuce
            print(f'Player 2 choose {carapuce.name}')
        if player_two == '2':
            salameche = Salameche('Salameche')
            player_two_pokemon = salameche
            print(f'Player 2 choose {salameche.name}')

    print('Let the battle begin ! A draw is held to determine which player will play first...')

    if random_draw_to_determine_first_player():
        print('Player 1 will play first')
    else:
        print('Player 2 will play first')



    while (player_one_pokemon.health | player_two_pokemon.health) > 0:

        print(f'[ROUND {fight_round}]')

        action = input(
            f'It\'s {salameche.name} turn. Spells : [1] Bite (-15), [2] Fireblaster (-20), [3] Heal (+10) : '
        ).upper()
        if action not in "123" or len(action) != 1:
            print("Action not recognized. You should decide between 1, 2 or 3.")
            continue
        if action == '1':
            salameche.bite(carapuce)
            display_pokemons_healpoints(player_one_pokemon, player_two_pokemon)
        if action == '2':
            salameche.fireblaster(carapuce)
            display_pokemons_healpoints(player_one_pokemon, player_two_pokemon)
        if action == '3':
            salameche.fireheal()
            display_pokemons_healpoints(player_one_pokemon, player_two_pokemon)
        if carapuce.health <= 0:
            exit()

        action = input(
            f'It\'s {carapuce.name} turn. Spells : [1] Bite (-10), [2] Waterjet (-25), [3] Aquaheal (+10) : '
            ).upper()
        if action not in "123" or len(action) != 1:
            print("Action not recognized. You should decide between 1, 2 or 3.")
            continue
        if action == '1':
            carapuce.bite(salameche)
            display_pokemons_healpoints(player_one_pokemon, player_two_pokemon)
        if action == '2':
            carapuce.waterjet(salameche)
            display_pokemons_healpoints(player_one_pokemon, player_two_pokemon)
        if action == '3':
            carapuce.aquaheal()
            display_pokemons_healpoints(player_one_pokemon, player_two_pokemon)
        if salameche.health <= 0:
            exit()

        fight_round += 1
