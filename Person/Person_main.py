from person import Person
from employee import Employee

# calling the persons class and assigning it to a variable
person = Person("Brainy", "Yawson", 32, "Male", "0552233328")

employee = Employee()

# Taping the methods in the persons class
print(f"Name: {person.get_name()}")
print(f"Age: {person.get_age()}")
print(f"Gender: {person.get_gender()}")
print(f"Phone: {person.get_phone()}")
print(f"Salary: {employee.get_salary()}")
print(f"Job title: {employee.get_jobtitle()}")
