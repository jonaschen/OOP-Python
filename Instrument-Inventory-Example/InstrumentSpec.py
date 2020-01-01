
class InstrumentSpec:
	def __init__(self, properties):
		self.properties = properties

	def __eq__(self, other):
		otherProperties = other.getProperties()
		#print (otherProperties)
		#print (self.properties) 
		for key in otherProperties.keys():
			if not key in self.properties:
				return False
			if self.properties[key] != otherProperties[key]:
				return False

		return True


	def getProperty(self, propertyName):
		return self.properties[propertyName]

	def getProperties(self):
		return self.properties


