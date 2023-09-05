def checkValidation(plate):
    plateLength = len(plate)
    invalid = False
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"

    while True:
        #check for length
        if plateLength < 2 or plateLength > 6:
            invalid = True
            break
        #check for first 2 letters
        if not plate[0] in letters and plate[1] in letters:
            invalid = True
            break
        #check for middle numbers
        for i, num in enumerate(plate[2: -2:]):
            if num in numbers:
                invalid = True
                break
        #check for 0 as the first letter
        for i, num in enumerate(plate):
            if num == "0":
                if i > 0:
                    if not plate[i - 1] in numbers:
                        invalid = True
                        break
        break

    if invalid:
        print("Invalid")
    else:
        print("Valid")
#main#
plate = input("Plate: ")
checkValidation(plate)