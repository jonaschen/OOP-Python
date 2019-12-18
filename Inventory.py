from Guitar import Guitar
from GuitarSpec import GuitarSpec


class Inventory:
	def __init__(self):
		self.guitars = []

	def newGuitar(self, serialNumber='', price=0, builder='', model='', guitarType='', backWood='', topWood=''):
		spec = GuitarSpec(builder, model, guitarType, backWood, topWood)
		guitar = Guitar(serialNumber, price, spec)
		self.guitars.append(guitar)

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
			builder = searchSpec.getBuilder()
			if builder != spec.getBuilder(): continue

			model = searchSpec.getModel()
			if model and len(model):
				if model.lower() != spec.getModel().lower(): continue

			gtype = searchSpec.getType()
			if gtype != spec.getType(): continue

			backWood = searchSpec.getBackWood()
			if backWood != spec.getBackWood(): continue

			topWood = searchSpec.getTopWood()
			if topWood != spec.getTopWood(): continue

			guitars.append(guitar)

		return guitars

