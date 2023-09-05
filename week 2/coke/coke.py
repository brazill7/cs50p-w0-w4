def sell_coke():
    coke_price = 50

    while True:
        inp = int(input("Insert Coin: "))

        if inp == 5 or inp == 10 or inp == 25:
            coke_price -= inp

        if coke_price <= 0:
            print(f"Change Owed: {abs(coke_price)}")
            break

        print(f"Amount Due: {coke_price}")

#
sell_coke()