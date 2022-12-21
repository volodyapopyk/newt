phonebook = {}
while True:
    print(f"\n""\033[34m{}".format("1)Stats"),"\033[33m{}".format("2)Add"),"\033[34m{}".format("3)Delete"),"\033[33m{}".format("4)List"), "\033[34m{}".format("5)Show"),"\033[33m{}".format("6)Close"))
    input_hello = input("\033[1m\033[34m\033[40m{}\033[0m".format("Chose a command:"))

    if input_hello == "Stats":
        print("\033[1m\033[33m\033[40m{}\033[0m".format(len(phonebook)))

    elif input_hello == "Add":
        key = input("\033[1m\033[34m\033[40m{}\033[0m".format("Write name:"))
        if phonebook.get(key) is not None:
            print("\033[1m\033[33m\033[40m{}\033[0m".format("!!!You cannot overwrite recordings!!!"))
        value = input("\033[1m\033[34m\033[40m{}\033[0m".format("Write number:"))
        phonebook[key] = value


    elif input_hello == "Delete":
        input_hello = input("Write name:")
        del phonebook[input_hello]

    elif input_hello == "List":
        print(phonebook.keys())

    elif input_hello == "Show":
        input_hello = input("Write name:")

        if input_hello in phonebook:
            print(phonebook.get(input_hello))

    elif input_hello == "Close":
        print("\033[1m\033[33m\033[40m{}\033[0m".format("!!!GOOD BYE!!!"))
        break
