
# Implement a class to hold room information. This should have name and
# description attributes.
class Room():
    def __init__(self, name, description, item=[]):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.item = item

    def __str__(self):
        output = f'{self.name} : {self.description} : {self.item}'
        if self.n_to:
             output += ' To the north' + self.n_to.name + '\n' + self.item.item_name + '\n'
        if self.s_to:
            output += ' To the south ' + self.s_to.name + '\n' + self.item.item_name + '\n'
        if self.e_to:
            output += ' To the east ' + self.e_to.name + '\n' + self.item.item_name + '\n'
        if self.w_to:
            output += ' To the west ' + self.w_to.name + '\n' + self.item.item_name + '\n'
        
        return output

    # def add_item(self):
    #     return item.append()

    # def remove_item(self):
    #     return item.remove()

# Room(name, description, items) 

# room = Room('room', 'its described as such', 'item')
# print(room)
