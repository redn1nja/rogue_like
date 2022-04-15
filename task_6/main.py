import game

kozelnytska = game.Street('Kozelnytska street')
kozelnytska.set_description('The street where the UCU is')

stryiska = game.Street('Stryiska street')
stryiska.set_description(
    '''The street which leads to the most popular place among students - Sil'po''')

franka = game.Street('Franka Street')
franka.set_description(
    'Old historical street with lots of museeums... and lazy people.')
shevckenka = game.Street('Shevchenka street')
shevckenka.set_description(
    'Life is blossoming here - lots of people, lots of cafes, lots of danger')

krakivska = game.Street('Krakivska street')
krakivska.set_description(
    '''Called after city, which is in other country, Krakivska is a street\
 where you definately don't want to go except you are brave and strong and smart''')

kozelnytska.link_street(stryiska, 'west')
stryiska.link_street(kozelnytska, 'east')
kozelnytska.link_street(franka, 'north')
franka.link_street(kozelnytska, 'south')
franka.link_street(stryiska, 'west')
stryiska.link_street(franka, 'north')
stryiska.link_street(shevckenka, 'west')
shevckenka.link_street(stryiska, 'east')
shevckenka.link_street(krakivska, 'north')
krakivska.link_street(shevckenka, 'east')


cavalier = game.Friend(
    'Cavalier', 'A young man looking for adventures and love.')
cavalier.set_conversation('''You're welcomed here, fellow knight!''')
cavalier.set_amplifier(
    'Strength', 'You have a chance to survive a lost fight for once.')
franka.set_character(cavalier)

student = game.Friend('Student', 'A fellow seeker of knowledge.')
student.set_conversation(
    'I need to finish this task ASAP, or i going to be expelled from here.')
student.set_amplifier(
    'Intellect', '''You may receive information about enemy's weakness for once''')
kozelnytska.set_character(student)

laydak = game.Enemy('Laydak', 'Well, he is so lazy that he does nothing')
laydak.set_conversation('Just let me some sleep...')
laydak.set_weakness('book')
stryiska.set_character(laydak)

lotr = game.Enemy(
    'Lotr', 'Not that LotR you may have thought, but a cruel bandit that wants your soul or money')
lotr.set_conversation('Give your wallet here, boy!')
lotr.set_weakness('wallet')
shevckenka.set_character(lotr)

batyar = game.Boss(
    'Batyar', 'An rogue who creates a real threat to the whole city')
batyar.set_conversation('Lvivski Batyary tsila nasha rodyna...')
batyar.set_weakness(['guitar', 'swiss_knife'])
batyar.set_power('You need two items to defeat this boss')
krakivska.set_character(batyar)

guitar = game.Item('guitar')
guitar.set_description('A cool guitar left in one of the UCU basements.')
kozelnytska.set_item(guitar)

swiss_knife = game.Item('swiss_knife')
swiss_knife.set_description('A knife bought in Silpo')
stryiska.set_item(swiss_knife)

book = game.Item('book')
book.set_description('A book about how to get a job')
shevckenka.set_item(book)

wallet = game.Item('wallet')
wallet.set_description('A found wallet on the floor')
franka.set_item(wallet)

current_room = kozelnytska
backpack = []


dead = False
res = 'Strength'
while dead == False:

    print("\n")
    current_room.get_details()

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    item = current_room.get_item()
    if item is not None:
        item.describe()

    command = input("> ")

    if command in current_room.streets:
        # Move in the given direction
        current_room = current_room.move(command)
    elif command == "talk":
        # Talk to the inhabitant - check whether there is one!
        if inhabitant is not None:
            inhabitant.talk()
        if isinstance(inhabitant, game.Friend):
            print(f'You get a {inhabitant.buff}')
            backpack.append(inhabitant.give_amplify_to_player())
    elif command == "fight":
        if inhabitant is not None:
            if isinstance(inhabitant, game.Enemy):
                # Fight with the inhabitant, if there is one
                print("What will you fight with?")
                fight_with = input()
                # Do I have this item?
                if fight_with in backpack:
                    if isinstance(inhabitant, game.Boss):
                        if inhabitant.fight(fight_with):
                            if inhabitant.weakness != []:
                                # What happens if you win?
                                print("You reduced one health from a boss")
                            elif inhabitant.weakness == []:
                                current_room.character = None
                                print(
                                    "Congratulations, you have vanquished the enemy and got to Krakivska street!")
                                dead = True
                        else:
                            # What happens if you lose?
                            print("Oh dear, you lost the fight.")
                            if res not in backpack:
                                dead = True
                                print("That's the end of the game")
                            else:
                                print(
                                    'you have been saved by strength given by Cavalier!')

                    else:
                        if inhabitant.fight(fight_with) == True:
                            # What happens if you win?
                            print("Hooray, you won the fight!")
                            current_room.character = None
                        else:
                            # What happens if you lose?
                            print("Oh dear, you lost the fight.")

                            if res not in backpack:
                                dead = True
                                print("That's the end of the game")
                            else:
                                print(
                                    'you have been saved by strength given by Cavalier!')
                                backpack.remove(res)
                else:
                    print("You don't have a " + fight_with)
        else:
            print("There is no one here to fight with")
    elif command == "take":
        if item is not None:
            if inhabitant is None or isinstance(inhabitant, game.Friend):
                print("You put the " + item.get_name() + " in your backpack")
                backpack.append(item.get_name())
                current_room.set_item(None)
            else:
                print('defeat enemy first!')
        else:
            print("There's nothing here to take!")
    elif command == 'Intellect':
        if 'Intellect' in backpack and inhabitant is not None:
            if isinstance(inhabitant.weakness, str):
                print(inhabitant.weakness)
                backpack.remove('Intellect')
            else:
                print(*inhabitant.weakness)
                backpack.remove('Intellect')
        else:
            print('You dont have this power just yet!')
    else:
        print("I don't know how to " + command)
