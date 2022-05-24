def fizzbuzz_line(num: int) -> str:
    if num % 15 == 0:
        return "FizzBuzz"
    if num % 5 == 0:
        return "Buzz"
    if num % 3 == 0:
        return "Fizz"
    return str(num)


def fizzbuzz_game(upper_lim: int):
    for i in range(1, upper_lim + 1):
        print(fizzbuzz_line(i))


def get_int(prompt: str = "Input number: ") -> int:
    user = ''
    while not user.isdigit():
        user = input(prompt)
    return int(user)


def clr():
    print("\n" * 100)


play = ''
while play != 'q':
    clr()
    fizzbuzz_game(get_int("Enter maximum: "))
    play = input("\nPlay again or q to quit: ")
