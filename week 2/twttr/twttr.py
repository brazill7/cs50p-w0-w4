def removeVowels(word):
    for char in word:
        if char in "AEIOUaeiou":
            word = word.replace(char, "")

    print(word)

inp = input("Input: ")
removeVowels(inp)