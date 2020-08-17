#  * This will be the _base class_ for specialized item types to be declared
class Item:
    def __init__(self, item_name, item_description):
        self.item_name = item_name
        self.item_description = item_description
    
    def __str__(self):
        return f'A {self.item_name}, {self.item_description}'

    def on_take(self):
        # return item.add({self.item_name})
        print(f'on take worked. {self.item_name}', type({self.item_name}))
        # print(f'You have picked up {self.item_name}')
        
    def on_drop(self):
        print(f'You have dropped {self.item_name}')
# item = Item('item_name', 'description of item')  
# print(item)