from abc import ABC, abstractmethod

class AbstractClass(ABC):
    @abstractmethod
    def abstract_method(self):
        pass

    def concrete_method(self):
        print("This is a concrete method.")

class ConcreteClass(AbstractClass):
    def abstract_method(self):
        print("This is the implementation of the abstract method in ConcreteClass.")

# Example usage:
# obj = AbstractClass()  # This will raise an error because you can't instantiate an abstract class

obj = ConcreteClass()
obj.abstract_method()
obj.concrete_method()

#abstract method for area and perimeter of rectangle
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
    
# Example usage:
rect = Rectangle(5, 10)
print("Area:", rect.area())
print("Perimeter:", rect.perimeter())
# Output:
# Area: 50
# Perimeter: 30

