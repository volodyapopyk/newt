import time
import sys
a = " "
while True:
    for new in a:
        a = input("\nWrite something:")
        if a.isdigit():
            if int(a) % 2 == 0:
                print(f'\nThis is a number')
                print(f'Is even')
            else:
                print(f'\nThis is a number')
                print(f'Is odd')

        elif a.isalpha():
            if a.isupper():
                print(f'\nThis is a text')
                print(f'It is a сapital letter')

            elif a.islower():
                print(f'\nThis is a text')
                print(f'It is a small letter')

        elif a.isascii():
                    print('\nThis is a symbol')

        c = input("\nDo you want to continue? [Y/N] or another program [a]:")
        if c == ("Y"):
            continue
        if c == "a":
            while True:
                print("I love Python")
                time.sleep(4.2)
        else:
                print("\n Bye ")
                sys.exit()
















