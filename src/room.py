# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f'You have entered {self.name} and it is {self.description}'

# Room(name, description)

# room = Room('Bano', 'Cono it fucking smells in here papi')
# print(room)
