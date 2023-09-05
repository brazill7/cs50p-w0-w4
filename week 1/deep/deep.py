def check(ans):
    if (ans == "42" or ans == "forty-two" or ans == "forty two"):
        return "Yes"
    else:
        return "No"

inp = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip(" ").lower()

print(check(inp))