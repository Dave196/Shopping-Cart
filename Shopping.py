def calculator(data):
    pricing = {'A': {"unitPrice": 50, "specialPrice": True},
               'B': {"unitPrice": 35, "specialPrice": True},
               'C': {"unitPrice": 25, "specialPrice": False},
               'D': {"unitPrice": 12, "specialPrice": False}
               }
    sub_total = 0

    for item in data:
        # Standard subtotal calculation for each item
        sub_total += item["quantity"] * pricing[item["code"]]["unitPrice"]
        # Special Price check for item
        if pricing[item["code"]]["specialPrice"]:
            if item["code"] == 'A' and item["quantity"] >= 3:
                # Floor division applied to attain the value to discount
                sub_total -= (item["quantity"] // 3) * 10
                print("Special price Discount for A applied!")
            elif item["code"] == 'B' and item["quantity"] >= 2:
                sub_total -= (item["quantity"] // 2) * 10
                print("Special price Discount for B applied!")

    final_output = "\nSUBTOTAL = £{}".format(str(sub_total))

    return final_output


Test_code = [{"code": "A", "quantity": 3}, {"code": "B", "quantity": 3}, {"code": "C", "quantity": 1},
             {"code": "D", "quantity": 2}]


def main():
    print("Would you like to select your shopping cart? (Yes/No)")
    response_1 = input("-> ")
    finished = False
    # User is able to select their own shopping cart
    if response_1 == "Yes":
        shopping_cart = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
        print("Item: A, Price: £50, Special Price:3 for £140")
        print("Item: B, Price: £35, Special Price:2 for £60")
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
            print("Add another item? (Yes/No)")
            response_2 = input("-> ")

            if response_2 == "No":
                finished = True
            else:
                continue

        print(shopping_cart)

    # Testing data
    elif response_1 == "No":
        print("Testing")
        print(calculator(Test_code))


main()
