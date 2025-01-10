""" 
Pk = 1 - r

pk < 0:
    xk+1 = xk + 1
    yk+1 = yk

    pk+1 = pk + 2xk + 3

pk >= 0:
    xk+1 = xk + 1
    yk+1 = yk - 1
    
    pk+1 = pk + 2*(xk - yk) + 5

"""

from pprint import pprint
import matplotlib.pyplot as plt

class MidPointCircle:
    def __init__(self, radius, center_cord=[0, 0]):
        self.radius = radius
        self.center_cord = center_cord
        print(self.center_cord)
        self.circle_quadrants = {
            "1": [],
            "2": [],
            "3": [],
            "4": [],
        }


    def run(self):
        current_x = 0
        current_y = self.radius

        first_octent = [[current_x, current_y]] 

        pk = 1 - self.radius

        while current_x < current_y:
            if pk < 0:
                pk += 2*current_x + 3
                current_x += 1
            else:
                pk += 2*(current_x - current_y) + 5
                current_x += 1
                current_y -= 1

            first_octent.append([current_x, current_y])

        second_octent = []

        for index in range(len(first_octent)):
            x, y = first_octent[len(first_octent) - index - 1]
            if [y, x] in first_octent: continue
            second_octent.append([y, x])
        
        self.circle_quadrants['1'] = first_octent + second_octent

        for x, y in self.circle_quadrants['1']:
            self.circle_quadrants['2'].append([-1 * x, y])

        for x, y in self.circle_quadrants['1']:
            self.circle_quadrants['3'].append([-1 * x, -1 * y])

        for x, y in self.circle_quadrants['1']:
            self.circle_quadrants['4'].append([x, -1 * y])

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
    # mid_point_circle1 = MidPointCircle(radius, [center_x, center_y])
    mid_point_circle1 = MidPointCircle(7, [0, 0])
    mid_point_circle1 = MidPointCircle(10, [10, 5])
    circle_data = mid_point_circle1.run()
    # pprint(circle_data) 
    draw_circle(circle_data)