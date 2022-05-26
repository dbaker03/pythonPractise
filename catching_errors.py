try:
    file = open("order.txt")
except FileNotFoundError as errmsg:
    print("There was an error")
    print(errmsg)
    raise  # this will do the things in the except then raise the error again
except KeyError:
    print("Error")

print("Bottom")