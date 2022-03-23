class Room:
    def __init__(self, name, north=None, south=None, east=None, west=None, character=None, item=None) -> None:
        self.name=name
        self.description=''
        self.north=north
        self.south=south
        self.east=east
        self.west=west
        self.character=character
        self.item=item
        

    def set_description(self, description):
        self.description=description

    def link_room(self, other, direction):
        if direction == 'north':
            self.north = other
        elif direction == 'south':
            self.south = other
        elif direction == 'west':
            self.west = other
        elif direction == 'east':
            self.east = other

    def set_character(self, chara):
        self.character=chara

    def set_item(self, item):
        self.item=item
    
    def get_details(self):
        return f'room {self.name}' + '\n' + f'{self.description}' + '\n'

    def get_character(self):
        char=Character(self.name)
        return char 

    def get_item(self):
        return self.item

    def move(self, command):
        if command == 'north':
            return self.north
        elif command == 'south':
            return self.south
        elif command == 'west':
            return self.west
        elif command == 'east':
            return self.east
        

class Character(Room):
    def __init__(self, name, north=None, south=None, east=None, west=None, character=None, item=None) -> None:
        super().__init__(name, north, south, east, west, character, item)
    
    def talk(self):
        return self.north


class Enemy:
    def __init__(self, name, desc) -> None:
        self.name=name
        self.desc=desc
        self.conversation=''
        self.weakness=''

    def set_conversation(self, phrase):
        self.conversation=phrase
    
    def set_weakness(self, item):
        self.weakness=item

class Item:
    def __init__(self, name) -> None:
        self.name=name
        self.description=''

    def set_description(self, desc):
        self.description=desc
    
    def describe(self):
        return self.description

room1=Room('kitchen')
room2=Room('hallway')

room1.link_room(room2, 'north')
char=room1.get_character()
print(char.talk())
