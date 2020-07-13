character_name = "George"
character_age = 50.3435
#
print("There once was an old man named " + character_name + ",")
print("he was " + str(character_age) + " years old.")
print("He really liked the name" + character_name + ",")
print("but he didn't like being " + str(character_age))
#
#
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
#
print(10 % 3)
my_num = -5
print(my_num)
print(str(my_num) + " my favorite number")
print(abs(my_num))
print(round(3.7))
print(ceil(3.7))
print(sqrt(3.7))
#
name = input ("Enter your name: ")
age = input("Enter your age: ")
print("Hello " + name + "! You are " + age + "!")
#
#
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = float(num1) + float(num2)
#
#
train = "Python is a language"
print(train)
print(train + "; a good one too.")
print(train.lower())
print(train.upper())
print(train.islower())
print(train.upper().isupper())
print(len(train))
print(train[12])
print(train.index("lang"))
print(train.replace("Java", "Python"))
#
color = input("Enter a color: ")
plural_noun = input("Enter a plural noun: ")
celebrity = input("Enter a celebrity: ")
athlete = input("Enter an athlete's name: ")
movie = input("Enter a movie: ")
song = input("Enter a song: ")
music_artist = input("Enter a famous singer: ")
tv_show = input("Enter your favorite TV Show: ")
pet = input("Enter the name of your pet: ")
social_media = input("Enter the name of your favorite social media app: ")
artist = input("Enter the name of your favorite artists: ")
#
#
print("Roses are " + color)
print(plural_noun + " are blue")
print("I love " + celebrity)
print(athlete + " is my favorite soccer player")
print(movie + " is pretty bad in my opinion")
print("Though, I do like that song : " + song + ".")
print("You've heard of " + social_media + ", right. I spend way too much time on that broski.")
print("I really love the paintings of " + artist + ".")

#
#Lists
#
lucky_numbers = [4, 7, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]
friends.extend(lucky_numbers)
friends.append("Creed")
friends.insert(1, "Kelly")
friends.remove("Jim")
friends.clear()
print(friends.index("Oscar"))
print(friends.count("Jim"))
friends.sort()
lucky_numbers.reverse()
friends2 = list(friends)
print(friends)
#
#
#Tuples
#
coordinates = [(4,5), (6,7), (80,34)]
print(coordinates[1])


#Functions

def sayhi(name, age):
    print("Hello " + name + ", you are " + str(age) + ".")

sayhi("Mike", 35)
sayhi("Steve", 70)


#Return

def cube(num):
    return num*num*num
# result = cube(4)
print(cube(3))


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
    print("You are not a male and not tall.")


#Comparisons

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(300, 4, 5))
