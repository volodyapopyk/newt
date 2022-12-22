phonebook = {}
while True:
    print(f"\n"f"\033[34m{'1)Stats'}",f"\033[33m{'2)Add'}",f"\033[34m{'3)Delete'}",f"\033[33m{'4)List'}", f"\033[34m{'5)Show'}",f"\033[33m{'6)Close'}")
    input_hello = input(f"\033[1m\033[34m\033[40m{'Chose a command:'}\033[0m")

    if input_hello == "Stats":
        print("\033[1m\033[33m\033[40m{}\033[0m".format(len(phonebook)))

    elif input_hello == "Add":
        key = input(f"\033[1m\033[34m\033[40m{'Write name:'}\033[0m")
        if phonebook.get(key) is not None:
            print(f"\033[1m\033[33m\033[40m{'!!!You cannot overwrite recordings!!!'}\033[0m")
        else:
            value = input(f"\033[1m\033[34m\033[40m{'Write number:'}\033[0m")
            phonebook[key] = value


    elif input_hello == "Delete":
        input_hello = input(f"\033[1m\033[34m\033[40m{'Write name:'}\033[0m")
        if input_hello in phonebook:
            del phonebook[input_hello]
        else:
            print("Error")

    elif input_hello == "List":
        print(phonebook.keys())

    elif input_hello == "Show":
        input_hello = input(f"\033[1m\033[34m\033[40m{'Write name:'}\033[0m")
        if input_hello in phonebook:
            print(phonebook.get(input_hello))

    elif input_hello == "Close":
        print(f"\033[1m\033[33m\033[40m{'!!!GOOD BYE!!!'}\033[0m")
        break
