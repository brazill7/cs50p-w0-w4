menu = {
    "baja taco": 4.00,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "quesadilla": 8.50,
    "super burrito": 8.50,
    "super quesadilla": 9.50,
    "taco": 3.00,
    "tortilla salad": 8.00
}

totalPrice = 0

while True:
    try:
        inp = input("Item: ").lower()
        try:
            price = menu[inp]
            totalPrice += price
            print(f"Total: ${totalPrice}0")
        except:
            pass
    except:
        break
