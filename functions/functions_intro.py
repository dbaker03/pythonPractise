#DRY Don't Repeat Yourself
#default values possible
def greeting(name="youuuuu"):
    return"Hello" + name


print(greeting("Dan"))

#type hints
def greeting2(name : str):
    """returns name for greeting"""
    print(name)


greeting("s")

#can also put hints for output
def division(denom: int, num: int) -> float:
    return denom/num


#Good function
#Clear name - obvious what it does - lower snake case
#Clear argument names - maybe use type hints or even put the type as part of argument name
#Keep them small, break big functions into lots of smaller ones
#Comments to keep code clear
#Document functions """this function does this"""
#Type hints arguments and output

def fizzbuzz_line(num: int) -> str:
    if num % 15 == 0:
        return "FizzBuzz"
    if num % 5 == 0:
        return "Buzz"
    if num % 3 == 0:
        return "Fizz"
    return(str(num))

def fizzbuzz_game():
    for i in range(1,101):
        print(fizzbuzz_line(i))
        