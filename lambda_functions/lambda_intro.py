def add_plus_one(num1, num2):
    return num1 + num2 + 1

print(add_plus_one(3, 7))

# Lambda (or anonymous) functions

addition = lambda num1, num2: num1 + num2 + 1

print(addition(5, 8))

# map
savings = [234.65, 330.00, 54.23, 8490.50]
# bonus = savings with 10% added on

bonus = []
for saving in savings:
    bonus.append(saving * 1.1)

print(savings)
print(bonus)


def apply_bonus(saving):
    return saving * 1.1


bonus_map = map(apply_bonus, savings)
print(bonus_map)

# map spits out an iterable

print(next(bonus_map))
print(next(bonus_map))

for b in bonus_map:
    print(b)

# we can convert it straight into a list

bonus_map = list(map(apply_bonus, savings))

bonus_lambda = list(map(lambda x: x * 1.1, savings))

total = sum(bonus_lambda)

squared_bonus = map(lambda x: x ** 2, bonus_lambda)

print(list(f"{sb:.2f}" for sb in squared_bonus))  # we can have flat loops

numbers = [1, 2, 3, 4, 5, 6, 7]

squared_plus_three = list(map(lambda x: (x ** 2) + 3, numbers))
print(squared_plus_three)

squared_plus_three = map(lambda x: (x ** 2) + 3, numbers)
print(list(squared_plus_three))
print(list(squared_plus_three))  # note the object disappears as we have used it

squared_plus_three = map(lambda x: (x ** 2) + 3, numbers)
print(next(squared_plus_three))
print(list(squared_plus_three))  # the first value has disappeared as it's been used



evens = list(filter(lambda x: x % 2 == 0, numbers))
# will be a filter object like map object, so we have to convert to list or next()
print(evens)



jobs = ['Data analyst', 'C# developer', 'Data engineer', 'devops engineer', 'data architect']
filtered = filter(lambda x: 'data' in x.lower(), jobs)
mapped_split = map(lambda x: x.split(' ')[-1], filtered)
print(list(mapped_split))

filtered = filter(lambda x: 'data' in x.lower(), jobs)
mapped_replace = map(lambda x: x.replace('Data', '').replace('data', '').strip().capitalize(), filtered)
print(list(mapped_replace))
# remove data and Data then strip to remove blank spaces left at start and end of string then capitalize first letter

the_bool = False
res = "yes" if the_bool else "no"  # conditional operator (pythons version of ?)



