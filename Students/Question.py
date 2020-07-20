
from student import Question
history = Question("How old is Sibhi?", "A")
print(history.prompt)
print(history.answer)


from student import Student
student1 = Student("Jim", "Business", 3.1, False)
print(student1.name)
print(student1.gpa)
print(student1.is_on_probation)
