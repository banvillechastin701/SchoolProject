import math

def calculate_area(shape):
    if shape == "circle":
        radius = float(input("Enter the radius of the circle: "))
        return math.pi * radius ** 2
    elif shape == "square":
        side = float(input("Enter the length of a side of the square: "))
        return side * side
    elif shape == "rectangle":
        width = float(input("Enter the width of the rectangle: "))
        height = float(input("Enter the height of the rectangle: "))
        return width * height
    else:
        print("Invalid shape. Please enter either 'circle', 'square', or 'rectangle'.")
        return -1

print(calculate_area("circle"))