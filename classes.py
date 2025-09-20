# object are bundle of relative attributes (variable) and methods(function)
      # example: Car, Person, BOOK ETC
      # YOU NEED A CLASS TO CREATE AS MANY OBJECTS AS YOU WANT

#CLASS : blueprint for creating objects (USE TO DESIGN THE STRUCTURE AND LAYOUT OF THE OBJECT)
#OBJECT : instance of a class


class Car:
    manufacture_year = 2024 # CLASS ATTRIBUTE
    def __init__(self,name,color,model,for_sale): # CONSTRUCTOR
        self.name =name
        self.color =color
        self.model =model
        self.for_sale =for_sale

    def drive(self,  age):
        self.age = age
        if self.age>=18:
            print(f"you can drive {self.name}")
        else:
            print(f"You are under Age")
    def describe(self):
        print(f"Name: {self.name}")
        print(f"Color: {self.color}")
        print(f"Model: {self.model}")
        print(f"For Sale: {self.for_sale}")

obj1 =Car("BMW","Black","X5",False)

obj1.describe()
obj1.drive(18)
print(f"Manufacturing Year: {obj1.manufacture_year}")