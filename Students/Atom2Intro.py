character_name = "George"
character_age = 50.3435

print("There once was an old man named " + character_name + ",")
print("he was " + str(character_age) + " years old.")
print("He really liked the name" + character_name + ",")
print("but he didn't like being " + str(character_age))

phrase = "Giraffe Academy"
print(phrase)
print(phrase + " is cool")
print(phrase.lower())
print(phrase.upper())
print(phrase.upper().isupper())
print(len(phrase))
print(phrase[3])
print(phrase.index("Acad"))

from math import *

#Numbers and Expressions

print(10 % 3)
my_num = -5
print(my_num)
print(str(my_num) + " my favorite number")
print(abs(my_num))
print(round(3.7))
print(ceil(3.7))
print(sqrt(3.7))

# name = input ("Enter your name: ")
# age = input("Enter your age: ")
# print("Hello " + name + "! You are " + age + "!")
#
#
# num1 = input("Enter a number: ")
# num2 = input("Enter another number: ")
# print(num1+num2)


train = "Python is a language"
print(train.isupper())
print(train)
print(train + "; a good one too.")
print(train.lower())
print(train.upper())
print(train.islower())
print(train.upper().isupper())
print(len(train))
print(train[12])
print(train.index("lang"))
print(train.replace("Python", "HTML"))

#Lists

lucky_numbers = [4, 7, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]
print(friends+lucky_numbers)
friends.extend(lucky_numbers)
print(friends)
print(friends.count("Jim"))
friends.append("Creed")
friends.insert(1, "Kelly")
friends.remove("Jim")
print(friends.index("Oscar"))
friends.sort()
lucky_numbers.reverse()
friends2 = list(friends)
print(friends)
print(lucky_numbers+friends)

#Tuples

coordinates = [(4,5), (6,7), (80,34)]
print(coordinates[1])


#Functions

def sayhi(name, age):
    print("Hello " + name + ", you are " + str(age) + ".")

sayhi("Mike", 35)


#Return

def cube(num):
    return num*num*num
#result = cube(4)

print(cube(4))


#If statments

is_male = False
is_tall = False

# if is_male or is_tall:
if is_male and is_tall:
    print("You are a male or tall or both.")
elif is_male and not(is_tall):
    print("You are a short male.")
elif is_tall and not(is_male):
    print("You are a not a male but are tall")
else:
    print("Your are not a male nor tall.")


#Comparisons

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
print(max_num(300, 4, 5))


#
# num1 = float(input("Enter first number: "))
# op = input("Enter operator: ")
# num2 = float(input("Enter second number: "))
#
# if op == "+":
    # print(num1 + num2)
# elif op == "-":
    # print(num1-num2)
# elif op == "/":
    # print(num1/num2)
# elif op == "*":
    # print(num1 * num2)
# else:
    # print("Invalid Operator")


#Dictionaries
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March,"
}

print(monthConversions["Feb"])
print(monthConversions.get("Jan"))
print(monthConversions.get("Luv", "Not a Valid Key"))

#While loops
i = 1
while i<= 10:
    print(i)
    i += 1

print("Done with loop")

#Guessing Game
# secret_word = "giraffe"
# guess = ""
# guess_count = 0
# guess_limit = 3
# out_of_guesses = False

# while guess != secret_word and not(out_of_guesses):
    # if guess_count < guess_limit:
        # guess = input("Enter guess: ")
        # guess_count +=1
    # else: out_of_guesses = True
#
# if out_of_guesses:
    # print("Out of guesses, YOU LOSE!")
# else
    # print("You Win!")


#For loops
friends = ["Jim", "Karen", "Kevin"]
for index in range(len(friends)):
    print(friends[index])

for index in range(5):
    if index ==0:
        print("FIRST ITERATION")
    else:
        print("Not First")

for letter in "Giraffe Academy":
    print(letter)

for index in range(10):
    print(index)

for index in range(3,10):
    print(index)

print(range(4))
#Exponent Functions
print(2**4)
def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(4,5))

#2D Lists & Nested loops
number_grid = [
[1,2,3],
[4,5,6],
[7,8,9],
[0]
]

print(number_grid[0][0])

for col in number_grid:
    for row in col:
        print(row)

#Try Except
try:
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid Input")

#Reading Files
employee_file = open ("employee.txt", "r")
print(employee_file.read())
print(employee_file.readlines())
for employee in employee_file.readlines():
    print(employee)
employee_file.close()

#Writing/Appending Files
employee_file = open("employee.txt", "a")
employee_file.write("\nKeep it cool bro.")
employee_file.close()

employee_file = open("employee.txt", "w")
employee_file.write("\nKeep it cool bro.")
employee_file.close()

#Modules and Pip
#import fractions
#print(fractions.whatever_function_you_need)
#import docx
#docx.whatever

#Classes and Objects
from student import student
student1 = Student("Jim", "Business", 3.1, False)
print(student1.name)

#Multiple Choice Quiz
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

question_prompts = [
"What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
"What color are bananas?\n(a) Teal\n(b) Magenta\n (c) Yellow\n\n",
"What color are strawberries\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b")
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct.")

#Translator
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))
