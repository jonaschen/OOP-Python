from InstrumentSpec import InstrumentSpec

class MandolinSpec(InstrumentSpec):
	def __init__(self, builder, model, guitarType, backWood, topWood, style):
		super().__init__(builder, model, guitarType, backWood, topWood)
		self.style = style

	def __eq__(self, other):
		if not isinstance(other, MandolinSpec):
			return False
		if not super().__eq__(other):
			return False

		if self.getStyle() != other.getStyle():
			return False

		return True

	def getStyle(self):
		return self.style

	def __str__(self):
		string = "MandolinSpec:\n"
		string += super().__str__()
		string += 'Style: %s' % (self.getStyle())
		return string
