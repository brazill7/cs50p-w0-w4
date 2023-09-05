def to_snake(camel):
    outputStr = ""

    for char in camel:
        ascii = ord(char)

        if ascii < 97:
            outputStr += "_"
            outputStr += char.lower()
        else:
            outputStr += char

    print(outputStr)


inp = input("Camel Case: ")

to_snake(inp)