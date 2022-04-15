"""Lviv Roguelike game"""


class Street:
    """Street class"""

    def __init__(self, name, north=None, south=None, east=None, west=None, character=None, item=None) -> None:
        """Creates an instance of a class"""
        self.name = name
        self.description = ''
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.character = character
        self.item = item
        self.streets = []

    def set_description(self, description):
        """Describes the street"""
        self.description = description

    def link_street(self, other, direction):
        """Links streets"""
        if direction == 'north':
            self.north = other
            self.streets.append('north')
        elif direction == 'south':
            self.south = other
            self.streets.append('south')
        elif direction == 'west':
            self.west = other
            self.streets.append('west')
        elif direction == 'east':
            self.east = other
            self.streets.append('east')

    def set_character(self, chara):
        """Sets the character on the street"""
        self.character = chara

    def set_item(self, item):
        """Sets the item on the street"""
        self.item = item

    def get_details(self):
        """Prints details about the street"""
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
        """Returns character instance which is on this street"""
        return self.character

    def get_item(self):
        """Return item instance which is on this street"""
        return self.item

    def move(self, command):
        """Moves between the streets"""
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

    def __init__(self, name, desc) -> None:
        """Creates a class instance"""
        super().__init__(name, desc)
        self.buff = ''
        self.buff_desc = ''

    def set_amplifier(self, buff, b_desc):
        """Sets the help that this ally will do"""
        self.buff = buff
        self.buff_desc = b_desc

    def give_amplify_to_player(self):
        """Returns the amplify"""
        return self.buff


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
            return True
        return False


class Boss(Enemy):
    """Strong enemy class"""

    def __init__(self, name, desc) -> None:
        """Creates a class instance"""
        super().__init__(name, desc)
        self.power = ''

    def set_power(self, power):
        """Sets the super power of the boss"""
        self.power = power

    def fight(self, item):
        """fights with boss"""
        if item in self.weakness:
            self.weakness.remove(item)
            return True
        return False


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
