class Point:
    #Implement the class here
    getcount = 0
    def __init__(self, x_, y_):
        self._x = x_
        self._y = y_

    @staticmethod
    def getter_count():
        return Point.getcount

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
    coords = [(0,1),(10,5)]
    p1 = Point(coords[0][0], coords[0][1])
    p2 = Point(coords[1][0], coords[1][1])
    print(str(p1.getter_count()))
    print(str(p1.x), str(p2.x))
    print(str(p1.getter_count()))
