class Chef:

    def make_chicken(self):
        print("The chef makes a chicken.")

    def make_salad(self):
        print("The chef makes a salad.")

    def make_special_dish(self):
        print("The chef makes bbq ribs.")

myChef = Chef()
myChef.make_special_dish()
myChef.make_salad()

class ChineseChef(Chef):

    def make_chicken(self):
        print("The Chinese chef makes a chicken.")

    def make_fried_rice(self):
        print("The Chinese chef makes friend rice.")

    def make_special_dish(self):
        print("The Chinese chef makes orange chicken.")

    def make_spring_rolls(self):
        print("The Chinese chef makes spring rolls.")

myChineseChef = ChineseChef()
myChineseChef.make_salad()
myChineseChef.make_special_dish()
myChineseChef.make_chicken()
myChineseChef.make_fried_rice()
myChineseChef.make_spring_rolls()

class IndianChef(Chef):

    def make_naan(self):
        print("The Indian chef makes naan.")

    def make_special_dish(self):
        print("The Indian Chef makes tandoori chicken.")

    def make_paneer(self):
        print("The Indian Chef makes paneer.")

myIchef = IndianChef()
myIchef.make_naan()
myIchef.make_chicken()
myIchef.make_special_dish()
myIchef.make_paneer()
myIchef.make_salad()
myIchef.make_naan()
myIchef.make_chicken()
myIchef.make_special_dish()
myIchef.make_paneer()
