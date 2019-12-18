from Guitar import Guitar
from GuitarSpec import GuitarSpec


class Inventory:
	def __init__(self):
		self.guitars = []

	def addGuitar(self, guitar):
		self.guitars.append(guitar)

	def displayGuitars(self):
		for guitar in self.guitars:
			print ('')
			guitar.showGuitar()

	def search(self, searchSpec):
		guitars = []

		for guitar in self.guitars:
			spec = guitar.getSpec()
			if spec == searchSpec:
				guitars.append(guitar)

		return guitars

