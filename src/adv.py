# room class import
from room import Room
# print(Room)
# player class import
from player import Player
# print(Player)
# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

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
#
# Main
#
instructions = 'Need to write out some instructions'
print(instructions)

# Make a new player object that is currently in the 'outside' room.
name = input(f'Enter your name: ')
player = Player(name)
player.currentRoom = room['outside']
player.items = ['inventory']

# print(player.currentRoom)

# Write a loop that:
while True:
# # * Prints the current room name
    print(player.currentRoom.name)
# # * Prints the current description (the textwrap module might be useful here).
    print(f'The current room {player.currentRoom.description}')
# If the user enters a cardinal direction, attempt to move to the room there.
    direction = input('Which way we goin? N, S, E or W?: ')    
# Print an error message if the movement isn't allowed.
    if direction == 'n':
        if player.currentRoom is not None:
            player.currentRoom = player.currentRoom.n_to
    elif direction == 's':
        if player.currentRoom is not None:
            player.currentRoom = player.currentRoom.s_to
    elif direction == 'e':
        if player.currentRoom is not None:
            player.currentRoom = player.currentRoom.e_to
    elif direction == 'w':
        if player.currentRoom is not None:
            player.currentRoom = player.currentRoom.w_to
# If the user enters "q", quit the game.
    elif direction == 'q':
        print(f'Sadly the quest has ended.')
        break
# * Waits for user input and decides what to do.
    else:
        print(f'Wrong way. Try again.')
