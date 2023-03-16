from person import Person


class Employee(Person):

    def __init__(self, first_name, last_name, age, gender, phone, salary, jobtitle):
        super().__init__(first_name, last_name, age, gender, phone)
        self.salary = salary
        self.jobtitle = jobtitle

    def get_salary(self):
        return self.salary

    def get_job_title(self):
        return self.jobtitle

