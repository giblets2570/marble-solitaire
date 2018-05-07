class Marble(object):
	"""docstring for Marble"""
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	@staticmethod	
	def can_place(x, y):
		if x < 2 or x > 4:
			if y < 2 or y > 4:
				return False
		return True

	def __repr__(self):
		return "{}, {}: {}".format(self.x, self.y, self.can_place())

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



if __name__ == '__main__':
	
	board = Board()

	print(board)
	image = board.save()
	print(image)
	board.load(image)

	print(board)