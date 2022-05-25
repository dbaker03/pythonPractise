from pokemon import Pokemon
from move import Move

class Charmander(Pokemon):
    def __init__(self):
        super().__init__(
            name="Charmander",
            type='Fire',
            hp=7,
            attack=9,
            defence=5
        )
        self.moves.append(Move('Scratch', 'Normal', 10))
        self.moves.append(Move('Growl', 'Normal', 0))

    def use_move(self, move_name) -> (int, str):
        for move in self.moves:
            if move.name == move_name:
                print(f"{self.name} used {move.name}!")
                return (move.power + self.attack, move.type)


class Pikachu(Pokemon):
    def __init__(self):
        super().__init__(
            'Pikachu',
            'Electric',
            hp=6,
            attack=6,
            defecne=6)
        self.moves.append(Move('Thundershock', 'Electric', 20))
        self.moves.append(Move('Tail whip', 'Normal', 0))

if __name__ == "__main__":
    char = Charmander()
    power, type = char.use_move('Scratch') #  remember we can unpack tuples
    print(power)
    print(type)

    print(char.moves) #  prints list of __repr__
    for move in char.moves: #  prints the __str__
        print(move)
