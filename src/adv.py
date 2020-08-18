# room class import
from room import Room
# player class import
from player import Player
# item class implort
from item import Item
# Declare all the items
item = {
    'staff': Item('Wizard Staff','When in the right hands it summons the true path'),
    
    'crystal': Item('Gemstone of Eyes','Use it to see into the future'),
    
    'book of summons': Item('Book of Summons','To know all the secrets of time'),
    
    'elven bow': Item('Elven Bow','Lightweight but fires with tremendous power and accuracy'),
    
    'mithril': Item('Mithril','None like it in the world. Will protect you against anything'),

    'watch': Item('Pocket Watch','Being able to know the time always comes in handy')
}

# Declare all the rooms
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

# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
#item assignment to rooms
room['outside'].item = item['staff']
room['foyer'].item = item['crystal']
room['overlook'].item = item['mithril']
room['narrow'].item = item['elven bow']
room['treasure'].item = item['book of summons']

#
# Main
#
instructions = '''Welcome to the adventure game! You will be searching for a lost treasure. Using the keys on your keyboard of n, s, e, w 
you can control with cardinal direction your player travels! Good luck on your journey!'''
print(instructions)

# Make a new player object that is currently in the 'outside' room.
player = Player()
# name = input(f'Enter your name: ')
name = 'Carl'
player.name = name
player.current_room = room['outside']
# print(player.current_room.item)
player.inventory = item['watch']

# print('player.current_room.item', player.current_room.item)
print(player.inventory)
# print(f'////// {player} end player info//////')

# Write a loop that:
while True:
# # * Prints the current room name
    print(f'{player.current_room.name}')
# # * Prints the current description (the textwrap module might be useful here).
    print(f'{player.current_room.description}')
    #prints items in a room if any
    print(f'{player.current_room.item}')
    # print(f'{player.current_room.item.item_name}')
# If the user enters a cardinal direction, attempt to move to the room there.
    direction = input('Move by cardinal direction commands N, S, E or W. You can "grab item" or "drop item": ')
    # Print an error message if the movement isn't allowed.
    if direction == 'n':
        if player.current_room is not None:
            player.current_room = player.current_room.n_to 
    #handle error
    elif direction == 's':
        if player.current_room is not None:
            player.current_room = player.current_room.s_to
    #handle error
    elif direction == 'e':
        if player.current_room is not None:
            player.current_room = player.current_room.e_to
    #handle error
    elif direction == 'w':
        if player.current_room is not None:
            player.current_room = player.current_room.w_to
#handle error
#grabbing an item
    elif direction == 'grab item':
        item_name = player.current_room.item
        print('//// item_name just name ///',item_name)
        # grabbing the item using get item from room class
        item = player.current_room.get_item(item_name)
        print('//// item_name whole item ///',item)
        if item:
            print('/// before on_take()',item)
            # invokes ontake from item class so you know you have it
            item.on_take()
#removing from room
# ### MONDAY NIGHT STOPPING. JUST NEED TO FIGURE OUT HOW TO REMOVE FROM CURRENT ROOM
            # AttributeError: 'Item' object has no attribute 'remove'
            player.current_room.remove_item(item_name)
            #removing from room and adding to players inventory
            player.inventory.append(item_name)
            
        # print('grabbed some stuff')
        else:
            print(f'{item_name} ////// is not here.')
        # if direction == 'grab item':
        
#dropping the item
    elif direction == 'drop item':
        print('drop some stuff')

# If the user enters "q", quit the game.
    elif direction == 'q':
        print(f'Sadly the quest has ended.')
        break
# * Waits for user input and decides what to do.
    else:
        print(f'Wrong way. Try again.')
