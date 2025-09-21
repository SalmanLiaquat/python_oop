#polymorphism->same name having many different form
#Method Overriding
'''
class Factory:
    def __init__(self,material,zips):
        self.material = material
        self.zips = zips
    def show(self):
        print(f"Material: {self.material}")
        print(f"Zips: {self.zips}")


class Car(Factory):
    def __init__(self,material,zips,engine):
        super().__init__(material,zips)
        self.engine = engine

    def show(self):
        print(f"Material: {self.material}")
        print(f"Zips: {self.zips}")
        print(f"Engine: {self.engine}")


class Bike(Car):
    def __init__(self,material,zips,engine,wheels):
        super().__init__(material,engine,zips)
        self.wheels = wheels

    def show(self):
        print(f"Material: {self.material}")
        print(f"Zips: {self.zips}")
        print(f"Engine: {self.engine}")
        print(f"Wheels: {self.wheels}")


obj=Bike("Metal","Zips","Engine","Wheels")
obj.show()


'''
# Duck Typing:Another way to achieve polymorphism beside inheritance-> is duck typing. Object must have minimum and necessary attributes/methods

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("Woof woof!")

class Cat(Animal):
    def speak(self):
        print("Meow meow!")

class Car:
    alive=False
    def speak(self):
        print("Vroom vroom!")


animal = Cat()
animal.speak()
'''
animals =[Dog(),Cat(),Car()]
for animal in animals:
    animal.speak()
    animal.alive

'''