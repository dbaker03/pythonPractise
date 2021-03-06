print("\nQ1a\n")
# Q1a: Write a function which takes in an integer as an argument and returns the divisors of that number as a list
# e.g. f(12) = [1, 2, 3, 4, 6, 12]
# hint: range(1, n) returns a collection of the numbers from 1 to n-1

# A1a:
def factors(target : int):
    result = []
    for num in range(1, target + 1):
        if target % num == 0:
            result.append(num)
    return result

print("\nQ1b\n")
# Q1b: Write a function which takes in two integers as arguments and returns true if one of the numbers
# is a factor of the other, false otherwise
# (bonus points if you call your previous function within this function

# A1b:
def isFactor(int1: int, int2: int):
    if int1 in factors(int2):
        return True
    if int2 in factors(int1):
        return True
    return False
# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: write a function which takes a letter (as a string) as an input and outputs it's position in the alphabet
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
"n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

# A2a:
def alph_pos(letter: str) -> int:
    for i in range(len(alphabet)):
        if alphabet[i] == letter:
            return int(i)

print("\nQ2b\n")
# Q2b: create a function which takes a persons name as an input string and returns an
# ID number consisting of the positions of each letter in the name
# e.g. f("bob") = "1141" as "b" is in position 1 and "o" is in position 14

# A2b:
def id(name: str):
    the_id = ''
    for letter in name.lower():
        the_id += str(alph_pos(letter))
    return the_id

print("\nQ2c\n")
# Q2c: Create a function which turns this ID into a password. The function should subtract
# the sum of the numbers in the id that was generated from the whole number of the id.
# e.g. f("bob") -> 1134 (because bob's id was 1141 and 1+1+4+1 = 7 so 1141 - 7 = 1134)

# A2c:
def password(name: str):
    total = 0
    for letter in id(name):
        total += int(letter)
    return int(id(name)) - total
# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Write a function which takes an integer as an input, and returns true if the number is prime, false otherwise.
def is_prime(target: int):
    facts = factors(target)
    if len(facts) <= 2:
        return True
    return False
# A3a:

print("\nQ3b\n")
# Q3b: Now add some functionality to the function which does not error if the user inputs something other than a digit

# A3b:
def is_prime_no_error():
    target = ''
    while not target.isdigit():
        target = input("Enter number to check if prime: ")
    print(is_prime(int(target)))
# -------------------------------------------------------------------------------------- #
is_prime_no_error()