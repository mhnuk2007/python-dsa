n = 15

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...

def fib_loop(n):
    a,b = 0, 1
    for i in range(n+1):
        print(i, ":", a)
        a, b = b, a + b

fib_loop(n)

def fib_loop_nth(n):
    
    a,b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

print(f'{n}th term of Fibonacci series using loop is', fib_loop_nth(n))


def fib_rec(n):
    a, b = 0, 1
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        return fib_rec(n-1) + fib_rec(n-2)

print(f'{n}th term of Fibonacci series using recursion is {fib_rec(n)}')
    
    