# Abstract classes: -> a class that can be instantiated by its own and it meant to be to subclass
# it can abstract methods which are decleare but have no implementation
# Benefits:
#  -> Prevent instiantiation
#  -> requiree children classes to implement abstract methods
'''
You use abstract classes when you don't want to create an object of the parent class. 
An abstract class acts as a blueprint that can only be inherited by other classes. 
You cannot directly instantiate an object from an abstract class.

An abstract method is a method declared inside an abstract class without any implementation. 
It forces any child class that inherits from the abstract class to provide its own, specific 
implementation for that method
'''

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        print("Woof woof!")


class Cat(Animal):
    def make_sound(self):
        print("Meow meow!")


obj =[Dog(),Cat()]
for animal in obj:
    animal.make_sound()