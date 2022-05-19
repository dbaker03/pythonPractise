name = input("What is your name? ")
age = input("How old? ")
height = input("How tall? ")


if(int(age) > 18):
    result = "more than"
else:
    result = "less than"

print(f"\nHello, {name.capitalize()} you are {float(height):.2f}m tall and are {result} 18 years old")