# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name=None, current_room=None, item=[]):
        self.name = name
        self.current_room = current_room
        self.item = item

    def __str__(self):
        return f'Player info: {self.name} : {self.current_room} : {self.item}'

    def add_item(self):
        return self.item.append()

    def drop_item(self):
        return self.item.remove()


# player = Player('carlitos', 'room', [])
# print(player)
# print(player.name)
# print(player.current_room)
# print(player.item)
