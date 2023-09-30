
def non_optimized(num):

    def recurse(num):
        if num == 0:
            return 1
        ways = 0
        if num % 10 > 0:
            ways += recurse(num // 10)
        if num % 100 <= 26 and num % 100 >= 10:
            ways += recurse(num // 100)
        return ways

    return recurse(num)

# like in the Fibonacci sequence, split the string into the number of ways you can split
# taking off the last letter like floor of dividing by 10, with the edge case of 0 and flooring
# of dividing by 100 if the last two could be a letter in the alphabet, use the base case of 0 return 1 case.
# The time complexity of this solution is roughly O(2^n), because for each additional digit you
# add onto the string, you must consider two times as many letter decoding combinations


def optimized(num):
    substrings = {}

    def recurse(n):
        if n in substrings:
            return (substrings[n])
        else:
            if n == 0:
                return 1
            ways = 0
            if n % 10 > 0:
                ways += recurse(n//10)
            if n % 100 <= 26 and n % 100 >= 10:
                ways += recurse(n//100)
            substrings[n] = ways
            return ways
    return recurse(num)

# use the same logic but each time you complete a substring n from recurse, store it to a
# dictionary called substrings and then check if you have a memoized version of the substring
# to save on time complexity
# The time complexity of this function is worst case O(n) since each of the substrings are stored
# so in the worst case scenario, the function runs through all of the substirngs. If it reaches an
# already computed substring it returns and does not have to run more computations.


def main():
    # calculates ways to decode
    num = 102111123123112312312312113111231
    print(non_optimized(num))

    print(optimized(num))


main()
