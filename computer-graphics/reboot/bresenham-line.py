""" 

if m < 1:
	Pk = 2dy - dx
	if Pk < 0
		PK+1 = Pk + 2dy
	else
		Pk+1 = Pk + 2dy - 2dx 

if m >= 1:
	Pk = 2dx - dy
	if Pk < 0
		Pk+1 = Pk + 2dx
	else 
		Pk+1 = Pk + 2dx - 2dy

"""

from pprint import pprint

class BresenhamLine:
	def __init__(self, start_cord, end_cord):
		self.start_cord = start_cord
		self.end_cord = end_cord
		self.line = []

	def run(self):
		self.line = [self.start_cord]
		
		dx = self.end_cord[0] - self.start_cord[0]
		dy = self.end_cord[1] - self.start_cord[1]

		pprint({
			"dx": dx,
			"dy": dy,
		})

		m = dy/dx
		print("m = ", m)

		pk = None
		if m < 1:
			pk = 2*dy - dx
		else:
			pk = 2*dx - dy

		print("pk = ", pk)

		current_x, current_y = self.start_cord
		
		while current_x < self.end_cord[0] or current_y < self.end_cord[1]:
			if pk < 0:
				if m < 1:
					pk += 2*dy
					current_x += 1
				else:
					pk += 2*dx
					current_y += 1
			else: 
				if m < 1:
					pk += 2*dy - 2*dx
					current_x += 1
					current_y += 1
				else:
					pk += 2*dx - 2*dy			
					current_x += 1
					current_y += 1

			pprint({
				"x": current_x,
				"y": current_y
			})


			self.line.append([current_x, current_y])

		
		return self.line




if __name__ == "__main__":
	# start_x, start_y, end_x, end_y = map(int, input("start x, start y, end_x, end_y = ").split())
	# bresenham_line1 = BresenhamLine([2, 3], [8, 6])
	# bresenham_line1 = BresenhamLine([2, 5], [5, 12])
	# bresenham_line1 = BresenhamLine([3, 4], [7, 10])
	bresenham_line1 = BresenhamLine([2, 3], [8, 7])
	# bresenham_line1 = BresenhamLine([start_x, start_y], [end_x, end_y])
	pprint(bresenham_line1.run())