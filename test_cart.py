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


# Testing the output message when an empty basket is ran during the CLI
def test_for_subtotal_calculation_scenario1():
    cart_test = Cart()
    output = cart_test.calculate_subtotal()

    assert output == "Basket is empty"


# Testing the subtotal output when manually entering an items with a quantity of 0
def test_for_subtotal_calculation_scenario2():
    test_code = [{"code": "A", "quantity": 0}, {"code": "B", "quantity": 0}, {"code": "C", "quantity": 0},
                 {"code": "D", "quantity": 0}]

    cart_test = Cart()
    cart_test.add_entire_basket(test_code)
    output, subtotal = cart_test.calculate_subtotal()

    assert subtotal == 0


# Testing that item A is the correct price
def test_for_subtotal_calculation_scenario3():
    cart_test = Cart()
    cart_test.add_item("A", 1)
    output, subtotal = cart_test.calculate_subtotal()

    assert subtotal == 50


# Testing that item B is the correct price
def test_for_subtotal_calculation_scenario4():
    cart_test = Cart()
    cart_test.add_item("B", 1)
    output, subtotal = cart_test.calculate_subtotal()

    assert subtotal == 35


# Testing that item C is the correct price
def test_for_subtotal_calculation_scenario5():
    cart_test = Cart()
    cart_test.add_item("C", 1)
    output, subtotal = cart_test.calculate_subtotal()

    assert subtotal == 25


# Testing that item D is the correct price
def test_for_subtotal_calculation_scenario6():
    cart_test = Cart()
    cart_test.add_item("D", 1)
    output, subtotal = cart_test.calculate_subtotal()

    assert subtotal == 12


# Special Price for item A test
def test_for_subtotal_calculation_scenario7():
    cart_test = Cart()
    cart_test.add_item("A", 3)
    output, subtotal = cart_test.calculate_subtotal()

    assert subtotal == 140


# test of Special Price for item A multiplied
def test_for_subtotal_calculation_scenario8():
    cart_test = Cart()
    cart_test.add_item("A", 6)
    output, subtotal = cart_test.calculate_subtotal()

    assert subtotal == 280


# Special Price for item B test
def test_for_subtotal_calculation_scenario9():
    cart_test = Cart()
    cart_test.add_item("B", 2)
    output, subtotal = cart_test.calculate_subtotal()

    assert subtotal == 60


# test of Special Price for item B multiplied
def test_for_subtotal_calculation_scenario10():
    cart_test = Cart()
    cart_test.add_item("B", 4)
    output, subtotal = cart_test.calculate_subtotal()

    assert subtotal == 120


# Test for data set provided
def test_for_subtotal_calculation_scenario11():
    test_code = [{"code": "A", "quantity": 3}, {"code": "B", "quantity": 3}, {"code": "C", "quantity": 1},
                 {"code": "D", "quantity": 2}]

    cart_test = Cart()
    cart_test.add_entire_basket(test_code)
    output, subtotal = cart_test.calculate_subtotal()
    # item A 50x3=150 (140), item B 35x3=105 (95), item C 25x1=25, item D 12x2=24     =284

    assert subtotal == 284


