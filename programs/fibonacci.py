def fibnacci(n, fib={1: 0, 2: 1}):
    #####Complexity O(n) time and O(n) space
    if (n in fib):
        return fib[n]
    else:
        fib[n] = fibnacci(n - 1, fib) + fibnacci(n - 2, fib)
        return fib[n]
    pass

z = fibnacci(4)
print(z)
