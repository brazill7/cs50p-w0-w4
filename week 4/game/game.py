from random import randint
import sys

def getInput(text):
    while True:
        try:
            inp = int(input(text))

            if inp > 0:
                return inp
            else:
                pass
        except:
            pass


def main():
    #get level#
    level = getInput("Level: ")
    #set randint#
    randomNumber = randint(1, level)

    #continue until correct guess
    while True:
        #get guess#
        guess = getInput("Guess: ")

        if guess == randomNumber:
            print("Just right!")
            sys.exit()
        elif guess > randomNumber:
            print("Too large!")
        elif guess < randomNumber:
            print("Too small!")

main()