class Dog:
    def __init__(self, dog_name, colour):  # initialization
        self.animal_type = 'canine'
        self.legs = 4
        self.name = dog_name
        self.colour = colour

    animal_type = 'canine'  # class variable

    def bark(self):  # method
        return f"Woof! I am a {self.animal_type}"


fido = Dog('fido', 'black')  # instanciation - creating an instance of the class
print(fido.animal_type)
print(fido.bark())


Dog.animal_type = "arachnid"


class Spartan:
    def __init__(self, fname, lname, dob, client=None):
        self.first_name = fname
        self.last_name = lname
        self.dob = dob
        self.client = client
        self.status = 'In Training'

    def graduate(self):
        self.status = 'Working with client'
        print('Hurray!')


dan = Spartan('dan', 'baker', '2003-05-11', 'Home Office')
print(dan.status)
dan.graduate()
# Spartan.graduate() would apply changes to all existing instances
# dan.dob = '11-05-2003' changes only dan's dob
# but Spartan.dob = '12-03-2000' changes all new and existing instances

konrad = Spartan(  # can declare in long format which makes it more readable
    fname='konrad',
    lname='qwerty',
    dob='11-23-4555'
)


class Car:
    def __init__(self, make, model, top_speed, colour=None):
        self.make = make
        self.model = model
        self.top_speed = top_speed
        self.colour = colour
        self._speed = 0

    def accelerate(self, amount):
        self._speed = min(self._speed + amount, self.top_speed)

    def brake(self, amount):
        self._speed = max(self._speed - amount, 0)

    # getter
    def get_speed(self):
        return self._speed


tonya = Car('Toyota', 'Yaris', 140)
print(tonya.get_speed())
tonya.accelerate(70)
print(tonya.get_speed())
tonya.brake(30)
print(tonya.get_speed())
tonya.brake(100)
print(tonya.get_speed())

# abstraction - take away detail, view from a higher level and make things easier
#   eg user doesn't need to worry about logic of maximum speed
#   we don't worry how .append() works we just know how to use it
#   same with toaster we don't know how it works we just use it
# encapsulation - hide away things
#   we hid away the speed because we protect it
#   In a toaster the user can choose exact current they use the knob to adjust heat
