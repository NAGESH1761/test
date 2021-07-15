##Write a Python class named Student with two instances student1, student2 and assign given values to
##the said instances attributes. Print all the attributes of student1, student2 instances with their values
class Student:
    school = 'forward thinking'
    address = '2626/Z Overlook Drive, COLUMBUS' 
student1 = Student()
student2 = Student() 
student1.student_id = "v12"
student1.student_name = "N"
student2.student_id = "v12"
student2.marks_language = 85
student2.marks_science = 93
student2.marks_math = 95 
students = [student1, student2]
for student in students:
    print('\n')
    for attr in student.__dict__:
        print(f'{attr} -> {getattr(student, attr)}')


#OUTPUT
##student_id -> v12
##student_name -> N
##
##
##student_id -> v12
##marks_language -> 85
##marks_science -> 93
##marks_math -> 95
