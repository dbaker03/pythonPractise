#LEGB

# Local - what is passed locally to a function
# Enclosed - when a function is defined within another function we don't have to pass variables to the sub-function
# Global - anything defined globally, on baseline
# Built-in - built in variables such as __name__

x = 10

l = lambda x: x * 2

print(l(2))
print(x * 2)


def outer(x):
    def inner():
        print(x)
    inner()


outer.inner('hi')

outer('hi')


def type(x):
    return 'string maybe?'


print(type(5))
# we have our own local version of a variable which python looks to first as it's a more inner scope
