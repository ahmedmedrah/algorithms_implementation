## iterative method
def fib_itr(n):
    n1 = 0
    n2 = 1
    f = n1+n2
    for i in range(n):
        f = n1+n2
        n1 = n2
        n2 = f
    return f
fib_itr(100)



## recursive method
def fib_rec(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return fib_rec(n-2) + fib_rec(n-1)
fib_rec(100)