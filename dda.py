import math
from pprint import pprint

class DDA:
  def __init__(self, cord):
    self.cord = cord

  def run(self):
    startX, startY, endX, endY = self.cord

    delX = endX - startX
    delY = endY - startY

    slope = delY / delX

    # step = None    
    # if slope <= 1: step = delX
    # else: step = delY
    
    step = delX if slope <=1 else delY

    xInc = delX / abs(step)
    yInc = delY / abs(step)

    output = [[startX, startY]]

    while True :
      if startX == endX or startY == endY: break

      startX += xInc
      startY += yInc

      output.append([startX, startY])

    return output
  
  
inputVal = list(map(int, input("Enter cordinates ").split()))

pprint(DDA(inputVal).run())