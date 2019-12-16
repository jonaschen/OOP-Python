
from enum import Enum

class Builder(Enum):
	FENDER = "Fender"
	MARTIN = "Martin"
	GIBSON = "Gibson"
	COLLINGS = "Collings"
	OLSON = "Olson"
	RYAN = "Ryan"
	PRS = "PRS"

	def __str__(self):
		return '%s' % (self.value)
