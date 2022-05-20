from time import sleep

while True:
    max = int(input("Enter maximum: "))
    for x in range(1, max + 1):
        if x % 5 == 0 and x % 3 == 0:
            print("Fizz Buzz")
        elif x % 3 == 0:
            print("Fizz")
        elif x % 5 == 0:
            print("Buzz")
        else:
            print(x)
        sleep(0.1)

    input("Press enter to continue...")
    print("\n" * 100)
