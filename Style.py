
from enum import Enum

class Style(Enum):
	A = 'A'
	F = 'F'

	def __str__(self):
		return '%s style' % (self.value)
