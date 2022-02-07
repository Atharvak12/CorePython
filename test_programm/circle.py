
class Circle(shape):
    def __init__(self):
        self.__radius = ""

    def get_radius(self):
        return self.__radius

    def set_radius(self,radius):
        self.__radius = radius

    def area(self):
        return self.__radius**2**shape.PI


c = Circle()
c.set_area(5)
print(c.get_area())