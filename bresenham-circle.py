from pprint import pprint

class BresenhamCircleDrawing:
  def __init__(self, redius):
    self.redius = redius
    self.circle_center_cordinate = [0, 0]
    self.circle = {
      "1st": [],
      "2nd": [],
      "3rd": [],
      "4th": [],
    }

  def run(self):
    currentX = self.circle_center_cordinate[0]
    currentY = self.redius

    currentP = 3 - 2 * self.redius

    first_octate = []
    second_octate = []

    while(currentX <= currentY):
      first_octate.append((currentX, currentY))
      second_octate.append((currentY, currentX))

      if currentP < 0:
        currentP += 4 * currentX + 6
        currentX += 1
      else:
        currentP += 4*(currentX - currentY) + 10
        currentX += 1
        currentY -= 1

    second_octate.pop()

    second_octate.reverse()

    """ first quadrant """
    self.circle['1st'] = first_octate + second_octate  

    """ second quadrant """
    for x, y in self.circle['1st']:
      self.circle['2nd'].append((-x, y))

    """ third quadrant """
    for x, y in self.circle['2nd']:
      self.circle['3rd'].append((x, -y))
    
    """ fourth quadrant """
    for x, y in self.circle['1st']:
      self.circle['4th'].append((x, -y))
    
    return self.circle
  

circle_radius = int(input("Enter circle radius === "))

if(circle_radius < 0):
  raise ValueError("Circle radius must be positive")

pprint(BresenhamCircleDrawing(circle_radius).run())

