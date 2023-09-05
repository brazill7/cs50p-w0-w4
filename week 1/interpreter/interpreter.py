def math(x,y,z):
    x = int(x)
    y = y.strip(" ")
    z = int(z)

    match y:
        case "+":
            return print(float(x + z))
        case "-":
            return print(float(x - z))
        case "*":
            return print(float(x * z))
        case "/":
            return print(float(x / z))
        case other:
            return print("Error")

x, y, z = input("Expression: ").split()
math(x,y,z)