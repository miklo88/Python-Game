# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        # self.items = items
     
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

# if currentRoom == room['outside']:
#     return f'youre outside. i should input here.'


# room['outside'].n_to = room['foyer']
# room['foyer'].s_to = room['outside']
# room['foyer'].n_to = room['overlook']
# room['foyer'].e_to = room['narrow']
# room['overlook'].s_to = room['foyer']
# room['narrow'].w_to = room['foyer']
# room['narrow'].n_to = room['treasure']
# room['treasure'].s_to = room['narrow']