from Cart import Cart


def test_to_add_item():
    cart_test = Cart()
    cart_test.add_item("A", 20)

    assert cart_test.basket[0]["code"] == 'A' and cart_test.basket[0]["quantity"] == 20


def test_to_add_entire_basket():
    test_code = [{"code": "A", "quantity": 3}, {"code": "B", "quantity": 100}, {"code": "C", "quantity": 1},
                 {"code": "D", "quantity": 2}]

    cart_test = Cart()
    cart_test.add_entire_basket(test_code)

    assert cart_test.basket[1]["quantity"] == 100 and len(cart_test.basket) == 4


# Edit a basket by updating an item quantity
def test_to_edit_a_basket_scenario1():
    cart_test = Cart()
    cart_test.add_item("A", 10)
    cart_test.edit_basket("A", 20)

    assert cart_test.basket[0]["code"] == 'A' and cart_test.basket[0]["quantity"] == 20


# Edit a basket by adding a new item if there is nothing present
def test_to_edit_a_basket_scenario2():
    cart_test = Cart()
    cart_test.add_item("A", 10)
    cart_test.edit_basket("B", 20)

    assert cart_test.basket[1]["code"] == 'B' and cart_test.basket[1]["quantity"] == 20


# Edit a basket by removing an item by setting the quantity to 0
def test_to_edit_a_basket_scenario3():
    cart_test = Cart()
    cart_test.add_item("A", 10)
    cart_test.edit_basket("A", 0)

    assert len(cart_test.basket) == 0


def test_for_subtotal_calculation_scenario1():
    test_code = [{"code": "A", "quantity": 0}, {"code": "B", "quantity": 0}, {"code": "C", "quantity": 0},
                 {"code": "D", "quantity": 0}]

    cart_test = Cart()
    cart_test.add_entire_basket(test_code)
    output, subtotal = cart_test.calculate_subtotal(cart_test.basket)

    assert output == "Basket is empty"


