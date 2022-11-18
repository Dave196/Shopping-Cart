
Pricing = {'A': {"unitPrice": '50', "specialPrice": True},
           'B': {"unitPrice": '50', "specialPrice": True},
           'C': {"unitPrice": '50', "specialPrice": False},
           'D': {"unitPrice": '50', "specialPrice": False}
           }

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
        print("Item: B, Price: £35, Special Price:3 for £140")
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

    # Pre-selected data is used to compute the subtotal
    elif response_1 == "No":
        print("Using pre-selected data source")


main()
