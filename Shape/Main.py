from rectangle import Rectangle
from circle import Circle

# An instance of a rectangle
rectangle = Rectangle(9.4, 5.7, "Rectangle")

# An instance of a circle
circle = Circle(5.4, "Circle")

print(f"Name: {rectangle.get_name()}")
print(f"Width: {rectangle.get_width()}cm")
print(f"Height: {rectangle.get_height()}cm")
print(f"Area of rectangle: {rectangle.calculate_area()}cm^2")
print(f"Perimeter of rectangle: {rectangle.calculate_perimeter()}cm")
print("\n")

print(f"Name: {circle.get_name()}")
print(f"Radius: {circle.get_radius()}cm")
print(f"Area of circle: {circle.calculate_area()}cm^2")
print(f"Perimeter of circle: {circle.calculate_perimeter()}cm")

