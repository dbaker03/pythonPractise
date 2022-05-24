def multiArgs(*args): #* makes it multi args - can be any name basically converts inputs into a tuple
    print(args, type(args))


multiArgs(1, 2, 3)


def product(*nums):
    if len(nums) == 0:
        return None
    total = 1
    for number in nums:
        total *= number
    return total


def product2(num1, *nums):#another solution forcing no blank inputs
    total = num1
    for number in nums:
        total *= number
    return total


print(product())
print(product(2, 3, 7))