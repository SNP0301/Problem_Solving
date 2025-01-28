"""
"""
T = int(input())
for _ in range(T):
    N = int(input())
    fib_zero = [0 for _ in range(41)]
    fib_one = [1 for _ in range(41)]
    fib_zero[0] = 1
    fib_zero[1] = 0
    fib_one[0] = 0
    fib_one[1] = 1
    for i in range(2,41):
        fib_zero[i] = fib_zero[i-1] + fib_zero[i-2]
        fib_one[i] = fib_one[i-1] + fib_one[i-2]
    print(fib_zero[N],fib_one[N])