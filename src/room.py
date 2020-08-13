# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        # self.items = items
        self.n_to: Room = None
        self.s_to: Room = None
        self.e_to: Room = None
        self.w_to: Room = None
     
    def __str__(self):
        output = f'You have entered {self.name} : {self.description}'
        if self.n_to:
             output += ' : ' + self.n_to.name + '\n'   
        if self.n_to:
            output += ' : ' + self.n_to.name + '\n'
        if self.n_to:
            output += ' : ' + self.n_to.name + '\n'
        if self.n_to:
            output += ' : ' + self.n_to.name + '\n'

        return output

# Room(name, description, items)

# room = Room('Bano', 'Cono it fucking smells in here papi')
# print(room)
