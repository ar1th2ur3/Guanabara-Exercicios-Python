from time import sleep

def calculateTriangleType(side1, side2, side3):
    if side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
        return "Cannot form a triangle."
    
    if side1 == side2 == side3:
        return "Can form an Equilateral triangle."
    elif side1 == side2 or side2 == side3 or side3 == side1:
        return "Can form an Isosceles triangle."
    else:
        return "Can form a Scalene triangle."

def calculateArea(side1, side2, side3):
    # Using Heron's formula to calculate the area of a triangle
    s = (side1 + side2 + side3) / 2
    area = (s * (s - side1) * (s - side2) * (s - side3)) ** 0.5
    return area

def main():
    print("Develop a program that reads the lengths of three sides and provides information about the triangle.")
    sleep(2)
    
    try:
        side1 = float(input("Enter the length of the first side: "))
        side2 = float(input("Enter the length of the second side: "))
        side3 = float(input("Enter the length of the third side: "))
    except ValueError:
        print("Invalid input. Please enter valid numeric values for the side lengths.")
        return

    if side1 <= 0 or side2 <= 0 or side3 <= 0:
        print("Side lengths must be positive values.")
        return

    message = calculateTriangleType(side1, side2, side3)
    area = calculateArea(side1, side2, side3)

    print(f"Triangle Type: {message}")
    print(f"Area of the triangle: {area:.2f} square units")

if __name__ == "__main__":
    main()
