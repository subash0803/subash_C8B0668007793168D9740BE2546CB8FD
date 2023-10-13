"""
Implement a function called sort_student that take a list of student objects as input and sorted the list based on theri CGPA in descending order.each student objects has the following attributes:name(string),roll_no(string),cgpa(float).test the function with diffrent input list of students
"""


class Student:

  def __init__(self, name, roll_no, cgpa):
    self.name = name
    self.roll_no = roll_no
    self.cgpa = cgpa


def sort_students(student_list):
  sorted_students = sorted(student_list,
                           key=lambda student: student.cgpa,
                           reverse=True)
  return sorted_students


#Example usage
students = [
    Student("hari", "A123", "7.8"),
    Student("sam", "A124", "8.9"),
    Student("nive", "A125", "9.1"),
    Student("maya", "A126", "9.8"),
]
sorted_students = sort_students(students)
for student in sorted_students:
  print("Name:{},Roll No:{},CGPA:{}".format(student.name, student.roll_no,
                                            student.cgpa))
