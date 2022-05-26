class Rectangle:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def get_area(self) -> int:
        return self.width * self.height

    def get_perimeter(self) -> int:
        return (self.width * 2) + (self.height * 2)

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __str__(self):
        return f"{self.width} by {self.height}"


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

    def __repr__(self):
        return f"Square({self.width})"


rectangle = Rectangle(5, 10)
print(rectangle)
print(rectangle.get_area())
print(rectangle.get_perimeter())

square = Square(5)
print(square)
print(square.get_area())
print(square.get_perimeter())


print(isinstance(square, Square))
print(issubclass(Square, Rectangle))
