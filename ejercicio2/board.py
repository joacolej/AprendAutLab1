# DEPENDENCIES ------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------
from numpy import *

# MAIN --------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------

class Board():

	# CONSTRUCTOR ---------------------------------------------------------------------------------------------------------------------------------------
	# ---------------------------------------------------------------------------------------------------------------------------------------------------

	def __init__(self):

		# Generates 19x19 matrix of 0
		self._free = 361
		self._matrix = zeros(361)
		self._matrix = reshape(self._matrix,(19,19))

	# GETTERS -------------------------------------------------------------------------------------------------------------------------------------------
	# ---------------------------------------------------------------------------------------------------------------------------------------------------

	def get_free(self):
		return self._free

	def get_matrix(self):
		return self._matrix
		
	# METHODS -------------------------------------------------------------------------------------------------------------------------------------------
	# ---------------------------------------------------------------------------------------------------------------------------------------------------

	# Adds token in (x,y), if is not able to, returns false
	def addToken(self, x, y, val):

		if x > 18 or x < 0:
			return False

		if y > 18 or y < 0:
			return False

		if self._matrix[x][y] != 0:
			return False

		self._free = self._free - 1
		self._matrix[x][y] = val
		return True

	# Removes token in (x,y), auxiliar method used by the player after adding a token
	def removeToken(self, x, y):
		self._free = self._free + 1
		self._matrix[x][y] = 0

	# Checks if player won after adding token in (x,y)
	def win(self, x, y, val):

		# Check horizontal
		# ---------------------------------------------------------------------------------------------------------------------------------

		if x-4 >= 0:
			if self._matrix[x-1][y] == val and self._matrix[x-2][y] == val and self._matrix[x-3][y] == val and self._matrix[x-4][y] == val:
				return True

		if x-3 >= 0 and x+1 < 19:
			if self._matrix[x-1][y] == val and self._matrix[x-2][y] == val and self._matrix[x-3][y] == val and self._matrix[x+1][y] == val:
				return True

		if x-2 >= 0 and x+2 < 19:
			if self._matrix[x-1][y] == val and self._matrix[x-2][y] == val and self._matrix[x+1][y] == val and self._matrix[x+2][y] == val:
				return True

		if x-1 >= 0 and x+3 < 19:
			if self._matrix[x-1][y] == val and self._matrix[x+1][y] == val and self._matrix[x+2][y] == val and self._matrix[x+3][y] == val:
				return True

		if x+4 < 19:
			if self._matrix[x+1][y] == val and self._matrix[x+2][y] == val and self._matrix[x+3][y] == val and self._matrix[x+4][y] == val:
				return True

		# Check vertical
		# ---------------------------------------------------------------------------------------------------------------------------------

		if y-4 >= 0:
			if self._matrix[x][y-1] == val and self._matrix[x][y-2] == val and self._matrix[x][y-3] == val and self._matrix[x][y-4] == val:
				return True

		if y-3 >= 0 and y+1 < 19:
			if self._matrix[x][y-1] == val and self._matrix[x][y-2] == val and self._matrix[x][y-3] == val and self._matrix[x][y+1] == val:
				return True

		if y-2 >= 0 and y+2 < 19:
			if self._matrix[x][y-1] == val and self._matrix[x][y-2] == val and self._matrix[x][y+1] == val and self._matrix[x][y+2] == val:
				return True

		if y-1 >= 0 and y+3 < 19:
			if self._matrix[x][y-1] == val and self._matrix[x][y+1] == val and self._matrix[x][y+2] == val and self._matrix[x][y+3] == val:
				return True

		if y+4 < 19:
			if self._matrix[x][y+1] == val and self._matrix[x][y+2] == val and self._matrix[x][y+3] == val and self._matrix[x][y+4] == val:
				return True

		# Check diagonal left to right
		# ---------------------------------------------------------------------------------------------------------------------------------

		if x-4 >= 0 and y-4 >= 0:
			if self._matrix[x-1][y-1] == val and self._matrix[x-2][y-2] == val and self._matrix[x-3][y-3] == val and self._matrix[x-4][y-4] == val:
				return True

		if x-3 >= 0 and y-3 >= 0 and x+1 < 19 and y+1 < 19:
			if self._matrix[x-1][y-1] == val and self._matrix[x-2][y-2] == val and self._matrix[x-3][y-3] == val and self._matrix[x+1][y+1] == val:
				return True

		if x-2 >= 0 and y-2 >= 0 and x+2 < 19 and y+2 < 19:
			if self._matrix[x-1][y-1] == val and self._matrix[x-2][y-2] == val and self._matrix[x+1][y+1] == val and self._matrix[x+2][y+2] == val:
				return True

		if x-1 >= 0 and y-1 >= 0 and x+3 < 19 and y+3  < 19:
			if self._matrix[x-1][y-1] == val and self._matrix[x+1][y+1] == val and self._matrix[x+2][y+2] == val and self._matrix[x+3][y+3] == val:
				return True

		if x+4 < 19 and y+4 < 19:
			if self._matrix[x+1][y+1] == val and self._matrix[x+2][y+2] == val and self._matrix[x+3][y+3] == val and self._matrix[x+4][y+4] == val:
				return True

		# Check diagonal right to left
		# ---------------------------------------------------------------------------------------------------------------------------------

		if x-4 >= 0 and y+4 < 19:
			if self._matrix[x-1][y+1] == val and self._matrix[x-2][y+2] == val and self._matrix[x-3][y+3] == val and self._matrix[x-4][y+4] == val:
				return True

		if x-3 >= 0 and y+3 < 19 and x+1 < 19 and y-1 >= 0:
			if self._matrix[x-1][y+1] == val and self._matrix[x-2][y+2] == val and self._matrix[x-3][y+3] == val and self._matrix[x+1][y-1] == val:
				return True

		if x-2 >= 0 and y+2 < 19 and x+2 < 19 and y-2 >= 0:
			if self._matrix[x-1][y+1] == val and self._matrix[x-2][y+2] == val and self._matrix[x+1][y-1] == val and self._matrix[x+2][y-2] == val:
				return True

		if x-1 >= 0 and y+1 < 19 and x+3 < 19 and y-3 >= 0:
			if self._matrix[x-1][y+1] == val and self._matrix[x+1][y-1] == val and self._matrix[x+2][y-2] == val and self._matrix[x+3][y-3] == val:
				return True

		if x+4 < 19 and y-4 >= 0:
			if self._matrix[x+1][y-1] == val and self._matrix[x+2][y-2] == val and self._matrix[x+3][y-3] == val and self._matrix[x+4][y-4] == val:
				return True

		return False

	# Checks if it is a draw after adding token in (x,y)
	def draw(self):
		return self._free == 0