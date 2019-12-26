#!/usr/bin/python3

from GuitarSpec import GuitarSpec
from MandolinSpec import MandolinSpec
from Inventory import Inventory
from Builder import Builder
from Wood import Wood
from GuitarType import Type
from Style import Style

def initializeInventory(inventory):
	testGuitars = {
		"11277": (3999.95, Builder.COLLINGS, "CJ",
				Type.ACOUSTIC, Wood.INDIAN_ROSEWOOD, Wood.SITKA, 6),
		"V95693": (1499.95, Builder.FENDER, "Stratocastor",
				Type.ELECTRIC, Wood.ALDER, Wood.ALDER, 6),
		"V9512": (1549.95, Builder.FENDER, "Stratocastor",
				Type.ELECTRIC, Wood.ALDER, Wood.ALDER, 6),
		"122784": (5495.95, Builder.MARTIN, "D-18",
				Type.ACOUSTIC, Wood.MAHOGANY, Wood.ADIRONDACK, 6),
		"76531": (6295.95, Builder.MARTIN, "OM-28",
				Type.ACOUSTIC, Wood.BRAZILIAN_ROSEWOOD, Wood.ADIRONDACK, 6),
		"70108276": (2295.95, Builder.GIBSON, "Les Paul",
				Type.ELECTRIC, Wood.MAHOGANY, Wood.MAPLE, 6),
		"82765501": (1890.95, Builder.GIBSON, "SG '61 Reissue",
				Type.ELECTRIC, Wood.MAHOGANY, Wood.MAHOGANY, 6),
		"77023": (6275.95, Builder.MARTIN, "D-28",
				Type.ACOUSTIC, Wood.BRAZILIAN_ROSEWOOD, Wood.ADIRONDACK, 6),
		"1092": (12995.95, Builder.RYAN, "SJ",
				Type.ACOUSTIC, Wood.INDIAN_ROSEWOOD, Wood.CEDAR, 6),
		"566-62": (8999.95, Builder.RYAN, "Cathedral",
				Type.ACOUSTIC, Wood.COCOBOLO, Wood.CEDAR, 6),
		"6 29584": (2100.95, Builder.PRS, "Dave Navarro Signature",
				Type.ELECTRIC, Wood.MAHOGANY, Wood.MAPLE, 6)
	}

	testMandolins = {
		"MT8552-A": (8939.95, Builder.RYAN, "Cathedral",
				Type.ACOUSTIC, Wood.COCOBOLO, Wood.CEDAR, Style.A),
		"MT8552-F": (2130.95, Builder.PRS, "Dave Navarro Signature",
				Type.ELECTRIC, Wood.MAHOGANY, Wood.MAPLE, Style.F)
	}

	for serial in testGuitars:
		meta = testGuitars[serial]
		price = meta[0]
		spec = GuitarSpec(meta[1], meta[2], meta[3], meta[4], meta[5], meta[6])
		inventory.addInstrument(serial, price, spec)

	for serial in testMandolins:
		meta = testMandolins[serial]
		price = meta[0]
		spec = MandolinSpec(meta[1], meta[2], meta[3], meta[4], meta[5], meta[6])
		inventory.addInstrument(serial, price, spec)


if __name__ == '__main__':
	inventory = Inventory()
	initializeInventory(inventory)
	inventory.displayInstruments()

	whatErinLikes = []
	whatErinLikes.append( GuitarSpec(Builder.FENDER, "Stratocastor",
                                      Type.ELECTRIC, Wood.ALDER, Wood.ALDER, 6) )
	whatErinLikes.append( MandolinSpec(Builder.RYAN, "Cathedral",
                                      Type.ACOUSTIC, Wood.COCOBOLO, Wood.CEDAR, Style.A) )

	instruments = []
	for spec in whatErinLikes:
		instruments += inventory.search(spec)

	if len(instruments):
		for instrument in instruments:
			spec = instrument.getSpec()
			if isinstance(spec, GuitarSpec):
				instType = 'Guitar'
			elif isinstance(spec, MandolinSpec):
				instType = 'Mandolin'
			print ("Erin, you might like this %s %s: %s" %
				(spec.getBuilder(), spec.getModel(), instType))
			print ("\t%s back and sides," % (spec.getBackWood()))
			print ("\t%s top." % (spec.getTopWood()))
			print ("You can have it for only $%s" % (instrument.getPrice()))
	else:
		print("Sorry, Erin, we have nothing for you.")


