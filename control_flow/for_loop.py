alphabet = ['a','b','c','d','e']

print(alphabet)

alphabet_upper = []
for letter in alphabet:
    alphabet_upper.append(letter.upper())

print(alphabet_upper)

nest = [[1,2,3],[4,5],[6,7]]

for sublist in nest:
    print(sublist)
    for number in sublist:
        print(number)



hi = "Hello Word!"

print(hi)
wordList = []
for c in hi:
    print(c)
    wordList.append(c)

print(wordList)



car = {"toyota":"yaris",
       "ford":"focus",
       "hyundai":"i30",
       "vw":"golf"}
for model in car:#same as putting .keys()
    print(model)

#when we iterate through a dictionary it spits out the keys by default, we can specify that we want values

for model in car.values():
    print(model)

for model in car.items():#spits out tuples
    print(model)

for make, model in car.items():#unpack tuples
    print(f"Made by {make} is a {model}")

t = (10, 50)
a, b = t
#we can unpack tuples by assigning to multiple values at once



for x in range(0,10):
    print(f"number {x}")

for x in range(10):
    print(f"number {x}")
#range inclusive lower bound, not inclusive upper


lst = ['a','b','c']
for i, letter in enumerate(lst):
    print(f"letter {letter} is number {i}")