"""Roguelike game"""
kills = 0


class Room:
    """Room class"""
    def __init__(self, name, north=None, south=None, east=None, west=None, character=None, item=None) -> None:
        """Creates the class instance"""
        self.name = name
        self.description = ''
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.character = character
        self.item = item
        self.rooms=[]

    def set_description(self, description):
        """Describes the room"""
        self.description = description

    def link_room(self, other, direction):
        """Links rooms"""
        if direction == 'north':
            self.north = other
            self.rooms.append('north')
        elif direction == 'south':
            self.south = other
            self.rooms.append('south')
        elif direction == 'west':
            self.west = other
            self.rooms.append('west')
        elif direction == 'east':
            self.east = other
            self.rooms.append('east')

    def set_character(self, chara):
        """Sets the character in the room"""
        self.character = chara

    def set_item(self, item):
        """Sets the item in the room"""
        self.item = item

    def get_details(self):
        """Prints details about the room"""
        print(f'{self.name}' + '\n' + '--------------------' +
              '\n' + f'{self.description}')
        if self.north:
            print(f'The {self.north.name} is north')
        if self.south:
            print(f'The {self.south.name} is south')
        if self.west:
            print(f'The {self.west.name} is west')
        if self.east:
            print(f'The {self.east.name} is east')

    def get_character(self):
        """Returns the character in the room"""
        return self.character

    def get_item(self):
        """Return the items in the rooms"""
        return self.item

    def move(self, command):
        """Moves between the rooms"""
        if command == 'north':
            return self.north
        elif command == 'south':
            return self.south
        elif command == 'west':
            return self.west
        elif command == 'east':
            return self.east


class Character:
    """Character class of the game"""
    def __init__(self, name, desc) -> None:
        """Creates a class instance"""
        self.name = name
        self.desc = desc
        self.conversation = ''

    def set_conversation(self, phrase):
        """Sets the phrase which character will say"""
        self.conversation = phrase

    def describe(self):
        """Describes the character"""
        print(f'{self.name} is here')
        print(self.desc)

    def talk(self):
        """Talk with character"""
        print(f'[{self.name}] says: {self.conversation}')


class Friend(Character):
    """Ally class inherited from character"""
    pass


class Enemy(Character):
    """Enemy class inherited from character class"""
    def __init__(self, name, desc) -> None:
        """Creates a class instance"""
        super().__init__(name, desc)
        self.weakness = ''

    def set_weakness(self, item):
        """Sets the weakness item which will defeat the enemy"""
        self.weakness = item

    def fight(self, item):
        """Fight loop"""
        if item == self.weakness:
            global kills
            kills += 1
            return True
        return False

    def get_defeated(self):
        """Returns number of defeated enemies"""
        global kills
        return kills


class Item:
    """Items that player fights with"""
    def __init__(self, name) -> None:
        """Creates class instance"""
        self.name = name
        self.description = ''

    def set_description(self, desc):
        """sets the description of item"""
        self.description = desc

    def describe(self):
        """prints the description"""
        print(f'the [{self.name}] is here - {self.description}')

    def get_name(self):
        """return the item name"""
        return self.name
