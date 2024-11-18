from pprint import pprint

class MidPointEllipse:
  def __init__(self, a, b, centerX=0, centerY=0):
    self.centerX = centerX
    self.centerY = centerY
    self.a = a
    self.b = b

    self.ellipse = {
      "1st": [],
      "2nd": [],
      "3rd": [],
      "4th": [],
    }
    
  
  def draw(self):
    x = 0
    y = self.b

    dx = 2 * x * self.b ** 2
    dy = 2 * y * self.a ** 2

    p = self.b ** 2 - self.a ** 2 * self.b + self.a ** 2 / 4

    while (dx < dy) :
      self.ellipse["1st"].append([x, y])

      if (p < 0) :
        x += 1
        dx += 2 * self.b ** 2
        p += dx + self.b ** 2
      else:
        x += 1
        y -= 1
        dx += 2 * self.b ** 2
        dy -= 2 * self.a ** 2
        p += dx - dy + self.b ** 2
    
      q = self.b ** 2 * (x + 1 / 2) ** 2 + self.a ** 2 * (y - 1) ** 2 - self.a ** 2 * self.b ** 2

    while y >= 0:
      self.ellipse["1st"].append([x, y])

      if q > 0:
        y -= 1
        dy += -2 * self.a ** 2
        q += self.a ** 2 - dy
      else:
        y -= 1
        x += 1
        dx += 2 * self.b ** 2
        dy -= 2 * self.a ** 2
        q += dx - dy + self.a ** 2

    
    for x,y in self.ellipse['1st']:
      self.ellipse['2nd'].append([-1 * x, y])
      self.ellipse['3rd'].append([-1 * x, -1 * y])
      self.ellipse['4th'].append([x, -1 * y])
      
    return self.ellipse


a, b, centerX, centerY = list(map(int, input("Enter a, b, centerX, centerY = ").split()))

midPointEllipse1 = MidPointEllipse(a, b, centerY, centerY)

pprint(midPointEllipse1.draw())
