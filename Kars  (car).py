class car(object):
    def __init__(self, condition, model, color, mpg):
        self.condition = condition
        self.model =  model
        self.color = color
        self.mpg = mpg
        print(condition, model, color, mpg)
    def display_car(self):
        print("This is a " + self.model + self.color + " car with " + self.mpg + " MPG.")
    def drive_car(self):
        print("This is a " + "used " + self.model + self.color + " car with " + self.mpg + " MPG.")
    
my_car = car("new", "DeLorian ", "silver","88")
my_car.display_car()
my_car.drive_car()

class electric_car(object):
    def __init__(self, battery, condition, model, color):
        self.battery = battery
        self.condition = condition
        self.model = model
        self.color = color
    def display_car(self):
        print("This is a " + self.condition + self.color + self.model + " electric car")
    def drive_car(self):
        print("This is a " + "like new " + self.model + self.color + " with a " + self.battery + " battery.")

my_electric_car = electric_car("molten salt ", "new ", " Tesla ", " blue.")
my_electric_car.display_car()
my_electric_car.drive_car()