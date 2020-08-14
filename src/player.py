# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room=None, player_item=[]):
        self.name = name
        self.current_room = current_room
        self.player_item = player_item

    def __str__(self):
        return f'Player info: {self.name} : {self.current_room} : {self.player_item}'

    def add_item(self):
        return self.player_item.append()

    def drop_item(self):
        return self.player_item.remove()


# player = Player('carlitos', 'room', [])
# print(player)
# print(player.name)
# print(player.current_room)
# print(player.item)
