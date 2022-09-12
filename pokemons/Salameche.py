from pokemons.Pokemon import Hero


class Salameche(Hero):

    def __init__(self, name: str):
        super().__init__(name)
        self.spells = ['Bite', 'Fireblaster', 'Fireheal']

    def fireheal(self):
        return Hero.heal(self, self.spells[2], 10)

    def bite(self, target):
        return Hero.attack(self, self.spells[0], target, 15)

    def fireblaster(self, target):
        return Hero.attack(self, self.spells[1], target, 20)
