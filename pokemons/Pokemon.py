import random


def _apply_critical_effect(modifier: int):
    return modifier * 2


def random_draw_to_determine_first_player():
    chance = (random.randint(1, 2))
    if chance == 1:
        return True
    else:
        return False


def display_pokemons_healpoints(pokemon_one, pokemon_two):
    print(f'[INFO] Remaining healpoints : {pokemon_one.name} : {pokemon_one.health}/100, {pokemon_two.name} : {pokemon_two.health}/100')


class Hero:
    critical_strike_chance: int = 20
    health: int = 100

    def __init__(self, name: str):
        self.name: str = name
        self.spells: list = []

    def attack(self, spell_name: str, target, damages: int):

        critical: bool = False

        if self._is_critical():
            critical = True
            damages = _apply_critical_effect(damages)

        if critical:
            print(f'{self.name} uses {spell_name} (critical) and inflicts -{damages} to {target.name}.')
        else:
            print(f'{self.name} uses {spell_name} and inflicts -{damages} to {target.name}.')

        target.health -= damages
        target.pokemon_is_dead()

    def heal(self, spell_name: str, restored_points: int):
        print(f'{self.name} uses {spell_name} and retrieves {restored_points} hps.')
        if self._is_critical():
            restored_points = _apply_critical_effect(restored_points)

        self.health += restored_points
        if self.health > 100:
            self.health = 100
        self.pokemon_is_dead()

    def _is_critical(self):
        chance = (random.randint(1, 100))
        if chance <= self.critical_strike_chance:
            return True
        else:
            return False

    def pokemon_is_dead(self):
        if self.health <= 0:
            print(f'{self.name} is KO !')
