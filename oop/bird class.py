class Bird:
    def __init__(self, species, colour, can_fly=True):
        self.species = species
        self.colour = colour
        self.wings = 2
        self.can_fly = True
        self._age = 0

    def reproduce(self):
        if self._age < 2:
            return "Too young"
        else:
            return "Laying eggs..."

    def age_up(self, years=1):
        self._age += years

    def get_age(self):
        return self._age


# Instantiate an object
bird = Bird('Sparrow', 'Brown')

# Call method
bird.age_up()
bird.age_up()
bird.age_up()
egg = bird.reproduce()


class Penguin(Bird):
    def __init__(self, subspecies, colour=('Black', 'White')):
        super().__init__('Penguin', colour, False)
        self.species = subspecies

    def hunt_for_fish(self):
        return 'Splash'


class Emperor(Penguin):
    def __init__(self):
        super().__init__('Emperor', ('Black', 'White', 'Yellow'))


class LittlePenguin(Penguin):
    def __init__(self):
        super().__init__('Little', ('Blue', 'White'))


little_blue = LittlePenguin()
print(little_blue.reproduce())
little_blue.age_up(3)
print(little_blue.reproduce())
