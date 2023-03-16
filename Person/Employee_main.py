from employee import Employee

# calling the employee class  which inherits from the parent class "Person" and assigning it to a variable
employee = Employee("Brainy", "Yawson", 32, "Male", "0552233328", 12000, "Product Manager")

# Taping the methods in the persons class
print(f"Name: {employee.get_name()}")
print(f"Age: {employee.get_age()}")
print(f"Gender: {employee.get_gender()}")
print(f"Phone: {employee.get_phone()}")
print(f"Salary: ${employee.get_salary()}")
print(f"Job title: {employee.get_job_title()}")
