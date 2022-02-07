
class Shape:
    PI = 3.14
    def __init__(self):
        self.__color = ""
        self.__bgwidth = ""

    def set_color(self, color):
        self.__color = color

    def get_color(self):
        return self.__color

    def set_bgwidth(self, bgwidth):
        self.__bgwidth = bgwidth

    def get_bgwidth(self):
        return self.__bgwidth


s = Shape()
s.set_color("Red")
print(s.get_color())
s.set_bgwidth(10)
print(s.get_bgwidth())