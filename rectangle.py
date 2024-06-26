from dataclasses import dataclass
@dataclass
class Rectangle:
    width: float
    height: float


    def Perimeter(self):
        """Calculates the perimeter by adding twice the sum 
        of the width and height"""
        return 2 * (self.width + self.height)

    def Area(self):
        """Calculates the area by multiplying the width by 
        the height"""
        return self.width * self.height

    def __str__(self):
        """Generate a scaled string representation of the rectangle."""
        scale_factor = 2  # Adjust this to scale the rectangle's size in the visualization
        scaled_width = int(self.width) * scale_factor
        scaled_height = int(self.height) * scale_factor

        top_bottom = "+" + "-" * scaled_width + "+\n"
        side = "|" + " " * scaled_width + "|\n"

        representation = top_bottom + side * scaled_height + top_bottom
        return representation


@dataclass
class Square(Rectangle):
    def __init__(self, side: float):
        super().__init__(side, side) 


def main():
    try:
        shape_type = input("Enter the shape (rectangle/square): ").lower()
        if shape_type == "rectangle":
            width = float(input("Enter the width of the Rectangle: "))
            height = float(input("Enter the height of the Rectangle: "))
            rect = Rectangle(width, height)
            print(f"The perimeter of the rectangle is: {rect.Perimeter()}")
            print(f"The area of the rectangle is: {rect.Area()}")
            print("Visual representation of the rectangle:")
            print(rect)
        elif shape_type == "square":
            side = float(input("Enter the side length of the Square: "))
            sqr = Square(side)
            print(f"The perimeter of the square is: {sqr.Perimeter()}")
            print(f"The area of the square is: {sqr.Area()}")
            print("Visual representation of the square:")
            print(sqr)
        else:
            print("Invalid shape type entered. Please enter 'rectangle' or 'square'.")
    except ValueError:
        print("Please enter a valid number for dimensions")

if __name__ == "__main__":
    main()
