from pokemons.Pokemon import Hero


class Carapuce(Hero):

    def __init__(self, name: str):
        super().__init__(name)
        self.spells = ['Bite', 'Waterjet', 'Aquaheal']

    def aquaheal(self):
        return Hero.heal(self, self.spells[2], 10)

    def bite(self, target):
        return Hero.attack(self, self.spells[0], target, 10)

    def waterjet(self, target):
        return Hero.attack(self, self.spells[1], target, 25)
