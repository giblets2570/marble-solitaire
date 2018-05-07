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

	def find_jump_position(self, x, y):
		x_diff = x - self.x
		y_diff = y - self.y
		jump_position = ( self.x + x_diff/2, self.y + y_diff/2 )
		return jump_position

	def can_move(self, points, x, y):
		if(not Marble.can_place(x, y)): return False
		x_diff = x - self.x
		y_diff = y - self.y
		if not ( (abs(x_diff) == 2 or abs(y_diff) == 2) and abs(x_diff) + abs(y_diff) == 2 ): return False

		jump_position = self.find_jump_position(x, y)
		jump_piece = points[jump_position[1]][jump_position[0]]
		if (jump_piece is None): return False
		if (points[y][x] is not None): return False
		return True

	def move(self, move):
		self.x, self.y = move

	def __repr__(self):
		return "{}, {}".format(self.x, self.y)

class Board(object):
	"""docstring for Board"""
	def __init__(self):
		self.points = []
		for y in range(7):
			self.points.append([])
			for x in range(7):
				if Marble.can_place(x, y):
					self.points[y].append(Marble(x,y))
				else:
					self.points[y].append(None)

		self.set_place(3, 3, None)

	def get_place(self, x, y):
		return self.points[y][x]

	def set_place(self, x, y, value=None):
		self.points[y][x] = value

	def display(self, x, y):
		if(self.get_place(x, y)):
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
		return ''.join([''.join([self.display(i, j) for i in range(7)]) for j in range(7)])


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


	def make_move(self, move):
		(x_s, y_s), (x_e, y_e) = move

		marble = self.get_place(x_s, y_s)
		(x_j, y_j) = marble.find_jump_position(x_e, y_e)

		self.set_place(x_j, y_j)
		marble.move((x_e, y_e))
		self.set_place(x_e, y_e, marble)
		self.set_place(x_s, y_s)

	def is_complete(self):
		marbles = list(self.itterate_marbles())
		# if len(marbles) < 31: return True
		if(len(marbles) > 1): return False
		marble = marbles[0]
		return marble.x == 3 and marble.y == 3


def solve(board):
	states = []
	best = {'amount': 34}
	def step(state):
		board.load(state)
		num_marbles = state.count('x')
		if num_marbles < best['amount']:
			best['amount'] = num_marbles
			print("Best: {}".format(best['amount']))
			print(board)
		if board.is_complete(): return True
		moves = board.find_available_moves()
		for move in moves:
			board.load(state)
			board.make_move(move)
			_state = board.save()
			if step(_state):
				states.append(_state)	
				return True
		return False
	step(board.save())
	return states[::-1]



if __name__ == '__main__':
	
	board = Board()

	image = board.save()
	board.load(image)
	states = solve(board)

	print(states)

	print(board)















