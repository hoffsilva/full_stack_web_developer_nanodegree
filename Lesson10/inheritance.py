class Parent():
    def __init__(self, last_name, eye_color):
        print("Parent Constructor Called")
        self.last_name = last_name
        self.eye_color = eye_color

    def showInfo(self):
        print("Last Name: " + self.last_name)
        print("Eye color: " + self.eye_color)

class Child(Parent):
    def __init__(self, last_name, eye_color, numer_of_toys):
        print("Constructor of Child Called")
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = numer_of_toys

    def showInfo(self):
        print("Last Name: " + self.last_name)
        print("Eye color: " + self.eye_color)
        print("Number of toys: " + str(self.number_of_toys))




#
# billy_cyrus = Parent("Cyrus", "blue")
# billy_cyrus.showInfo()
# print(billy_cyrus.last_name)
# #
miley_cyrus = Child("Cyrus", "Blue", 5)
print(miley_cyrus.last_name)
print(miley_cyrus.number_of_toys)
miley_cyrus.showInfo()
