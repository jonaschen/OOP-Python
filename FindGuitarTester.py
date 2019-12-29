#!/usr/bin/python3

from InstrumentSpec import InstrumentSpec
from InstrumentType import InstrumentType
from Inventory import Inventory
from Builder import Builder
from Wood import Wood
from GuitarType import Type
from Style import Style

def initializeInventory(inventory):
	properties = {}
	properties["instrumentType"] = InstrumentType.GUITAR
	properties["builder"] = Builder.COLLINGS
	properties["model"] = "CJ"
	properties["type"] = Type.ACOUSTIC
	properties["numStrings"] = 6
	properties["topWood"] = Wood.INDIAN_ROSEWOOD
	properties["backWood"] = Wood.SITKA
	inventory.addInstrument("11277", 3999.95, InstrumentSpec(properties.copy()))

	properties["builder"] = Builder.MARTIN
	properties["model"] = "D-18"
	properties["topWood"] = Wood.MAHOGANY
	properties["backWood"] = Wood.ADIRONDACK
	inventory.addInstrument("122784", 5495.95, InstrumentSpec(properties.copy()))

	properties["builder"] = Builder.FENDER
	properties["model"] = "Stratocastor"
	properties["type"] = Type.ELECTRIC
	properties["topWood"] = Wood.ALDER
	properties["backWood"] = Wood.ALDER
	inventory.addInstrument("V95693", 1499.95, InstrumentSpec(properties.copy()))
	inventory.addInstrument("V9512", 1549.95, InstrumentSpec(properties.copy()))

	properties["builder"] = Builder.GIBSON
	properties["model"] = "Les Paul"
	properties["topWood"] = Wood.MAPLE
	properties["backWood"] = Wood.MAPLE
	inventory.addInstrument("70108276", 2295.95, InstrumentSpec(properties.copy()))

	properties["model"] = "SG '61 Reissue"
	properties["topWood"] = Wood.MAHOGANY
	properties["backWood"] = Wood.MAHOGANY
	inventory.addInstrument("82765501", 1890.95, InstrumentSpec(properties.copy()))

	properties["instrumentType"] = InstrumentType.MANDOLIN
	properties["type"] = Type.ACOUSTIC
	properties["model"] = "F-5G"
	properties["backWood"] = Wood.MAPLE
	properties["topWood"] = Wood.MAPLE
	properties.pop("numStrings")
	inventory.addInstrument("9019920", 5495.99, InstrumentSpec(properties.copy()))

	properties["instrumentType"] = InstrumentType.BANJO
	properties["model"] = "RB-3 Wreath"
	properties.pop("topWood")
	properties["numStrings"] = 5
	inventory.addInstrument("8900231", 2945.95, InstrumentSpec(properties.copy()))



if __name__ == '__main__':
	inventory = Inventory()
	initializeInventory(inventory)
	print ("List of instruments:")
	inventory.displayInstruments()
	print ("===== End of List =====")

	properties = {}
	properties["builder"] = Builder.GIBSON
	properties["backWood"] = Wood.MAPLE
	whatBryanLikes = InstrumentSpec(properties)

	instruments = inventory.search(whatBryanLikes)

	if len(instruments):
		print ("Bryan, you might like these instruments:")
		for instrument in instruments:
			print (instrument)
	else:
		print("Sorry, Erin, we have nothing for you.")


