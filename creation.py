import character
import zones
import manual

title = "Character Creation"

description = """
Not all adventurers are the same. Please choose a class from the options below.
At any time during the game, enter 'm' to access the user manual.
"""

options = """
1 - Warrior. Tackle problems head on. Often literally. (Main stat: Strength)
2 - Wizard. Use your knowledge to outwit foes and cast magic spells. (Main stat: Intelligence)
3 - Rogue. Use your charm and skill to try and weasel your way through life. (Main stat: Dexterity)
"""

def create_character():
    print(title)
    print("\n\n\n")
    print(description)
    print("\n\n\n")
    print(options)

    user_input = input()
    while (user_input != '1' and user_input != '2' and user_input != '3' and user_input != 'm'):
        print('Please select from the available options:')
        user_input = input()
    if user_input == '1':
        #create warrior
        playerCharacter = character.Warrior(12, 16, 3, 2, 0, -1, 1, 1, 1, 1)
    elif user_input == '2':
        #create wizard
        playerCharacter = character.Wizard(7, 12, -1, 1, 1, 3, 2, 0, 1, 2)
    elif user_input == '3':
        #create rogue
        playerCharacter = character.Rogue(9, 14, 0, 1, 3, 1, -1, 2, 1, False)
    elif user_input == 'm':
        #view manual
        manual.print_manual()
        create_character()
    else:
        print('problem with creating character')
        quit()


    print('Your character:')
    print('Max HP:', playerCharacter.get_hit_points())
    print('Current HP:', playerCharacter.get_current_hp())
    print('AC:', playerCharacter.get_armor_class())
    print('Str:', playerCharacter.get_strength())
    print('Con:', playerCharacter.get_constitution())
    print('Dex:', playerCharacter.get_dexterity())
    print('Int:', playerCharacter.get_intelligence())
    print('Wis:', playerCharacter.get_wisdom())
    print('Cha:', playerCharacter.get_charisma())

    #start the game!
    zones.arrival(playerCharacter)