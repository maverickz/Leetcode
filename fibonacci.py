def fibonacci(N):
    fib = [0]*N
    fib[1] = 1
    for i in xrange(2, N):
        fib[i] = fib[i-1] + fib[i-2]

    return fib[N-1]


print fibonacci(10)