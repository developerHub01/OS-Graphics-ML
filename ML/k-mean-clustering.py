import math

class K_Mean_Clustering:
  def __init__(self, dataset):
    self.dataset = dataset

  def run(self):
    print("step == 1")
    self.central_variable = self.dataset[:2]
    print(f"central variable = {self.central_variable}")
    print("============================")

    for i in range(2, len(self.dataset)):
      print(f"step == {i}")
      print(f"data point = {self.dataset[i]}")
      distance1 = self.distance(self.central_variable[0], self.dataset[i])
      distance2 = self.distance(self.central_variable[1], self.dataset[i])

      print(f"distance 1 = {distance1} | distance 2 = {distance2}")

      if distance1 < distance2:
        self.central_variable[0] = self.meanCord(self.central_variable[0], self.dataset[i])
      else:
        self.central_variable[1] = self.meanCord(self.central_variable[1], self.dataset[i])
      
      print(f"central variable = {self.central_variable}")
      print("============================")
  
  def distance(self, cord1, cord2):
    return math.sqrt((cord1[0] - cord2[0])**2 + (cord1[1] - cord2[1])**2)

  def meanCord(self, previousCord, newCord):
    return [(previousCord[0] + newCord[0]) / 2, (previousCord[1] + newCord[1]) / 2]

k_mean_clustering = K_Mean_Clustering([
  [20, 500],
  [40, 1000],
  [30, 800],
  [18, 300],
  [28, 1200],
  [35, 1400],
  [45, 1800],
])
k_mean_clustering.run()