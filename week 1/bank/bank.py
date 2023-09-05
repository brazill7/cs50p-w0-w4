
def check(g):
    if "hello" in g:
        return "$0"
    elif g.startswith("h"):
        return "$20"
    else:
        return "$100"

inp = input("Greeting: ").lower()

print(check(inp))