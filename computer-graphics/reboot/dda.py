from pprint import pprint

class DDA:
	def __init__(self, start_cord: list, end_cord: list):
		self.start_cord = start_cord
		self.end_cord = end_cord
		self.line = []
	
	def run(self):
		self.line = [self.start_cord]
		
		dx = self.end_cord[0] - self.start_cord[0]
		dy = self.end_cord[1] - self.start_cord[1]
		
		m = None
		step = None
	
		""" 
		## corner case when dx will be 0
		
		if dx == 0:
			x_inc = 0
			y_inc = 1

		else:
			m = dy/dx
			step = dx if m <= 1 else dy

			x_inc = dx/step
			y_inc = dy/step 
			
		"""

		m = dy/dx
		step = dx if m <= 1 else dy

		x_inc = dx/step
		y_inc = dy/step 
	
		current_x, current_y = self.start_cord

		print(x_inc, y_inc)

		while current_x <self.end_cord[0] or current_y < self.end_cord[1]:
			current_x += x_inc
			current_y += y_inc
			
			self.line.append([current_x, current_y])

		return self.line



if __name__ == "__main__":
	# start_x, start_y, end_x, end_y = map(int, input("start x, start y, end x, end y = ").split())
	dda1 = DDA([2, 2], [2, 12])
    # dda1 = DDA([start_x, start_y], [end_x, end_y])
	pprint(dda1.run())