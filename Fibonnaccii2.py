# Use generator
n = int(input("Write something:"))
def fib(n):
    a = 1
    b = 0
    for item in range(n):
        c = a + b
        a = b
        b = c
    yield b

print(next(fib(n)))

#Use iterator
class MyIterator:

    def __init__(self, max= 10000):
        self.n = max
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self


    def __next__(self):
        if self.n == 0:
            raise StopIteration

        self.n -= 1

        c = self.a + self.b
        self.a = self.b
        self.b = c

        return self.a

look = list(MyIterator(n))
print(look[-1])

# #Use Recursion
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

c = fibonacci(n)
print(c)

#fakturial
def fakturial(n):
    if n < 1:
        return 1
    return n * fakturial(n-1)
lol = fakturial(n)
print(lol)