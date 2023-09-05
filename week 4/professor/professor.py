from random import randint
import sys

def getLevel():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                return level
            else:
                pass
        except:
            pass
###
def askQuestion(level):
    match level:
        case 1:
            lower = 0
            upper = 9
        case 2:
            lower = 10
            upper = 99
        case 3:
            lower = 100
            upper = 999


    numOfWrong = 0
    randOne = randint(lower, upper)
    randTwo = randint(lower, upper)
    cAns = (randOne + randTwo)

    while True:
        try:
            ans = int(input(f"{randOne} + {randTwo} = "))
            if ans > 3:
                pass

            if ans == cAns:
                if numOfWrong == 0:
                    return True
                else:
                    return False
            else:
                print("EEE")
                if numOfWrong == 2:
                    print(f"{randOne} + {randTwo} = {cAns}")
                    return False
                else:
                    numOfWrong += 1
                pass

        except:
            print("EEE")
            if numOfWrong == 2:
                print(f"{randOne} + {randTwo} = {cAns}")
                return False
            else:
                numOfWrong += 1
                pass

def main():
    totalScore = 0

    l = getLevel()

    for i in range(10):
        c = askQuestion(l)

        if c:
            totalScore += 1

    print(f"Score: {totalScore}")
    sys.exit()


main()
