""" 
Pk = 3 * 2d

if pk < 0
    yk+1 = yk
    pk+1 = pk + 4xk+1 + 6

if pk >= 0
    yk+1 = yk + 1
    pk+1 = pk + 4(xk+1 - yk+1) + 10

"""

from pprint import pprint
import matplotlib.pyplot as plt

class BresenhamCircle:
    def __init__(self, radius, center_cord=[0, 0]):
        self.radius = radius
        self.center_cord = center_cord
        self.circle_quadrants = {
            "1": [],
            "2": [],
            "3": [],
            "4": [],
        }

    def run(self):
        current_x = 0
        current_y = self.radius
        
        first_octet = [[current_x, current_y]]
        pk = 3 - 2*self.radius

        while current_x < current_y:
            if pk < 0:
                current_x += 1
                pk += 4*current_x + 6
            else:
                current_x += 1
                current_y -= 1
                pk += 4*(current_x - current_y) + 10
            
            first_octet.append([current_x, current_y])
        
        second_octet = []

        for index in range(len(first_octet)):
            x, y = first_octet[len(first_octet) - index - 1]
            if [y, x] in first_octet: continue
            second_octet.append([y, x])
        
        first_quadrants = first_octet + second_octet
        
        self.circle_quadrants["1"] = first_quadrants
        
        for x, y in self.circle_quadrants["1"]:
            self.circle_quadrants["2"].append([-1 * x, y])

        for x, y in self.circle_quadrants["1"]:
            self.circle_quadrants["3"].append([-1 * x, -1 * y])

        for x, y in self.circle_quadrants["1"]:
            self.circle_quadrants["4"].append([x, -1 * y])

        self.circle_quadrants["1"].pop()
        self.circle_quadrants["2"].pop(0)
        self.circle_quadrants["3"].pop()
        self.circle_quadrants["4"].pop(0)


        if self.center_cord[0] != 0 and self.center_cord[1] != 0:
            self.change_center_cord()

        return self.circle_quadrants
    
    def change_center_cord(self):
        for index, value in enumerate(self.circle_quadrants["1"]):
            x, y = value
            self.circle_quadrants["1"][index] = [x + self.center_cord[0], y + self.center_cord[1]]

        for index, value in enumerate(self.circle_quadrants["2"]):
            x, y = value
            self.circle_quadrants["2"][index] = [x + self.center_cord[0], y + self.center_cord[1]]

        for index, value in enumerate(self.circle_quadrants["3"]):
            x, y = value
            self.circle_quadrants["3"][index] = [x + self.center_cord[0], y + self.center_cord[1]]

        for index, value in enumerate(self.circle_quadrants["4"]):
            x, y = value
            self.circle_quadrants["4"][index] = [x + self.center_cord[0], y + self.center_cord[1]]


def draw_circle(circle_data):
    # Extract points from all quadrants
    x_points, y_points = [], []
    for quadrant in circle_data.values():
        for x, y in quadrant:
            x_points.append(x)
            y_points.append(y)
    
    # Plot the points
    plt.figure(figsize=(6, 6))
    plt.scatter(x_points, y_points, color="blue", s=10)  # Small dots
    plt.gca().set_aspect('equal', adjustable='box')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.title("Bresenham Circle")
    plt.show()


if __name__ == "__main__":
    # radius, center_x, center_y = map(int, input("radius, center x, center_y = "))
    # bresenham_circle1 = BresenhamCircle(radius, [center_x, center_y])
    # bresenham_circle1 = BresenhamCircle(8, [0, 0])
    bresenham_circle1 = BresenhamCircle(100, [3, 5])
    circle_data = bresenham_circle1.run()
    pprint(circle_data)
    draw_circle(circle_data)