from Cart import Cart


def main():
    print("Create own shopping cart (CREATE) or test current data source (TEST)? ")
    response_1 = input("-> ")
    finished = False
    # User is able to select their own shopping cart
    if response_1 == "CREATE":
        current_basket = Cart()
        shopping_cart = {'A': 0, 'B': 0, 'C': 0, 'D': 0}

        print("Item: A, Price: £50, Special Price: 3 for £140")
        print("Item: B, Price: £35, Special Price: 2 for £60")
        print("Item: C, Price: £25")
        print("Item: D, Price: £12")
        while not finished:
            # Enter a item
            print("Select an item to add to the basket. (A/B/C/D)")
            item = input("-> ")
            # Error check for item input
            if item not in shopping_cart.keys():
                print("---Need to enter a valid item (A/B/C/D)---")
                continue
            # Enter the units for that item
            print("How many units?")
            try:
                current_basket.add_item(item, int(input("-> ")))
            except ValueError as ve:
                print("---Must enter a positive number!---")
                continue
            # Adding an item
            print("Add another item? (YES/NO)")
            response_2 = input("-> ")

            if response_2 == "NO":
                finished = True
            else:
                continue

        print(current_basket.calculate_subtotal())

    # Testing data
    elif response_1 == "TEST":
        current_basket = Cart()
        test_code = [{"code": "A", "quantity": 3}, {"code": "B", "quantity": 3}, {"code": "C", "quantity": 1},
                     {"code": "D", "quantity": 2}]

        current_basket.add_entire_basket(test_code)

        print(current_basket.calculate_subtotal())


main()
