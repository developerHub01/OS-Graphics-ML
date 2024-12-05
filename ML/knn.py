import math
from pprint import pprint

class KNN:
  def __init__(self, dataset, newData, k=5) -> None:
    self.dataset = dataset
    self.newData = newData
    self.k = k

  def run(self):
    for index, data in enumerate(self.dataset):
      current_data = [data[0], data[1]]
      distance = self.distance(current_data, self.newData)
      current_color = self.dataset[index].pop()
      self.dataset[index].append(distance)
      self.dataset[index].append(current_color)
    
    self.dataset = self.sort()

    self.dataset = self.dataset[:self.k]

    return self.find_result_color()

  def distance(self, cord1, cord2):
    return math.sqrt((cord1[0] - cord2[0])**2 + (cord1[1] - cord2[1])**2)
  
  def sort(self):
    # return sorted(self.dataset, key=lambda x: x[2])
    return self.bubble_sort(self.dataset)
  
  def find_result_color(self):
    red_color = 0
    blue_color = 0

    for data in self.dataset:
      color = data[2]

      if color == "red":
        red_color += 1
      else:
        blue_color += 1
    return "red" if red_color > blue_color else "blue" 

  def bubble_sort(self, arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j][2] > arr[j+1][2]:  # Swap if the element is greater
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


knn1 = KNN([
    [40, 20, "red"],
    [50, 50, "blue"],
    [60, 90, "blue"],
    [10, 25, "red"],
    [70, 70, "blue"],
    [60, 10, "red"],
    [25, 80, "blue"],
  ],
  [20, 35],
  k=5
)
print(knn1.run())