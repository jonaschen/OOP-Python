from Instrument import Instrument
from InstrumentType import InstrumentType

class Inventory:
	def __init__(self):
		self.inventory = []

	def addInstrument(self, serial, price, spec):
		#print (spec)
		self.inventory.append(Instrument(serial, price, spec))

	def displayInstruments(self):
		for instrument in self.inventory:
			print (instrument)
			print ('\n')

	def get(self, serial):
		for instrument in self.inventory:
			if instrument.getSerialNumber() == serial:
				return instrument

	def search(self, searchSpec):
		instruments = []

		for instrument in self.inventory:
			spec = instrument.getSpec()
			if spec == searchSpec:
				instruments.append(instrument)

		return instruments

