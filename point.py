import random

class Point:
    """
    Class modeling a real life 2D point
    """
    a = 7
    def __init__(self, x, y):
        """
        Initialize the point instance
        :param x: the x axis coordinate value
        :param y: the y axis coordinate value
        """
        self.x = x
        self.y = y

    def __str__(self):
        """
        Magic method that defines how a Point is printed
        :return:
        """
        return f"<{self.x}, {self.y}>"

    def __repr__(self):
        return self.__str__()

    def distance_origin(self):
        """
        Calculate the distance of the point from the origin
        :return: the distance from the origin
        """
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __gt__(self, other):
        """
        Magic method that is called when you do self>other
        :param other: the other point to compare to
        :return: True/False
        """
        return self.distance_origin() > other.distance_origin()

    def __eq__(self, other):
        """
        Magic method that is called when you do self==other
        :param other: the other point to compare to
        :return: True/False
        """
        return self.distance_origin() == other.distance_origin()

if __name__ == "__main__":
    p1 = Point(1, 2)

p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = Point("James", "Jane") # This is valid, but probably not intended

print (p1.x, p1.y) # Access attributes of p1

points = []
for i in range (5):
    p = Point(
        random.randint(-100, 100),
        random. randint(-100, 100)
    )
    # Append it to the list
    points.append(p)
for point in points:
    print(point)

print (points)
p = Point(12, 5)
print(p.distance_origin())

print(p1 > p2)
print(p1 == p2)

print ("Unsorted Points")
print(points)
print ("Sorted Points")
points.sort()
print(points)

found_equal = 0
count = 0
while True:
    if found_equal == 100:
        break
    p1 = Point(
        random.randint(-100, 100),
        random.randint(-100, 100)
    )
    p2 = Point(
        random.randint(-100, 100),
        random.randint(-100, 100)
    )
    count += 1
    if p1 == p2:
        print(p1,p2)
        found_equal += 1

print (f"Probability is 1 in {count/found_equal}")

