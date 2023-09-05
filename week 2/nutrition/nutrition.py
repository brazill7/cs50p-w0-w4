def calories(fruit):
    fruit = fruit.lower()
    match fruit:
        case "apple":
            print("Calories: 130")
        case "avocado":
            print("Calories: 50")
        case "sweet cherries":
            print("Calories: 100")
        case "kiwifruit":
            print("Calories: 90")
        case "pear":
            print("Calories: 100")
        case _:
            print("")



inp = input("Item: ")
calories(inp)
