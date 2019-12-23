from Guitar import Guitar
from GuitarSpec import GuitarSpec
from Mandolin import Mandolin
from MandolinSpec import MandolinSpec


class Inventory:
	def __init__(self):
		self.inventory = []

	def addInstrument(self, serial, price, spec):
		if isinstance(spec, GuitarSpec):
			self.inventory.append(Guitar(serial, price, spec))
		elif isinstance(spec, MandolinSpec):
			self.inventory.append(Mandolin(serial, price, spec))

	def displayInstruments(self):
		for instrument in self.inventory:
			print (instrument)
			print ('\n')

	def get(self, serial):
		for instrument in self.inventory:
			if instrument.getSerialNumber() == serial:
				return instrument

	def searchGuitar(self, searchSpec):
		guitars = []

		for instrument in self.inventory:
			spec = instrument.getSpec()
			if isinstance(spec, GuitarSpec) and spec == searchSpec:
				guitars.append(instrument)

		return guitars

	def searchMandolin(self, searchSpec):
		mandolin = []

		for instrument in self.inventory:
			spec = instrument.getSpec()
			if isinstance(spec, MandolinSpec) and spec == searchSpec:
				mandolin.append(instrument)

		return guitars
