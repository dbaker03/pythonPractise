x = 0

while x < 10:
    print(f"While loop running: {x}")
    x += 1

print("end")

age_int = None
keep_asking = True

while keep_asking:
    age = input("Enter age: ")
    if age.isdigit():
        age_int = int(age)
        keep_asking = False
    else:
        print("Enter a number")

print(f"Your age is {age_int}")