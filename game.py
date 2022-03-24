kills=0
class Room:
    def __init__(self, name, north=None, south=None, east=None, west=None, character=None, item=None) -> None:
        self.name = name
        self.description = ''
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.character = character
        self.item = item

    def set_description(self, description):
        self.description = description

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
        self.character = chara

    def set_item(self, item):
        self.item = item

    def get_details(self):
        print(f'{self.name}' + '\n' + '----------------' +'\n'+ f'{self.description}')
        if self.north:
            print(f'The {self.north.name} is north')
        if self.south:
            print(f'The {self.south.name} is south')
        if self.west:
            print(f'The {self.west.name} is west')
        if self.east:
            print(f'The {self.east.name} is east')
    def get_character(self):
        return self.character

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


class Character:
    def __init__(self, name, desc) -> None:
        self.name = name
        self.desc = desc
        self.conversation = ''

    def set_conversation(self, phrase):
        self.conversation = phrase
    
    def describe(self):
        print(f'{self.name} is here')
        print(self.desc)

    def talk(self):
        print(f'[{self.name}] says: {self.conversation}')


class Friend(Character):
    def __init__(self, name, desc) -> None:
        super().__init__(name, desc)




class Enemy(Character):
    def __init__(self, name, desc) -> None:
        super().__init__(name, desc)
        self.weakness = '' 
        

    def set_weakness(self, item):
        self.weakness = item

    def fight(self, item):
        if item == self.weakness:
            global kills
            kills += 1
            return True
        return False

    def get_defeated(self):
        global kills
        return kills


class Item:
    def __init__(self, name) -> None:
        self.name = name
        self.description = ''

    def set_description(self, desc):
        self.description = desc

    def describe(self):
        print(f'the [{self.name}] is here - {self.description}')

    def get_name(self):
        return self.name


# room1 = Room('kitchen')
# room2 = Room('hallway')

# room1.link_room(room2, 'north')
# char = Enemy('dudee', 'meme')
# print(char.set_conversation('lol'))
# print(char.conversation)
