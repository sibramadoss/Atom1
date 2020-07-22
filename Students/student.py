class Student:

    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    def on_honor_roll(self):
        if self.gpa  >= 3.5:
            return "Congratulations"
        else:
            return "Sorry, we are informing you today that you are not on the honor roll."


class Question:

    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer
