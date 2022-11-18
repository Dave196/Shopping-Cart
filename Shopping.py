def calculator(data):
    pricing = {'A': {"unitPrice": 50, "specialPrice": True},
               'B': {"unitPrice": 35, "specialPrice": True},
               'C': {"unitPrice": 25, "specialPrice": False},
               'D': {"unitPrice": 12, "specialPrice": False}
               }
    sub_total = 0

    for item in data:
        # Standard subtotal calculation for each item
        price = item["quantity"] * pricing[item["code"]]["unitPrice"]
        sub_total += price
        discounted_amount = 0
        # Special Price check for item using floor division
        if pricing[item["code"]]["specialPrice"]:
            if item["code"] == 'A' and item["quantity"] >= 3:
                discounted_amount = (item["quantity"] // 3) * 10
                sub_total -= discounted_amount
                print("---Special price discount for A applied!---")

            elif item["code"] == 'B' and item["quantity"] >= 2:
                discounted_amount = (item["quantity"] // 2) * 10
                sub_total -= discounted_amount
                print("---Special price discount for B applied!---")

        # Print statements showing the basket prices
        if item["quantity"] > 0:
            if pricing[item["code"]]["specialPrice"]:
                print("Item: [{}] Quantity: [{}] Non Discounted Price: [£{}] Discounted Price: [£{}]".format(item["code"],
                                                                                                    item["quantity"],
                                                                                                    price,
                                                                                                    price - discounted_amount))
            else:
                print("Item: [{}] Quantity: [{}] Price: [£{}]".format(item["code"], item["quantity"], price))








    final_output = "\nSUBTOTAL = £{}".format(str(sub_total))

    return final_output


def main():
    print("Create own shopping cart (CREATE) or test current data source (TEST)? ")
    response_1 = input("-> ")
    finished = False
    # User is able to select their own shopping cart
    if response_1 == "CREATE":
        shopping_cart = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
        readable_shopping_cart = []

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
                shopping_cart[item] += int(input("-> "))
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

        readable_shopping_cart.append({"code": "A", "quantity": shopping_cart["A"]})
        readable_shopping_cart.append({"code": "B", "quantity": shopping_cart["B"]})
        readable_shopping_cart.append({"code": "C", "quantity": shopping_cart["C"]})
        readable_shopping_cart.append({"code": "D", "quantity": shopping_cart["D"]})

        print(readable_shopping_cart)

        print(calculator(readable_shopping_cart))

    # Testing data
    elif response_1 == "TEST":
        test_code = [{"code": "A", "quantity": 3}, {"code": "B", "quantity": 3}, {"code": "C", "quantity": 1},
                     {"code": "D", "quantity": 2}]
        print(calculator(test_code))


main()
