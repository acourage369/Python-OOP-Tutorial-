from student import Student
# An array of student objects
students = [

    Student("Brainy Yawson", 30, [70, 90, 67]),
    Student("Normson Solomon", 30, [75, 93, 62]),
    Student("Frank Nero", 30, [40, 95, 80])

]
# printing out student details
for student in students:
    print(f" Student name: {student.get_name()} \n Age: {student.get_age()} \n Average grade: {student.average()}")