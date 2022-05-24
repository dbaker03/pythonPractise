from time import sleep

play = ""
while play != 'q':
    last = ''
    while not last.isdigit():
        last = input("Enter maximum: ")

    for x in range(1, int(last) + 1):
        if x % 5 == 0 and x % 3 == 0:
            print("Fizz Buzz")
        elif x % 3 == 0:
            print("Fizz")
        elif x % 5 == 0:
            print("Buzz")
        else:
            print(x)
        sleep(0.1)

    play = input("\nPress enter to continue, q to quit: ")
    print("\n" * 100)
