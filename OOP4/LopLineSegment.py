import copy

class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def set_x(self, x):
        self.__x = x

    def get_y(self):
        return self.__y

    def set_y(self, y):
        self.__y = y

    def __str__(self):
        return f"({self.__x}, {self.__y})"


class LineSegment:
    # Constructor mặc định
    def __init__(self, d1=None, d2=None):
        if d1 is None:
            d1 = Point()
        if d2 is None:
            d2 = Point()
        # Sao chép sâu để tránh tham chiếu chung
        self.__d1 = copy.deepcopy(d1)
        self.__d2 = copy.deepcopy(d2)

    # Getter & Setter
    def get_d1(self):
        return self.__d1

    def set_d1(self, d1):
        self.__d1 = copy.deepcopy(d1)

    def get_d2(self):
        return self.__d2

    def set_d2(self, d2):
        self.__d2 = copy.deepcopy(d2)

    def __str__(self):
        return f"LineSegment: {self.__d1} -> {self.__d2}"


# Ví dụ sử dụng
p1 = Point(1, 2)
p2 = Point(4, 6)
line = LineSegment(p1, p2)
print(line)
