class Guitar:
	def __init__(self, serialNumber='', price=0, builder='', model='', guitarType='', backWood='', topWood=''):
		self.serialNumber = serialNumber
		self.price = price
		self.builder = builder
		self.model = model
		self.guitarType = guitarType
		self.backWood = backWood
		self.topWood = topWood

	def getSerialNumber(self):
		return self.serialNumber

	def getPrice(self):
		return self.price

	def setPrice(self, price):
		self.price = price

	def getBuilder(self):
		return self.builder

	def getModel(self):
		return self.model

	def getType(self):
		return self.guitarType

	def getBackWood(self):
		return self.backWood

	def getTopWood(self):
		return self.topWood

	def showGuitar(self):
		print ('serial number: ' + self.serialNumber)
		print ('price: ' + str(self.price))
		print ('model: ' + self.model)
		print ('guitarType: ' + str(self.guitarType))
		print ('builer:' + str(self.builder))

