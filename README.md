# Shopping-Cart
Sofware development test

## Introduction
This project is a simple checkout system that produces a subtotal using a CLI. The prices used are from the dataset below: 

##### Pricing dataset
Item Code  | Unit Price | Special Price
---------- | ---------- | ----------
A          | £50        | 3 for £140
B          | £35        | 2 for £60
C          | £25        |
D          | £12        |

##### Data source example
`[{"code":"A","quantity":3},{"code":"B","quantity":3},{"code":"C","quantity":1},{"code":"D","quantity":2}]`

##### CLI (Command line interface)
The CLI is mainly split into two paths. The first path is used for quick testing. In the testing path, a user can recieve an output from the pre-set data source implemented at the bottom of the main.py script.

The secound path in the CLI allows users to create their own cart. By following the various outputs and inputs, users could add and edit items in the cart to their liking. There is a range of validation checks to help ensure there are no crashes. After editing, a cart summary is presented with a subtotal in the checkout.

## Requirements
##### installs
* Python 3.9+ should be downlaoded and used either in an IDE of choice or a python shell. see the link for installation https://www.python.org/downloads/
* (Optional) Install pytest to recreate the unit testing. Command line: install pip install -U pytest
##### Files to download
Main.py, Cart.py and optionally test_cart.py should be downloaded and placed in the same directory.

## Testing
Unit testing was conducted using the pytest framework. The tests were coded in test_cart.py. The main focus of these tests was to ensure that the methods 
in the Cart.py class worked under a range of scenarios.

![This is an image](test.png)
