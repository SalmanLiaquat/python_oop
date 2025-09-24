# Nested class: A class define withi the another class is called nested class
#    -> class outer
#    -> Class inner

#    BENEFITS:
#         -> allow to group the classes that logically are related to each other
#         -> keep namespace clean , reduce the conflict of naming possibilities
#         -> Encapsulate (priate the details that are not relevant outside the class)


class Company:
    def __init__(self, name):
        self.name = name
        self.employees = []   # Company will manage employees list

    def add_employee(self, name, age):
        emp = self.Employee(name, age)
        self.employees.append(emp)

    def employees_list(self):
        return [emp.name for emp in self.employees]

    # Nested Employee Class
    class Employee:
        def __init__(self, name, age):
            self.name = name
            self.age = age

# ------------------- USAGE -------------------
company = Company("Google")

company.add_employee("Ahmed", 24)
company.add_employee("Salman", 24)
company.add_employee("Liaquat", 24)
print(f"------{company.name}---------")
for emp in company.employees_list():
    print(emp)



