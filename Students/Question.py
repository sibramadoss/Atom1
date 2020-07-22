
from student import Question
history = Question("How old is Sibhi?", "A")
print(history.prompt)
print(history.answer)

from student import Student
student1 = Student("Thilaga", "Zoology", 3.7, False)
student2 = Student("Sibhi", "Computer Engineering", 3.99, False)
print(student1.name)
print(student1.gpa)
print(student1.is_on_probation)
print(student1.on_honor_roll())
print(student2.name)
print(student2.gpa)
print(student2.is_on_probation)
print(student2.on_honor_roll())
