class Marble(object):
	"""docstring for Marble"""
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	@staticmethod	
	def can_place(x, y):
		if x >= 7 or y >= 7: return False
		if x < 0 or y < 0: return False
		if (x < 2) or (x > 4):
			if (y < 2) or (y > 4):
				return False
		return True

	def can_move(self, points, x, y):
		if(not Marble.can_place(x, y)): return False
		x_diff = x - self.x
		y_diff = y - self.y
		if not ( (abs(x_diff) == 2 or abs(y_diff) == 2) and abs(x_diff) + abs(y_diff) == 2 ): return False
		jump_position = ( self.x + x_diff/2, self.y + y_diff/2 )
		jump_piece = points[jump_position[0]][jump_position[1]]
		if (jump_piece is None): return False
		if (points[x][y] is not None): return False
		return True

	def __repr__(self):
		return "{}, {}".format(self.x, self.y)

class Board(object):
	"""docstring for Board"""
	def __init__(self):
		self.points = []
		for i in range(7):
			self.points.append([])
			for j in range(7):
				if Marble.can_place(i, j):
					self.points[i].append(Marble(i,j))
				else:
					self.points[i].append(None)

		self.points[3][3] = None

	def display(self, x, y):
		if(self.points[x][y]):
			return 'x'
		elif Marble.can_place(x, y):
			return 'o'
		else:
			return ' '

	def __repr__(self):
		result = ''
		for i in range(7):
			result += '  '.join([self.display(i, j) for j in range(7)]) + '\n'
		return result

	def save(self):
		return ''.join([''.join([self.display(i, j) for j in range(7)]) for i in range(7)])


	def load(self, image):
		self.points = []
		for i, char in enumerate(image):
			x = i % 7
			y = i // 7
			if x == 0: self.points.append([])
			if char == 'x':
				self.points[-1].append(Marble(x, y))
			else:
				self.points[-1].append(None)


	def itterate_marbles(self):
		for row in self.points:
			for point in row:
				if (point is not None):
					yield point

	def find_available_moves(self):
		moves = []
		directions = [(0,2),(2,0),(0,-2),(-2,0)]
		for marble in self.itterate_marbles():
			possible_moves = [(marble.x + x, marble.y + y) for (x, y) in directions]
			for (x, y) in possible_moves:
				if marble.can_move(self.points, x, y):
					moves.append(((marble.x, marble.y), (x, y)))
		return moves




if __name__ == '__main__':
	
	board = Board()

	print(board)
	image = board.save()
	print(image)
	board.load(image)

	print(board)

	moves = board.find_available_moves()
	print(moves)














