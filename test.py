
import sys


def fib(n):

    a, b, counter = 0, 1, 0
    while counter < n:
        yield a
        a, b = b, a + b
        counter += 1


f = fib(999)
print(sys.getsizeof(f))


# sakdjlkasjdalsjkd

# test2
