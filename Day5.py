

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


def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


def main():
    print(cons(3, 4))
    print(car(cons(3, 4)))
    print(cdr(cons(3, 4)))


main()
