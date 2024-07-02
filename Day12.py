import time
#Return number of ways to go up N number of steps with step sizes 1 or 2
def naive_recursion(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    return naive_recursion(n-1) + naive_recursion(n-2)

cache = [0 for i in range(1000)]
def memoized_recursion(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif cache[n] != 0:
        return cache[n]
    else:
        cache[n] = memoized_recursion(n-1) + memoized_recursion(n-2)
        return cache[n]
    
def iterative(n):
    a, b = 1, 2
    for _ in range(n-1):
        a, b = b, a + b
    return(a)

def generalized(n, X):
    cache = [0 for i in range(n+1)]
    cache[0] = 1
    for i in range(1, n + 1):
        # cache[i] = sum(cache[i-x] for x in X if i-x >= 0)
        cache[i] = 0
        for x in X:
            if i-x >= 0:
                cache[i] += cache[i-x]
    return cache[n]

def main():
    start = time.time()
    print(naive_recursion(30))
    end = time.time()
    print("time computed: " + str(end - start))
    
    start = time.time()
    print(memoized_recursion(30))
    end = time.time()
    print("time computed: " + str(end - start))

    print(iterative(4))

    print(generalized(4, [1,2]))
main()