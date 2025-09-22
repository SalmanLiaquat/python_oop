# Aggregation: one object(the whole) contains references of one or more independent objects

'''
Real-world example:

A University has many Professors.

Professors can exist even if the university is closed.

So, professors are not dependent on the university’s lifetime.


'''

class Professor:
    def __init__(self,name):
        self.name = name
        


class University:
    def __init__(self,name):
        self.name = name
        self.professors = [] # aggregation

    def add_professor(self,professor): # aggregation method
        self.professors.append(professor)
    def list_professors(self):
       
            return [prof.name for prof in self.professors] 
    def remove_professor(self,professor):
        self.professors.remove(professor)


Prof1 = Professor("Ahmed")
Prof2 = Professor("Sayed")
Prof3 = Professor("Ahmed")

university = University("Cairo University")
university.add_professor(Prof1)
university.add_professor(Prof2)
university.add_professor(Prof3)
print(university.name)
print(f"---{university.name} has {len(university.professors)} professors:---")
count =0
for i in university.list_professors():
    count+=1
    print(f"{count}: {i}") #print(i.name)
