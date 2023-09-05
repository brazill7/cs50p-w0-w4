def main():
    listOfPeople = []

    while True:
        #error catching
        try:
            inp = str(input("Name: "))
        except:
            break

        #check for the end
        if len(inp) < 2:
            break
        else:
            listOfPeople.append(inp)

    #after they're done inputting names
    outputNames = ""
    lastName = ""

    #1 person
    if len(listOfPeople) ==  1:
        name = listOfPeople[0]
        print(f"Adieu, adieu, to {name}")
    #2 people
    elif len(listOfPeople) == 2:
        firstName = listOfPeople[0]
        secondName = listOfPeople[1]

        print(f"Adieu, adieu, to {firstName} and {secondName}")
    #more than 3 people
    else:
        for i, people in enumerate(listOfPeople):
            if i == (len(listOfPeople) - 1):
                lastName =  people
            else:
                outputNames += people + ', '

        print(f"Adieu, adieu, to {outputNames}and {lastName}")


main()