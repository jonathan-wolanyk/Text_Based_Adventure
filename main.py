# Jonathan Wolanyk

# using time module so that users can read ending before closing
import time

# information that is produced at the start and if player asks for help
def show_instructions():
   print('-------------------------------')
   print("Lair of the Mad God Adventure Game")
   print("Collect 6 items to win the game, or be destroyed by Archon, the Mad God.")
   print("Move commands: north, south, east, west")
   print("Add to Inventory: get 'item name' - capitalization matters!")
   print('-------------------------------')


# core game
def main():

    # initialization information
    location = 'The Grand Theater'
    dungeon_complete = 0
    inventory = []
    rooms = {
        'The Grand Theater': {'south': 'The Ice Room', 'north': 'The Snake Pit', 'west': 'The Spider Room', 'east':
                              'The Mad Laboratory', 'item': 'doors on every side of you and wonder where to go.'},
        'The Ice Room': {'north': 'The Grand Theater', 'east': 'The Garden', 'item': 'Blazing Longsword'},
        'The Snake Pit': {'east': 'The Sunken Corridor', 'south': 'The Grand Theater', 'item': 'Invisibility Cloak'},
        'The Spider Room': {'east': 'The Grand Theater', 'item': 'Webbed Legguards'},
        'The Sunken Corridor': {'west': 'The Snake Pit', 'item': 'Shield of Hope'},
        'The Mad Laboratory': {'west': 'The Grand Theater', 'north': 'The Lava Room', 'item': 'Chestplate of Wrath'},
        'The Garden': {'west': 'The Ice Room', 'item': 'Lionheart Helm'},
        'The Lava Room': {'south': 'The Mad Laboratory'}}

    # status updates location and inventory
    def status():
        print('You are in the {}'.format(location))
        print('Inventory: {}'.format(inventory))
        print('-------------------------------')

    # while loop keeps game running indefinitely:
    while dungeon_complete != 1:

        # status update and input for movement
        status()
        direction = input('Please enter your move: ')

        # Checking for valid input for movement
        if direction in rooms[location].keys():
            if location != 'The Mad Laboratory' or (location == 'The Mad Laboratory' and direction != 'north'):
                location = rooms[location][direction]

            # If user goes into boss room with 6 items, they win. Less than 6, they lose.
            elif location == 'The Mad Laboratory' and direction == 'north':
                if len(inventory) >= 6:
                    print("Archon, the Mad God can't believe his eyes! An adventurer as strong as he? It's not\n"
                          "possible! He immediately rushes to your location, but you cloak yourself and dash out of \n"
                          "the way. You defeat him with your Blazing Longsword to end his reign of tyranny once\n"
                          "and for all.\n"
                          "Thank you for playing!\n"
                          "Closing in 30 seconds... ")
                    time.sleep(30)
                    exit()
                elif len(inventory) < 6:
                    print("Archon, the Mad God spots you immediately and laughs at the difference in strength between\n"
                          "you and him. He immediately rushes to your location and grabs you, lifting you into \n"
                          "the air with ease. He throws you out of his castle and tells you to return when you\n"
                          "can pose a real threat to him; he loves a good fight, after all!\n"
                          "You may have lost this time, but you can always try again! Thanks for playing.\n"
                          "Closing in 30 seconds... ")
                    time.sleep(30)
                    exit()

            # Printing the room's item if it is not been collected
            # Otherwise, reminding player they have been to this area
            if 'item' in rooms[location]:
                if rooms[location]['item'] in inventory:
                    print('This place seems familiar... ')
                else:
                    print('You see the {}'.format(rooms[location]['item']))

        # Allowing player to collect item if it exists in the room
        # If player attempts to pick up an item twice, reminder sent that it has been collected already
        elif 'get ' in direction and rooms[location]['item'] != 'doors on every side of you and wonder where to go.':
            if direction.strip('get ') in rooms[location]['item']:
                if direction.strip('get ') in rooms[location]['item'] and direction.strip('get ') in inventory:
                    print('You already have that item!')
                elif direction.strip('get ') in rooms[location]['item']:
                    inventory.append(rooms[location]['item'])
                    print('You equip the {} and immediately feel stronger. '
                          'You now have {}/6 items.'.format(rooms[location]['item'], len(inventory)))
            else:
                print('Invalid command!')
                print('You see the {}'.format(rooms[location]['item']))

        # Allowing for exit and help commands
        elif direction == 'exit':
            exit('Thank you for playing!')
        elif direction == 'help':
            show_instructions()

        # Catch all statement for invalid commands
        # Reminds player if an item is in the room after an invalid input
        else:
            print('Invalid command!')
            if 'item' in rooms[location]:
                if rooms[location]['item'] in inventory:
                    continue
                else:
                    print('You see the {}'.format(rooms[location]['item']))

# Main game loop
show_instructions()
main()




