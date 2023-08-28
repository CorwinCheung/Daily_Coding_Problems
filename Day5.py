

# This is a functional programming and closures problem
# Basically, cons is returning a function pair that has f as the argument and returns f(a,b)

# Therefore to get the first element, we need to call pair <- cons(a,b) on another function, either the lambda
# or return_first to get the resulr of return_first(a,b) which we can just set to a in this example


def car(pair):
    def return_first(a, b):
        return a
    # return pair(return_first)
    return pair(lambda x, y: x)


def cdr(pair):
    def return_second(a, b):
        return b
    # return pair(return_second)
    return pair(lambda x, y: y)

# car = car, cdr = cudder, cons = cons


def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


def main():
    print(cons(3, 4))
    print(car(cons(3, 4)))
    print(cdr(cons(3, 4)))


#looking into the signature type, where things are stored. 
# >>> def cons(a, b):
# ...     def pair(f):
# ...         return f(a, b)
# ...     return pair
# ...
# >>> cons(42, 81)
# <function cons.<locals>.pair at 0x11b46f048>
# >>> pair_42_81 = cons(42, 81)
# >>> pair_42_81.__closure__
# (<cell at 0x11b3c02b8: int object at 0x10f59a750>, <cell at 0x11b3c05b8: int object at 0x10f59ac30>)
# >>> pair_42_81.__closure__[0].cell_contents
# 42
# >>> pair_42_81.__closure__[1].cell_contents
# 81

main()
