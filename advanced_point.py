from color_point import ColorPoint

class AdvancedPoint(ColorPoint):
    COLORS = ["red", "green", "blue", "black", "white"]

    def _init_ (self, x, y, color):
        """
        Initialize an AdvancedPoint with x, y, and color, with validation.
        """
        if not isinstance(x, (int, float)):
            raise TypeError("x must be a number")
        if not isinstance(y, (int, float)):
            raise TypeError("y must be a number")
        if not color in self.COLORS:
            raise ValueError(f"color must be one of: {self.COLORS}")
        # super()._init_(x, y, color) #call the init method of the parent
        self._x = x
        self._y = y
        self._color = color

    @property
    def x(self):
        """
        Return x-coordinate.
        """
        return self._x

    @property
    def y(self):
        """
        Return y-coordinate.
        """
        return self._y

    @property
    def color(self):
        """
        Return color.
        """
        return self._color

    @color.setter
    def color(self, new_color):
        """
        Set a new color if it's in the allowed COLORS list.
        """
        if new_color not in AdvancedPoint.COLORS:
            raise ValueError(f"color must be one of: {AdvancedPoint.COLORS}")
        self._color = new_color

    @classmethod
    def add_color(cls, new_color):
        """
        Add new color to COLORS list.
        """
        cls.COLORS.append(new_color)

    @staticmethod
    def distance_2_points(p1, p2):
        """
        Return the distance between the points.
        """
        return ((p1.x - p2.x)* 2 + (p1.y - p2.y)2)*0.5

    @staticmethod
    def from_dictionary(dict):
        """
        Create an AdvancedPoint from a dictionary with optional values.
        """
        x = dict.get("x", 10)
        y = dict.get("y", 20)
        color = dict.get("color", "black")
        return AdvancedPoint(x, y, color)


AdvancedPoint.add_color("amber")
p2 = AdvancedPoint( 1, 2, "red")
print(p2.x)
print(p2.y)
p2.color = "blue"
print(p2)
p3 = AdvancedPoint(-1, -2, "blue")
print(AdvancedPoint.distance_2_points(p2, p3))
p4 = AdvancedPoint.from_dictionary({"x": 44})
print(p4)