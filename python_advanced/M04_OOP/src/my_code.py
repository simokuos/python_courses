import math
class Point:
    getcount = 0
    def __init__(self, x_, y_):
        self._x = x_
        self._y = y_

    @staticmethod
    def getter_count():
        return Point.getcount

    @staticmethod
    def closest(p_list):
        min_dist = p_list[0].x **2 + p_list[0].y **2
        min_dist_index = 0
        for index, p in enumerate(p_list):
            temp_value = p.x ** 2 + p.y ** 2
            if(temp_value < min_dist):
                min_dist = temp_value
                min_dist_index = index

        min_dist = math.sqrt(min_dist)
        return min_dist

    @property
    def x(self):
        Point.getcount = Point.getcount+1
        return self._x

    @x.setter
    def x(self, v):
        self._x = v

    @property
    def y(self):
        Point.getcount = Point.getcount+1
        return self._y

    @y.setter
    def y(self, v):
        self._y = v

#Write test software under this if
if __name__ == "__main__":
    coords = [(2,1),(3,0)]
    p1 = Point(coords[0][0], coords[0][1])
    p2 = Point(coords[1][0], coords[1][1])
    print("get count:", str(p1.getter_count()))
    print("x coord for points:",str(p1.x), str(p2.x))
    print(str(p1.getter_count()))
    print(str(Point.getter_count()))
