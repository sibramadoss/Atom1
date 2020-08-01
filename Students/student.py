class Student:

    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    def on_honor_roll(self):
        if self.gpa  >= 3.5:
            return "Congratulations, you are on the honor roll"
        else:
            return "Sorry, we are informing you today that you are not on the honor roll."

    def engineering(self):
        if "Engineering" in self.major:
            return "$1,000,000 starting"
        elif "Computer Science" in self.major:
            return "$1,000,000 starting"
        elif "Pre-Medicine" in self.major:
            return "$50,000 starting"
        else:
            return "$500,000 starting"

    def years_to_manage(self):
        if "SOE" in self.major:
            return "5 years needed"
        elif "SAS" in self.major:
            return "3 years needed"
        else:
            return "7 years needed"

    def scholar(self):
        if self.gpa >= 3.75 and self.is_on_probation == False:
            return "You are eligible for a scholarship"
        else:
            return "You are not eligible for a scholarship"

    def med_sch(self):
        if self.gpa >= 3.65 and "Pre-Medicine" in self.major:
            return "You are eligible for Medical School"
        elif self.gpa >=3.65 and "Pre-Medicine" not in self.major:
            return "You are qualified but are not on the right track for Medical School"
        else:
            return "You are not eligible for Medical School"

class Question:

    def __init__(self, prompt, answer):

# REVIEW:        self.prompt = prompt
        self.answer = answer
