#!/usr/bin/python3

from Guitar import Guitar
from Inventory import Inventory

guitar = Guitar(serialNumber='1010', price=135, model='Classical')
inventory = Inventory()
inventory.newGuitar(serialNumber='1100', price=100, guitarType='Electric')
inventory.addGuitar(guitar)

inventory.displayGuitars()

