b = input("Write something:")

if  b.isdigit():
 if  int(b) % 2 == 1:
    print("This is a number")
    print("Is odd")


 if b.isdigit():
    if int(b) % 2 == 0:
        print("This is a number")
        print("Is even")


else:
    print("This is a word")
    print(len(b))














