#Composition

#-👉 Composition is a strong "owns-a" relationship.
#-It means one class owns another class, and the part cannot exist without the whole.
#-The lifetime of the part depends entirely on the whole.
#-If the container is destroyed, all its parts are also destroyed.
#✅ Real-world example:
#->A House has Rooms.
#->Rooms cannot exist independently of a house.
#->If the house is destroyed, the rooms are destroyed too.


class Room:
    def __init__(self, room_type):
        self.room_type = room_type

class House:
    def __init__(self, name):
        self.name = name
        self.rooms = [Room("bedroom"), Room("bathroom"), Room("kitchen")]

    

    def list_rooms(self):
         return [ f"{self.name} has a {room.room_type} rooms." for room in self.rooms] 



house =House("Salman House")


for i in house.list_rooms():
    print(i)
