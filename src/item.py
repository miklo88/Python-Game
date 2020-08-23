
#  //////////////////ITEM CLASS
class Item:
    def __init__(self, item_name, item_description):
        self.item_name = item_name
        self.item_description = item_description
    
    def __str__(self):
        return f'Item: {self.item_name}, {self.item_description}'

    def on_take(self):
        return f'You have picked up {self.item_name}'
        
    def on_drop(self):
        print(f'You have dropped {self.item_name}')
# item = Item('item_name', 'description of item')  
# print(item)

# print(item.on_take())
# ITEM DATA DICTIONARY
item = {
    'staff': Item('Wizard Staff','When in the right hands it summons the true path'),
    
    'crystal': Item('Gemstone of Eyes','Use it to see into the future'),
    
    'book of summons': Item('Book of Summons','To know all the secrets of time'),
    
    'elven bow': Item('Elven Bow','Lightweight but fires with tremendous power and accuracy'),
    
    'mithril': Item('Mithril','None like it in the world. Will protect you against anything'),

    'watch': Item('Pocket Watch','Being able to know the time always comes in handy')
}