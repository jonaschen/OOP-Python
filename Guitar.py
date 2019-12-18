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

	def showGuitar(self):
		print ('serial number: ' + self.serialNumber)
		print ('price: ' + str(self.price))
		print ('model: ' + str(self.getSpec().getModel()))
		print ('guitarType: ' + str(self.getSpec().getType()))
		print ('builer:' + str(self.getSpec().getBuilder()))

