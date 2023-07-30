#!/usr/bin/env python3
import ipdb

from classes.customer import Customer
from classes.order import Order
from classes.coffee import Coffee

if __name__ == "__main__":
    print("HELLO! :) let's debug")

steve = Customer("Steve")
fred = Customer("fred")
mocha = Coffee("mocha")
latte = Coffee("latte")
order_one = Order(steve, mocha, 10)
order_two = Order(steve, mocha, 4)
order_three = Order(fred, latte, 6)
order_four = Order(fred, mocha, 8)

ipdb.set_trace()
