class Chef:

    def make_chicken(self):
        print("The chef makes a chicken.")

    def make_salad(self):
        print("The chef makes a salad.")

    def make_special_dish(self):
        print("The chef makes bbq ribs.")

myChef = Chef()
myChef.make_special_dish()

class ChineseChef(Chef):

    def make_fried_rice(self):
        print("The chef makes friend rice.")

    def make_special_dish(self):
        print("The chef makes orange chicken.")

    def make_spring_rolls(self):
        print("The chef makes spring rolls.")

myChineseChef = ChineseChef()
myChineseChef.make_salad()
myChineseChef.make_special_dish()
myChineseChef.make_chicken()
myChineseChef.make_fried_rice()
myChineseChef.make_spring_rolls()