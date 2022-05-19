h = "Hello World!"

double = "Double Quotes"
single = 'Single quotes'

print(double, single)

string_block = """
everything
is
text
a
a
a
a
a   dddd


"""


print(h[6])
print(h[-2])

print(h[2:7])#slicing, goes upto not including final index

print(h[3:8])
print(h[3:-4])##same as above (can count backwards in a range
print(h[:-4])
print(h[3:])

print(h[1:-1:3])#start to end every third char
print(h[4::2])#4th to end every 2nd char

print(h[::-1])#whole string backwards



#Methods (belong to objects) similar to functions

print(type(h))
print(h.lower())

#count - how many times a string apprears in a string eg 3 l's in a word
#strip - removes all whitespace at start and end of string by default or just the characters specified
#upper - makes all charaters upper case
#capitalize - makes first letter a capital
#replace - swaps any instance of old for new, if count is given then only the first if count is 1 etc

s = "hhhello h world"
print(s.capitalize())
print(s.strip('h'))
print(s.replace('o', 'ooo'))
print(s.replace('o', 'ooo', 1))#only first instance



print("\n\n\n\n\n")



sent = "hello world. acb. yes"
list = sent.split(". ")
print(list)

new = ". ".join(s.capitalize() for s in list)
print(new)



#concatenation

a = "Mr"
b = "Blue"
c = "Sky"
d = 5

print(a, b, c, d)
print(f"{a} {b} {c}")


theFloat = 3.49597
print(f"rounded {theFloat:.2f}")

score = 16
max_score = 26

print(f"You have scored {score/max_score*100}")
print(f"You have scored {score/max_score:%}")
print(f"You have scored {score/max_score:.2%}")
