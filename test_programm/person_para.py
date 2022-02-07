class Perosn:
    def __init__(self, name,dob,address):
        self.__name = name
        self.__dob = dob
        self.__address = address

    def get_name(self):
        return self.__name

    def get_dob(self):
        return self.__dob

    def get_address(self):
        return self.__address


a = Perosn("atha","28/03","Indore")
print(a.get_name())
print(a.get_dob())
print(a.get_address())