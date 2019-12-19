from GuitarSpec import GuitarSpec

class Guitar:
	def __init__(self, serialNumber='', price=0, spec=None):
		self.serialNumber = serialNumber
		self.price = price
		self.spec = spec

	def getSerialNumber(self):
		return self.serialNumber

	def getPrice(self):
		return self.price

	def setPrice(self, price):
		self.price = price

	def getSpec(self):
		return self.spec

	def __str__(self):
		string = 'serial number: %s\n' % (self.serialNumber)
		string += 'price: %d\n' % (self.price)
		string += 'model: %s\n' % (self.getSpec().getModel())
		string += 'guitarType: %s\n' % (self.getSpec().getType())
		string += 'builer: %s' % (self.getSpec().getBuilder())
		return string

