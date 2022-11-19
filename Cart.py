class Cart():
    # private members of the Cart class
    pricing = {'A': {"unitPrice": 50, "specialPrice": True, "specialAmount": 3},
               'B': {"unitPrice": 35, "specialPrice": True, "specialAmount": 2},
               'C': {"unitPrice": 25, "specialPrice": False},
               'D': {"unitPrice": 12, "specialPrice": False}
                    }

    def __init__(self):
        self.basket = []

    def add_item(self, item, quantity):
        self.basket.append({"code": item, "quantity": quantity})

    def add_entire_basket(self, basket):
        self.basket = basket

    def edit_basket(self, code, quantity):
        for item in self.basket:
            # Boolean check for if the quantity is set to 0
            if quantity > 0:
                # if the code is present in the basket edit the quantity
                if item["code"] == code:
                    item["quantity"] = quantity
                # If the code is not present add it to the basket
                else:
                    self.basket.append({"code": code, "quantity": quantity})
            # Remove the item from the basket if present
            else:
                if item["code"] == code:
                    self.basket.remove(item)

    def calculate_subtotal(self):
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

            return final_output

        else:
            return "Basket is empty"


