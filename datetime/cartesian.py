import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def getx(self):
        return self.__x

    def gety(self):
        self.__y

    def distance_from_xy(self, x, y):
        base_val = self.__x - x
        perp_val = self.__y - y
        return math.hypot(base_val, perp_val)

    def distance_from_point(self, point):
        base_val = self.__x - point.x
        perp_val = self.__y - point.y
        return math.hypot(base_val, perp_val)


if __name__ == '__main__':
    point1 = Point(0, 0)
    point2 = Point(1, 1)
    print(point1.distance_from_point(point2))
    print(point2.distance_from_xy(2, 0))
