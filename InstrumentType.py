
from enum import Enum

class InstrumentType(Enum):
	GUITAR = "Guitar"
	MANDOLIN = "Mandolin"
	BANJO = "Banjo"
	DOBRO = "Dobro"
	FIDDLE = "Fiddle"
	BASS = "Bass"

	def __str__(self):
		return '%s' % (self.value)

