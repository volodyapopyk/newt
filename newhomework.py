import time
#1
# def my_generator(func):
#     def new():
#         func()
#     return new
#
# @my_generator
# def my_function():
#     print("my_function")
#     print(time.strftime('%H'':''%M'))
# my_function()


#2
# class MyCustomException(Exception):
#     pass
# raise MyCustomException("Custom exception is occured")
#

# #3
# class CtxManager:
#
#     def __enter__(self):
#         print('==========')
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('==========')
#
#     try:
#         print(2/0)  #example error
#     except Exception as zde:
#         print(f'Your Error is {zde}')
#         input("Write Enter for exit:")
#
# with CtxManager() as new:
#     print("Some text")


#4
# try:
#     print('==========')
# except Exception as zde:
#     print(f'Your Error is {zde}')
# else:
#     print('==========')
# finally:
#     input("Write Enter for exit:")
#

### The First Homework ###
# try:
#     #===========================
#     c = "I Love Python\n" *42
#     print()
#     #===========================
#     age_in_mounth = 12*24
#     print(age_in_mounth, end="\n\n")
#     #===========================
#     age_in_years = int(age_in_mounth/12)
#     print(age_in_years)
#     #===========================
#     name = "Volodymyr"
#     my_age = "\nMy name is " + name + ", I'm "+str(age_in_years) + " year old\n"
#     print(my_age)
#     #===========================
#     a=1
#     b=2
#     c=a==b
#     print(c)
#     c=a>b
#     print(c)
#     c=a<b
#     print(c)
#     c=b>=a
#     print(c)
#     c=b<=a
#
#     print(c, end="\n\n")
#     #===========================
#     a = 2
#     b = 5
#     c = 6
#     d = str(a)+str(b)+str(c)
#     print(d)
#     results=type(d)
#     print(results)
#     #===========================
#
# except Exception as zde:
#     print(f'Your Error is {zde}')
### The  Second Homework ###
# try:
#     b = input("Write something:") # for example error add int before input
# except Exception as zde:
#     print(f'Your Error is {zde}')
# else:
#     if  b.isdigit():
#      if  int(b) % 2 == 1:
#         print("This is a number")
#         print("Is odd")
#
#      if b.isdigit():
#         if int(b) % 2 == 0:
#             print("This is a number")
#             print("Is even")
#
#     else:
#         print("This is a word")
#         print(len(b))

### The Thirty Homework ###

#todo " i dont know where i can put try except else bcs my program don show any error"

# phonebook = {}
# while True:
#     print(f"\n"f"\033[34m{'1)Stats'}",f"\033[33m{'2)Add'}",f"\033[34m{'3)Delete'}",f"\033[33m{'4)List'}", f"\033[34m{'5)Show'}",f"\033[33m{'6)Close'}")
#     input_hello = input(f"\033[1m\033[34m\033[40m{'Chose a command:'}\033[0m")
#
#     if input_hello == "Stats":
#         print("\033[1m\033[33m\033[40m{}\033[0m".format(len(phonebook)))
#
#     elif input_hello == "Add":
#         key = input(f"\033[1m\033[34m\033[40m{'Write name:'}\033[0m")
#         if phonebook.get(key) is not None:
#             print(f"\033[1m\033[33m\033[40m{'!!!You cannot overwrite recordings!!!'}\033[0m")
#         else:
#             value = input(f"\033[1m\033[34m\033[40m{'Write number:'}\033[0m")
#             phonebook[key] = value
#
#
#     elif input_hello == "Delete":
#         input_hello = input(f"\033[1m\033[34m\033[40m{'Write name:'}\033[0m")
#         if input_hello in phonebook:
#             del phonebook[input_hello]
#         else:
#             print("Error")
#
#     elif input_hello == "List":
#         print(phonebook.keys())
#
#     elif input_hello == "Show":
#         input_hello = input(f"\033[1m\033[34m\033[40m{'Write name:'}\033[0m")
#         if input_hello in phonebook:
#             print(phonebook.get(input_hello))
#
#     elif input_hello == "Close":
#         print(f"\033[1m\033[33m\033[40m{'!!!GOOD BYE!!!'}\033[0m")
#         break
#
### The Fourth Homework ###
#todo " i dont know where i can put try except else bcs my program don show any error"

# import time
# while True:
#     a = input("\nWrite something:")
#     for new in a:
#         if a.isdigit():
#             if int(a) % 2 == 0:
#                 print(f'\nThis is a number')
#                 print(f'Is even')
#             else:
#                 print(f'\nThis is a number')
#                 print(f'Is odd')
#
#         elif a.isalpha():
#             if a.isupper():
#                 print(f'\nThis is a text')
#                 print(f'It is a сapital letter')
#
#             elif a.islower():
#                 print(f'\nThis is a text')
#                 print(f'It is a small letter')
#
#         elif a.isascii():
#                 print('\nThis is a symbol')
#
#     c = input("\nDo you want to continue? [Y/N] or another program [a]:")
#     if c == ("Y"):
#         continue
#     if c == "a":
#         while True:
#                 print("I love Python")
#                 time.sleep(4.2)
#     else:
#         print("\n Bye ")
#         break
#
### The Lst Homework ###
#Use generator
# try:
#     n = int(input("Write something:"))
# except Exception as new:
#     print(f'The Error is {new}')
# else:
#     def fib(n):
#         a = 1
#         b = 0
#         for item in range(n):
#             c = a + b
#             a = b
#             b = c
#             yield b
#     for k in fib(n):
#         print(k)
#
#
# Use iterator
# try:
#     n = int(input("Write something:"))
# except ValueError as new:
#         print(f'The Error is {new}')
# else:
#     class MyIterator:
#
#         def __init__(self, max= 10000):
#             self.n = max
#             self.a = 0
#             self.b = 1
#
#         def __iter__(self):
#             return self
#
#         def __next__(self):
#             if self.n == 0:
#                 raise StopIteration
#
#             self.n -= 1
#
#             c = self.a + self.b
#             self.a = self.b
#             self.b = c
#
#             return self.a
#
#     look = list(MyIterator(n))
#     print(look[-1])
# #
# # #Use Recursion
# try:
#     n = int(input("Write something:"))
# except Exception as new:
#     print(f'The Error is {new}')
# else:
#     def fibonacci(n):
#         if n < 2:
#             return n
#         return fibonacci(n-1) + fibonacci(n-2)
#
#     c = fibonacci(n)
#     print(c)
#fakturial
# try:
#     n = int(input("Write something:"))
# except Exception as new:
#     print(f'The Error is {new}')
# else:
#     def fakturial(n):
#         if n < 1:
#             return 1
#         return n * fakturial(n-1)
#     lol = fakturial(n)
#     print(lol)