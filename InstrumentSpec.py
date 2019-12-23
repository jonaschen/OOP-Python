
class InstrumentSpec:
	def __init__(self, builder, model, guitarType, backWood, topWood):
		self.builder = builder
		self.model = model
		self.guitarType = guitarType
		self.backWood = backWood
		self.topWood = topWood

	def __eq__(self, other):
		if self.getBuilder() != other.getBuilder():
			return False

		if self.getModel().lower() != other.getModel().lower():
			return False

		if self.getType() != other.getType():
			return False

		if self.getBackWood() != other.getBackWood():
			return False

		if self.getTopWood() != other.getTopWood():
			return False

		return True

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

	def __str__(self):
		string = 'Model: %s\n' % (self.getModel())
		string += 'Type: %s\n' % (self.getType())
		string += 'Builer: %s' % (self.getBuilder())
		return string
