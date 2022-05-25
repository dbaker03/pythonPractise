class Location:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        return f"Location(latitude: {self.latitude}, longitude: {self.longitude})"

    def __str__(self):
        return f"({self.latitude}, {self.longitude})"


class Dog:
    def __init__(self, age):
        self.age = age

    def __str__(self):
        return f"a {self.age} year old dog"

    def __format__(self, format_spec):
        if format_spec == 'dog':
            return f"A {self.age * 7} year old dog"
        else:
            return self.__str__()


bham_academy = Location(52.488647, -1.887249)
print(bham_academy)

fido = Dog(5)
print(fido)
print(f"Fido is a {fido:dog}")
