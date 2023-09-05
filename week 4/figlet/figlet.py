from pyfiglet import Figlet
import sys


if len(sys.argv) < 3 or len(sys.argv) > 3:
    if len(sys.argv) == 1:
        f = Figlet(font='standard')
    else:
        print("Invalid usage")
        sys.exit()
else:
    if not sys.argv[1] == '-f' or sys.argv[1] == '--font':
        print("Invalid usage")
        sys.exit()

    arg = sys.argv[2]

    try:
        f = Figlet(font=arg)
    except:
        print("Invalid usage")
        sys.exit()

inp = input("Input: ")


print(f.renderText(inp))

