from Instrument import Instrument

class Mandolin(Instrument):
	def __init__(self, serialNumber='', price=0, spec=None):
		super().__init__(serialNumber, price, spec)


	def __str__(self):
		string = "Mandolin:\n"
		string += super().__str__()
		return string

