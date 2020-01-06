#!/usr/bin/python3

class Unit:
	def __init__(self, unitId):
		self.properties = {}
		self.weapons = []
		self.id = unitId

	def setType(self, unitType):
		self.type = unitType

	def getType(self):
		return self.type

	def setProperty(self, propertyName, propertyValue):
		self.properties[propertyName] = propertyValue

	def getProperty(self, propertyName):
		if propertyName not in self.properties:
			return None
		return self.properties[propertyName]

	def getID(self):
		return self.id

	def getName(self):
		return self.name

	def setName(self, name):
		self.name = name

	def addWeapon(self, weapon):
		self.weapons.append(weapon)

	def getWeapons(self):
		return self.weapons


if __name__ == '__main__':
	unit = Unit(0)
	unit.setType('infantry')
	unit.setProperty('HitPoints', 25)

	print (unit.getType())
	print (unit.getProperty('HitPoints'))


	unit.setProperty('HitPoints', 15)
	print (unit.getProperty('HitPoints'))

	print (unit.getProperty('Strength'))
