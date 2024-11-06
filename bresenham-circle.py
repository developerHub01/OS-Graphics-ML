from pprint import pprint

class BresenhamCircleDrawing:
  def __init__(self, redius, center):
    self.redius = redius
    self.center = center
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

    tempCircle = {
      "1st": [],
      "2nd": [],
      "3rd": [],
      "4th": [],
    }

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
    tempCircle['1st'] = first_octate + second_octate  

    """ second quadrant """
    for x, y in tempCircle['1st']:
      tempCircle['2nd'].append((-x, y))

    """ third quadrant """
    for x, y in tempCircle['2nd']:
      tempCircle['3rd'].append((x, -y))
    
    """ fourth quadrant """
    for x, y in tempCircle['1st']:
      tempCircle['4th'].append((x, -y))

    

    """ 1st quadrant """
    for x, y in tempCircle['1st']:
      if y == 0: continue
      self.circle['1st'].append((x, y))

    """ 2nd quadrant """
    for x, y in tempCircle['2nd']:
      if x == 0: continue
      self.circle['2nd'].append((x, y))

    """ third quadrant """
    for x, y in tempCircle['3rd']:
      if y == 0: continue
      self.circle['3rd'].append((x, y))
    
    """ fourth quadrant """
    for x, y in tempCircle['4th']:
      if x == 0: continue
      self.circle['4th'].append((x, y))


    return self.circle
  

circle_radius = int(input("Enter circle radius === "))
circle_center = list(map(int, input("Enter circle radius === ").split()))

if(circle_radius < 0):
  raise ValueError("Circle radius must be positive")

pprint(BresenhamCircleDrawing(circle_radius, circle_center).run())

