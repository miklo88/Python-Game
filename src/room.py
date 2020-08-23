# ITEM IMPORT
from item import Item, item
# /////////////ROOM CLASS
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
        return f'Room: {self.name} Room Description: {self.description} Room Items: {self.item}'

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
        return False
# Room(name, description, items) 

# room = Room('room', 'its described as such', 'item')
# print(room)

# ROOM DATA DICTIONARY
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),
# 
    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),
# 
    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),
# 
    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),
#
    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}
#DIRECTIONAL ATTRIBUTES APPLIED TO LINK ROOMS POINT TO
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
#ITEM ASSIGNMENT TO ROOMS
room['outside'].item = item['staff']
room['foyer'].item = item['crystal']
room['overlook'].item = item['mithril']
room['narrow'].item = item['elven bow']
room['treasure'].item = item['book of summons']


    # def __str__(self):
    #     output = f'Room: {self.name} Room Description: {self.description} Room Items: {self.item}'
    #     if self.n_to:
    #          output += self.n_to.name + '\n'
    #     if self.s_to:
    #         output += self.s_to.name + '\n' 
    #     if self.e_to:
    #         output += self.e_to.name + '\n' 
    #     if self.w_to:
    #         output += self.w_to.name + '\n' 
    #     return output