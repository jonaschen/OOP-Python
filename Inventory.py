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

