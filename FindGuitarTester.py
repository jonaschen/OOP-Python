#!/usr/bin/python3

from Guitar import Guitar
from Inventory import Inventory

def initializeInventory(inventory):
	inventory.newGuitar("11277", 3999.95, "Collings", "CJ", "acoustic",
	                 "Indian Rosewood", "Sitka")
	inventory.newGuitar("V95693", 1499.95, "Fender", "Stratocastor", "electric",
	                 "Alder", "Alder")
	inventory.newGuitar("V9512", 1549.95, "Fender", "Stratocastor", "electric",
	                 "Alder", "Alder")
	inventory.newGuitar("122784", 5495.95, "Martin", "D-18", "acoustic",
	                 "Mahogany", "Adirondack")
	inventory.newGuitar("76531", 6295.95, "Martin", "OM-28", "acoustic",
	                 "Brazilian Rosewood", "Adriondack")
	inventory.newGuitar("70108276", 2295.95, "Gibson", "Les Paul", "electric",
	                 "Mahogany", "Maple")
	inventory.newGuitar("82765501", 1890.95, "Gibson", "SG '61 Reissue",
	                 "electric", "Mahogany", "Mahogany")
	inventory.newGuitar("77023", 6275.95, "Martin", "D-28", "acoustic",
	                 "Brazilian Rosewood", "Adirondack")
	inventory.newGuitar("1092", 12995.95, "Olson", "SJ", "acoustic",
	                 "Indian Rosewood", "Cedar")
	inventory.newGuitar("566-62", 8999.95, "Ryan", "Cathedral", "acoustic",
	                 "Cocobolo", "Cedar")
	inventory.newGuitar("6 29584", 2100.95, "PRS", "Dave Navarro Signature",
	                    "electric", "Mahogany", "Maple")

if __name__ == '__main__':
	inventory = Inventory()
	initializeInventory(inventory)
	inventory.displayGuitars()


	whatErinLikes = Guitar("", 0, "fender", "Stratocastor",
                                      "electric", "Alder", "Alder")

	guitar = inventory.search(whatErinLikes)

	if guitar:
		print ("Erin, you might like this %s %s %s guitar:" %
			(guitar.getBuilder(), guitar.getModel(), guitar.getType()))
		print ("\t%s back and sides," % (guitar.getBackWood()))
		print ("\t%s top." % (guitar.getTopWood()))
		print ("You can have it for only $%s" % (guitar.getPrice()))
	else:
		print("Sorry, Erin, we have nothing for you.")
