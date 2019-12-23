from Instrument import Instrument

class Guitar(Instrument):
	def __init__(self, serialNumber='', price=0, spec=None):
		super().__init__(serialNumber, price, spec)


	def __str__(self):
		string = "Guitar:\n"
		string += super().__str__()
		return string
