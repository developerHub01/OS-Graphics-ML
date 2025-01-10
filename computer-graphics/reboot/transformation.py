import math

class Transformation:
    def __init__(self, cord):
        self.cord = cord

    def translate(self, tx, ty):
        self.cord[0] += tx
        self.cord[1] += ty

        return self.cord
    
    def scale(self, sx, sy):
        self.cord[0] *= sx
        self.cord[1] *= sy

        return self.cord

    def rotate(self, angle):
        radian_angle = math.radians(angle)

        x, y = self.cord
    
        self.cord[0] = x*math.cos(radian_angle) - y*math.sin(radian_angle)
        self.cord[1] = x*math.sin(radian_angle) + y*math.cos(radian_angle)

        self.cord[0] = round(self.cord[0], 10)
        self.cord[1] = round(self.cord[1], 10)

        return self.cord

    def reflact(self):
        self.cord[0] = -1 * self.cord[0]
        self.cord[1] = -1 * self.cord[1]

        return self.cord

    def shearing(self, sx, sy):
        self.cord[0] += self.cord[1] * sx
        self.cord[1] += self.cord[0] * sy

        return self.cord


if __name__ == "__main__":
    # transformation1 = Transformation([2, 3])

    # print(transformation1.translate(3, 5))
    # print(transformation1.rotate(30))
    # print(transformation1.scale(2, 2))
    # print(transformation1.shearing(2, 3))
    # print(transformation1.reflact())

    # transformation1 = Transformation([4, 3])
    # print(transformation1.scale(3, 5))

    transformation1 = Transformation([1, 0])
    print(transformation1.rotate(90))