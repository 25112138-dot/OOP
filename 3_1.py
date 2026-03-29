import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def show(self):
        print(f"({self.x}, {self.y})")

    def distance_to(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def symmetric_origin(self):
        return Point(-self.x, -self.y)

# Tạo điểm A(3,4)
A = Point(3, 4)
A.show()

# Tạo điểm B từ bàn phím
x, y = map(int, input("Nhập tọa độ B (x y): ").split())
B = Point(x, y)
B.show()

# Điểm C đối xứng B qua gốc O
C = B.symmetric_origin()
print("C đối xứng B qua O:", end=" ")
C.show()
O = Point(0, 0)
# Tính khoảng cách
print("Khoảng cách B→O:", B.distance_to(O))
print("Khoảng cách A→B:", A.distance_to(B))
