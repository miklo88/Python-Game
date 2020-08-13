# room class import
from room import Room
# player class import
from player import Player
# item class implort
from item import Item
# Declare all the items
item = {
    'staff': Item('Wizard Staff','When in the right hands it summons true path'),
    
    'crystal': Item('Gemstone of Eyes','Use it to see into the future'),
    
    'book of summons': Item('Book of Summons','To know all the secrets of time'),
    
    'elven bow': Item('Elven Bow','Lightweight but fires with tremendous power and accuracy'),
    
    'mithril': Item('Mithril','None like it in the world. Will protect you against anything'),
}
# print(item['staff'])
# print(item['crystal'])
# print(item['book of summons'])
# print(item['elven bow'])
# print(item['mithril'])
# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", item['staff']),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", item['book of summons']),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", item['crystal']),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", item['mithril']),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", item['elven bow']),
}
# print(room['outside'])
# print(room['foyer'])
# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
#
# Main
#
instructions = '''Welcome to the adventure game! You will be searching for a lost treasure. Using the keys on your keyboard of n, s, e, w 
you can control with cardinal direction your player travels! Good luck on your journey!'''
print(instructions)

# Make a new player object that is currently in the 'outside' room.
name = input(f'Enter your name: ')
player = Player(name)
player.current_room = room['outside']
player.item = []
print(player.item)
# Write a loop that:
while True:
# # * Prints the current room name
    print(player.current_room.name)
# # * Prints the current description (the textwrap module might be useful here).
    print(f'{player.current_room.description}')
# If the user enters a cardinal direction, attempt to move to the room there.
    direction = input('Which way we goin? N, S, E or W?: ')    
# Print an error message if the movement isn't allowed.
    if direction == 'n':
        if player.current_room is not None:
            player.current_room = player.current_room.n_to
    elif direction == 's':
        if player.current_room is not None:
            player.current_room = player.current_room.s_to
    elif direction == 'e':
        if player.current_room is not None:
            player.current_room = player.current_room.e_to
    elif direction == 'w':
        if player.current_room is not None:
            player.current_room = player.current_room.w_to
# If the user enters "q", quit the game.
    elif direction == 'q':
        print(f'Sadly the quest has ended.')
        break
# * Waits for user input and decides what to do.
    else:
        print(f'Wrong way. Try again.')
