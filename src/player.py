# Write a class to hold player information, e.g. what room they are in
# currently.
# class Items:
#     def __init__(self, name, description):
#         self.name = name
#         self.description = description
#     def __str__(self):
#         return f'{self.name} : {self.description}'

# item = {
# 'one': Items('a','A'),
# 'two': Items('b','B'),
# 'three': Items('c','C'),
# 'four': Items('d','D'),
# 'five': Items('e','E'),
# 'six': Items('f','F'),
# }
# print(item['one'])
# print(type(item))
class Player:
    def __init__(self, name=None, current_room=None, inventory=[]):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory

    def __str__(self):
        return f'Player info: Name: "{self.name}" Current Location: "{self.current_room}" Inventory Bag: "{self.inventory}"'

    # def add_item(self):
    #     # print(f'add_item worked for player', {self.player.inventory})
    #     return self.inventory

    # def drop_item(self):
    #     return self.item.remove()

 
# player = Player('carlitos', 'room', item['two'])
# print(player)
# print(player.name)
# print(player.current_room)
# print(type(player.inventory))
# print(player.add_item(item['three']))
# print(player)

