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

class ItalianChef(Chef):

    def make_special_dish(self):
        print("The Italian chef makes shrimp alfredo.")

    def make_spaghetti(self):
        print("The Italian chef makes spaghetti.")

    def make_lasagna(self):
        print("The Italian chef makes lasagna.")

myItal = ItalianChef()
myItal.make_lasagna()
myItal.make_spaghetti()
myItal.make_special_dish()
myItal.make_chicken()
myItal.make_salad()
myItal.make_spaghetti()
myItal.make_special_dish()
myItal.make_chicken()
myItal.make_salad()


class IndoChineseChef(IndianChef):

    def make_roti_kanan(self):
        print("The IndoChinese chef makes roti kanan.")

    def make_singaporean_noodles(self):
        print("The IndoChinese chef makes singaporean noodles.")

    def make_special_dish(self):
        print("The IndoChinese chef makes fish curry.")


myId = IndoChineseChef()
myId.make_chicken()
myId.make_special_dish()
myId.make_roti_kanan()
myId.make_singaporean_noodles()
myId.make_naan()
myId.make_paneer()
myId.make_salad()
myId.make_chicken()
myId.make_special_dish()
