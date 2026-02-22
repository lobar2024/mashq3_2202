class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Point(x=%s, y=%s)" % (self.x, self.y)

print(Point(1, 2))
