file = open("order.txt")

print(file, type(file))
orders = file.readlines()
print(orders)
file.close()


# we want our orders without the newline characters
orders = list(map(lambda x: x.replace('\n', ''), orders))  # strip() \n counts as whitespace so that would've worked
print(orders)

# when we read we might want to:
# lines = list(map(lambda x: x.strip(), file.readlines()))

# this will automatically close the file once we go back to the baseline

with open("order.txt") as file:
    raw_orders = file.readlines()
    orders = list(map(lambda x: x.strip(), raw_orders))

# .readline() - reads one line
# .read() - reads whole file as a string

file = open("order.txt")
whole_file = file.read()
orders = whole_file.split('\n')
# another way to get a list of the lines

file.close()

# with open("order.txt", 'w') as file:
#     file.write("String to write")
# now opened in write mode - it overwrites the whole file also if the file doesn't already exist write will create it

with open("order.txt", 'a') as file:  # this is in append mode - adds onto the file
    file.write("String to write\n")
    file.writelines(['cheese\n', 'ketchup\n', 'dough\n'])
