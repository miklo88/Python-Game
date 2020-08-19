from item import Item
# Implement a class to hold room information. This should have name and
# # description attributes.
class Room():
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.item = []

    def __str__(self):
        output = f'{self.name} : {self.description} : {self.item}'
        if self.n_to:
             output += self.n_to.name + '\n'            
        if self.s_to:
            output += self.s_to.name + '\n' 
        if self.e_to:
            output += self.e_to.name + '\n' 
        if self.w_to:
            output += self.w_to.name + '\n' 
        return output
# looping and grabbing items
    def get_item(self, item_name: str):
        for item in self.item.item_name:
            print('/// loop_name', self.item.item_name)
            if self.item.item_name == self.item.item_name:
                return self.item
        return False
        #removing item from current room
    def remove_item(self, item_name: str):
        print('/// remove_item func.')
        if self.item.item_name == self.item.item_name:
            # print('/// checking if condition worked', item_name)
            return self.item.remove()
# Room(name, description, items) 

# room = Room('room', 'its described as such', 'item')
# print(room)
