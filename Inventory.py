from Guitar import Guitar


class Inventory:
	def __init__(self):
		self.guitars = []

	def newGuitar(self, serialNumber='', price=0, builder='', model='', guitarType='', backWood='', topWood=''):
		guitar = Guitar(serialNumber, price, builder, model, guitarType, backWood, topWood)
		self.guitars.append(guitar)

	def addGuitar(self, guitar):
		self.guitars.append(guitar)

	def displayGuitars(self):
		for guitar in self.guitars:
			print ('')
			guitar.showGuitar()

	def search(self, searchGuitar):
		for guitar in self.guitars:
			builder = searchGuitar.getBuilder()
			if builder and len(builder):
				if builder != guitar.getBuilder(): continue

			model = searchGuitar.getModel()
			if model and len(model):
				if model != guitar.getModel(): continue

			gtype = searchGuitar.getType()
			if gtype and len(gtype):
				if gtype != guitar.getType(): continue

			backWood = searchGuitar.getBackWood()
			if backWood and len(backWood):
				if backWood != guitar.getBackWood(): continue

			topWood = searchGuitar.getTopWood()
			if topWood and len(topWood):
				if topWood != guitar.getTopWood(): continue

			return guitar;

		return None

