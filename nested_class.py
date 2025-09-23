# Nested class: A class define withi the another class is called nested class
#    -> class outer
#    -> Class inner

#    BENEFITS:
#         -> allow to group the classes that logically are related to each other
#         -> keep namespace clean , reduce the conflict of naming possibilities
#         -> Encapsulate (priate the details that are not relevant outside the class)


class Company:
    def __init__(self,name):
        self.name = name
    class Employee:
       def __init__(self,name,age):
           self.name = name
           self.age = age

    
company=Company("Google")
emp1=company.Employee("Ahmed",24)
print(company.name)
print(f"Name: {emp1.name} Age: {emp1.age}") #print(emp1.name)






