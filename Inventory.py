from Guitar import Guitar
from GuitarSpec import GuitarSpec


class Inventory:
	def __init__(self):
		self.guitars = []

	def addGuitar(self, serial, price, spec):
		self.guitars.append(Guitar(serial, price, spec))

	def displayGuitars(self):
		for guitar in self.guitars:
			print ('')
			guitar.showGuitar()

	def getGuitar(self, serial):
		for guitar in self.guitars:
			if guitar.getSerialNumber() == serial:
				return guitar

	def search(self, searchSpec):
		guitars = []

		for guitar in self.guitars:
			spec = guitar.getSpec()
			if spec == searchSpec:
				guitars.append(guitar)

		return guitars

