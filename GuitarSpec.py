class GuitarSpec:
	def __init__(self, builder, model, guitarType, backWood, topWood, numStrings):
		self.builder = builder
		self.model = model
		self.guitarType = guitarType
		self.backWood = backWood
		self.topWood = topWood
		self.numStrings = numStrings

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

	def getNumStrings(self):
		return self.numStrings
