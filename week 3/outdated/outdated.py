def numberReFactor(x,y,z):
    try:
        x = int(x)
        y = int(y)
        z = int(z)
    except:
        return

    c = ""
    b = ""
    a = z

    while True:
        if x > 12:
            c = x
            b = y
        else:
            if y < 32:
                b = x
                c = y
            else:
                break
        if x > 12 and y > 12:
            break
        #all is good
        break
    #pad 0s
    b = str(b)
    c = str(c)

    if len(b) == 1:
        b = "0" + b
    if len(c) == 1:
        c = "0" + c
    #print ISO
    print(f"{a}-{b}-{c}")

###

def letterReFactor(x,y,z):
    a = x.lower()
    b = y
    c = z

    #decode a
    months = [
        "january",
        "february",
        "march",
        "april",
        "may",
        "june",
        "july",
        "august",
        "september",
        "october",
        "november",
        "december"
    ]

    for i,month in enumerate(months):
        if a == month:
            a = (i + 1)
            break
    a = str(a)
    #pad a and b
    if len(b) == 1:
        b = "0" + b
    if len(a) == 1:
        a = "0" + a


    print(f"{c}-{a}-{b}")


###
def main():
    noComma = False
    while True:
        inp = input("Date: ")

        if "/" in inp:
            x,y,z = inp.split("/")
            try:
                if int(x) > 12 or int(y) > 31:
                    pass
                else:
                    numberReFactor(x,y,z)
                    break
            except:
                pass
        else:
            x,y,z = inp.split(" ")
            if "," in y:
                y = y.replace(',','')
            else:
                noComma = True

            try:
                if int(y) > 31:
                    pass

                else:
                    if not noComma:
                        letterReFactor(x, y, z)
                        break
                    else:
                        pass
            except:
                pass

#run
main()