from person import Person
A = Person()

A.set_name("Atharva")
print("Namw: ",A.get_name())

A.set_dob("12/03/200")
print("Dob: ",A.get_dob())

A.set_address("Indore")
print("Address: ", A.get_address())

print("Age :", A.Avg_age)
print("Age :", Person.Avg_age)



new = Person()

new.set_name("Kabra")
print("Name :", new.get_name())

new.set_address("ujjain")
print("address :", new.get_address())

new.set_dob("03/02/2006")
print("dob :",new.get_dob())

print("Age :", new.Avg_age)