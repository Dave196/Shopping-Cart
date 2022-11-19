from Cart import Cart


def main():
    print("Create own shopping cart (CREATE) or test current data source (TEST)? ")
    response_1 = ""
    while (response_1 != "CREATE") and (response_1 != "TEST"):
        response_1 = input("-> ")

    # User is able to select their own shopping cart
    if response_1 == "CREATE":
        finished = False
        current_basket = Cart()
        shopping_cart = {'A': 0, 'B': 0, 'C': 0, 'D': 0}

        # Manually update the catalog if there price changes
        print("Item: A, Price: £50, Special Price: 3 for £140")
        print("Item: B, Price: £35, Special Price: 2 for £60")
        print("Item: C, Price: £25")
        print("Item: D, Price: £12")
        while not finished:
            # Enter a item
            print("Select an item to add to the basket. (A/B/C/D)")
            item = input("-> ")
            # Error check for item input
            if item not in ['A', 'B', 'C', 'D']:
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
            response_2 = ""
            while (response_2 != "YES") and (response_2 != "NO"):
                response_2 = input("-> ")

            if response_2 == "NO":
                print("Would you like to edit your basket? (YES/NO)")
                for item in current_basket.basket:
                    print("Item: [{}] Unit Price: [£{}] Quantity: [{}] ".format(item["code"],
                                                                                current_basket.pricing[item["code"]][
                                                                                   "unitPrice"], item["quantity"]))
                response_3 = ""
                while (response_3 != "YES") and (response_3 != "NO"):
                    response_3 = input("->")

                if response_3 == "YES":
                    edit_loop = True
                    while edit_loop:
                        print("Item to edit or add? (A/B/C/D)")
                        item_to_edit = input("->")
                        print("The new quantity?")

                        try:
                            new_quantity = int(input("->"))
                        except ValueError as ve:
                            print("---Must enter a positive number!---")
                            continue

                        current_basket.edit_basket(item_to_edit, new_quantity)

                        for item in current_basket.basket:
                            print("Item: [{}] Unit Price: [£{}] Quantity: [{}] ".format(item["code"], current_basket.
                                                                                  pricing[item["code"]]
                                                                                  ["unitPrice"], item["quantity"]))

                        print("Would you like to edit another item (YES/NO)")
                        response_4 = ""
                        while (response_4 != "YES") and (response_4 != "NO"):
                            response_4 = input("->")

                        if response_4 == "YES":
                            continue
                        elif response_4 == "NO":
                            edit_loop = False

                    finished = True
                else:
                    finished = True
            else:
                continue

        output, subtotal = current_basket.calculate_subtotal()
        print(output)

    # Testing data
    elif response_1 == "TEST":
        current_basket = Cart()
        test_code = [{"code": "A", "quantity": 3}, {"code": "B", "quantity": 3}, {"code": "C", "quantity": 1},
                     {"code": "D", "quantity": 2}]

        current_basket.add_entire_basket(test_code)

        output, subtotal = current_basket.calculate_subtotal()
        print(output)


main()
