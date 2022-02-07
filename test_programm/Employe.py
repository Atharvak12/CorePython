from person import Person

class Employe(Person):
    def __init__(self, emp_id, salary, designation):
        super().__init__()
        self.__emp_id = emp_id
        self.__salary = salary
        self.__designation = designation

    def get_emp_id(self):
        return self.__emp_id

    def set_emp_id(self,emp_id):
        self.__emp_id = emp_id

    def get_salary(self):
        return self.__salary

    def get_designation(self):
        return self.__designation



e= Employe(2,5000,"engineer")
print(e.get_emp_id())
print(e.get_salary())
print(e.get_designation())
e.set_name("raj")
e.set_dob("112/03")
e.set_address("indore")

print(e.get_name())
print(e.get_dob())
print(e.get_address())