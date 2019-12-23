
class Instrument:
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
		string += '%s' % (self.getSpec())
		return string

if __name__ == "__main__":
	inst = Instrument("123", 456)
	print (inst.getSerialNumber())
