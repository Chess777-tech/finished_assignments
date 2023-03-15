import math

class Shape:
    def __init__(self, color, size):
        self.color = color
        self.size = size

    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, color, size, radius):
        super().__init__(color, size)
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, color, size, width, height):
        super().__init__(color, size)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Triangle(Shape):
    def __init__(self, color, size, side1, side2, side3):
        super().__init__(color, size)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

# Example usage:
my_circle = Circle("red", "small", 5)
print(f"Area of my_circle is {my_circle.area()}") # Area of my_circle is 78.53981633974483
print(f"Perimeter of my_circle is {my_circle.perimeter()}") # Perimeter of my_circle is 31.41592653589793

my_rectangle = Rectangle("green", "medium", 3, 4)
print(f"Area of my_rectangle is {my_rectangle.area()}") # Area of my_rectangle is 12
print(f"Perimeter of my_rectangle is {my_rectangle.perimeter()}") # Perimeter of my_rectangle is 14

my_triangle = Triangle("blue", "large", 3, 4, 5)
print(f"Area of my_triangle is {my_triangle.area()}") # Area of my_triangle is 6.0
print(f"Perimeter of my_triangle is {my_triangle.perimeter()}") # Perimeter of my_triangle is 12
