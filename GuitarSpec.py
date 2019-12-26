from InstrumentSpec import InstrumentSpec

class GuitarSpec(InstrumentSpec):
	def __init__(self, builder, model, guitarType, backWood, topWood, numStrings):
		super().__init__(builder, model, guitarType, backWood, topWood)
		self.numStrings = numStrings

	def __eq__(self, other):
		if not isinstance(other, GuitarSpec):
			return False
		if not super().__eq__(other):
			return False

		if self.getNumStrings() != other.getNumStrings():
			return False

		return True

	def getNumStrings(self):
		return self.numStrings

	def __str__(self):
		string = "GuitarSpec:\n"
		string += super().__str__()
		string += 'Number of Strings: %s' % (self.getNumStrings())
		return string
