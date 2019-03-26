# fib without memoization; take a lot of time to compute after number 35 if we put in for loop - range(120)

def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

#print("fib(11) = ", fib(11))

""" for i in range(121):
    print('fib(' + str(i) + ') = ', fib(i)) """

# fib with memoization - storing fib of a number in memo and look up
def fastFib(n, memo = {}):
    #assumes n is integer >=0
    if n == 0 or n == 1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result = fastFib(n-1, memo) + fastFib(n-2, memo)
        memo[n] = result
        return result
    
for i in range(5):
    print('fib(' + str(i) + ') = ', fastFib(i))

