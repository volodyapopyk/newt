# Use generator
n = int(input("Write something:"))
def fib(n):
    a = 0
    b = 1
    for item in range(n):
        c = a + b
        a = b
        b = c
    yield b
for k in range(n):
    print(next(fib(k)))

#Use iterator
class MyIterator:

    def __init__(self, max= 10000):
        self.new = max
        self.a = 0
        self.b = 1


    def __iter__(self):
        return self


    def __next__(self):
        if self.new == 0:
            raise StopIteration

        self.new -= 1

        c = self.a + self.b
        self.a = self.b
        self.b = c

        return self.a

look = MyIterator(n)

for item in look:
    print(item)

#Use Recursion

def fibonacci(n):
    if n < 2 :
        return n
    return fibonacci(n-1) + fibonacci(n-2)

c = fibonacci(n)

for item in range(n):
    print(fibonacci(item))

#fakturial

def fakturial(n):
    if n < 1:
        return 1
    return n * fakturial(n-1)
lol = fakturial(n)
print(lol)