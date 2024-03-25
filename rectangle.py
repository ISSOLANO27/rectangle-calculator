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


def main():
    try:
        Userwidth = float(input("Enter the width of the Rectangle: "))
        Userheight = float(input("Enter the height of the Rectangle: "))
    except ValueError:
        print("Please enter a valid number for the width adn height")

    # Create a rectangle object with the provided dimensions
    rect = Rectangle(Userwidth, Userheight)
    print(f"The perimeter of the rectangle is: {rect.Perimeter}")
    print(f"The area of the rectangle is: {rect.Area} ")

    print("Visual representation of the rectangle")
    print(rect)

if __name__ == "__main__":
    main()

