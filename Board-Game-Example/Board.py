#!/usr/bin/python3

from Unit import Unit


class Tile:
	def __init__(self, x, y):
		self.name = "pos: (" + str(x) + ', '+ str(y) +')'
		self.units = []

	def __str__(self):
		return '<%s, %s>' % (self.name, self.units)

	def getUnits(self):
		return self.units

	def addUnit(self, unit):
		self.units.append(unit)

	def removeUnit(self, unit):
		self.units.pop(unit)

class Board:
	def __init__(self, height, width):
		self.height = height
		self.width = width
		self.tiles = []
		self.__setup__()

	def getTile(self, x, y):
		return self.tiles[x][y]

	def addUnit(self, unit, x, y):
		tile = self.getTile(x, y)
		tile.addUnit(unit)

	def removeUnit(self, unit, x, y):
		tile = self.getTile(x, y)
		tile.removeUnit(unit)

	def getUnits(self, x, y):
		tile = self.getTile(x, y)
		return tile.getUnits()

	def __str__(self):
		string = ''
		for x in range(0, self.width):
			for y in range(0, self.height):
				string += '%s, ' % (str(self.tiles[x][y]))
			string += '\n'
		return string

	def __setup__(self):
		for x in range(0, self.width):
			line = []
			for y in range(0, self.height):
				tile = Tile(x, y)
				line.append(tile)
			self.tiles.append(line)

if __name__ == '__main__':
	board = Board(8, 5)

	print (board)

	tile = board.getTile(3, 3)
	tile.addUnit('Jonas')
	print (board)
