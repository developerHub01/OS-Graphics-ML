from pprint import pprint

class Bresenham:
  def __init__(self, cord):
    self.x1, self.y1, self.x2, self.y2 = cord
    
    self.output = [[self.x1, self.y1]]
    
  def run(self):
    delX = self.x2 - self.x1
    delY = self.y2 - self.y1

    slope = delY / delX
    
    currentP = 2 * delY - delX
    
    if slope >= 1:
      currentP = 2 * delX - delY
    
    currentX = self.x1
    currentY = self.y1
    
  
    while ((slope < 1 and currentX < self.x2) or
      (slope >= 1 and currentY < self.y2)):
      
      if slope < 1 and currentP < 0:
        currentP += 2 * delY
        currentX += 1
      elif slope < 1 and currentP >= 0:
        currentP += 2 * delY - 2 * delX
        currentY += 1
        currentX += 1
      elif slope >= 1 and currentP < 0:
        currentP += 2 * delX
        currentY += 1
      elif slope >= 1 and currentP >= 0:
        currentX += 1
        currentY += 1
        currentP += 2 * delX - 2 * delY

      self.output.append([currentX, currentY])

    return self.output
  
    # if slope < 1:
    #   while(currentX < self.x2):
        
    #     if currentP < 0:
    #       currentP = currentP + 2 * delY
    #     else:
    #       currentP = currentP + 2 * delY - 2 * delX
    #       currentY += 1
          
    #     currentX += 1

    #     print(currentX, currentY)

    #     self.output.append([currentX, currentY])
        
    # else: 
    #    while(currentY < self.y2):
        
    #     if currentP < 0:
    #       currentP = currentP + 2 * delX
    #     else:
    #       currentP = currentP + 2 * delX - 2 * delY
    #       currentX += 1
          
    #     currentY += 1
    #     self.output.append([currentX, currentY])
        
    # return self.output
  
inputVal = list(map(int, input("Enter cordinates ").split()))

pprint(Bresenham(inputVal).run())