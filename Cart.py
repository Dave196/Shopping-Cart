class Cart:
    # pricing class data
    pricing = {'A': {"unitPrice": 50, "specialPrice": True, "specialAmount": 3},
               'B': {"unitPrice": 35, "specialPrice": True, "specialAmount": 2},
               'C': {"unitPrice": 25, "specialPrice": False},
               'D': {"unitPrice": 12, "specialPrice": False}
               }

    def __init__(self):
        self.basket = []

    def add_item(self, code: str, quantity: int):
        # Checks if the item is present in the basket
        if any(item["code"] == code for item in self.basket):
            for item in self.basket:
                if item["code"] == code:
                    if quantity > 0:
                        # Adds to the current quantity set
                        item["quantity"] += quantity
                    else:
                        # Removes item if the quantity is set to 0
                        self.basket.remove(item)
        else:
            # Adds the item to the basket
            if quantity > 0:
                self.basket.append({"code": code, "quantity": quantity})

    def add_entire_basket(self, basket: list):
        self.basket = basket

    def edit_basket(self, code: str, quantity: int):
        # Checks if the item is present in the basket
        if any(item["code"] == code for item in self.basket):
            for item in self.basket:
                if item["code"] == code:
                    if quantity > 0:
                        # Replaces the quantity value with the new value
                        item["quantity"] = quantity
                    else:
                        # Removes item if the quantity is set to 0
                        self.basket.remove(item)
        else:
            # Adds the item to the basket
            if quantity > 0:
                self.basket.append({"code": code, "quantity": quantity})

    def calculate_subtotal(self):
        # If the basket is not empty
        if self.basket:
            sub_total = 0

            for item in self.basket:
                # Standard subtotal calculation for each item
                price = item["quantity"] * self.pricing[item["code"]]["unitPrice"]
                sub_total += price
                discounted_amount = 0

                # Special Price check for item using floor division
                if self.pricing[item["code"]]["specialPrice"]:
                    if item["quantity"] >= self.pricing[item["code"]]["specialAmount"]:
                        discounted_amount = (item["quantity"] // self.pricing[item["code"]]["specialAmount"]) * 10
                        sub_total -= discounted_amount
                        print("---Special price discount for {} applied!---".format(item["code"]))

                # Print statements showing the basket prices
                if item["quantity"] > 0:
                    if self.pricing[item["code"]]["specialPrice"]:
                        print("Item: [{}] Quantity: [{}] Non Discounted Price: [£{}] Discounted Price: [£{}]".format(
                            item["code"],
                            item["quantity"],
                            price,
                            price - discounted_amount))
                    else:
                        print("Item: [{}] Quantity: [{}] Price: [£{}]".format(item["code"], item["quantity"], price))

            final_output = "\nSUBTOTAL = £{}".format(str(sub_total))

            return final_output, sub_total
        else:
            return "Basket is empty!", "Basket is empty!"
