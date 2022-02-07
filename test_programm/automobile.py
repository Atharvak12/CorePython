class Automobile:
    Numebr_of_gear = 6
    def __init__(self,color,speed,make):
        self.__color = color
        self.__speed = speed
        self.__make = make

    def get_color(self):
        return self.__color

    def get_speed(self):
        return self.__speed

    def get_make(self):
        return self.__make


a= Automobile("Red","60km/hr","Mahindra")
print(a.get_color(),end=" ")
print(a.get_speed(),end=" ")
print(a.get_make(),end=" ")
print(a.Numebr_of_gear)