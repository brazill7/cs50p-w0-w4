while True:
        inp = input("Fraction: ")
        x = ""
        y = ""
        afterDivide = False

        for num in inp:
            if not afterDivide:
                if num == "/":
                    afterDivide = True
                else:
                     x += num
            else:
                y += num
        try:
            x = int(x)
            y = int(y)
            z = round((x / y * 100))

            if x > y:
                print("error: more than 100%")
                break
            match z:
                case 0:
                    print("E")
                case 1:
                    print("E")
                case 99:
                    print("F")
                case 100:
                    print("F")
                case other:
                    print(f"{z}%")
            break
        except:
            pass