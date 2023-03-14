import manual
import character
from diceRoll import rollDice

def arrival(playerCharacter):
    print("""
    You arrive at the frontier town of Valleywood.
    Many aspiring adventures have made their starts here, and
    jobs of all sorts can be found at the job board in the
    Town Hall or by hearing recent rumors from the local
    townsfolk.
    There is a well-supplied General Store you may find useful
    as well as a local Inn known for its hearty meals.
    """)

    print("\n\n\n")

    print("""
    1 - Go to the Inn
    2 - Go to the Town Hall
    3 - Go to the General Store
    """)

    user_input = input()
    while (user_input != '1' and user_input != '2' and user_input != '3' and user_input != 'm'):
        print('Please select from the available options:')
        user_input = input()

    if user_input == '1':
        #Go to the Inn
        inn(playerCharacter)
    elif user_input == '2':
        #Go to the Town Hall
        townHall(playerCharacter)
    elif user_input == '3':
        #Go to the Store
        generalStore(playerCharacter)
    elif user_input == 'm':
        manual.print_manual()
        arrival(playerCharacter)
    else:
        print('problem with input in arrival')
        quit()

def inn(playerCharacter):
    print("""
    You enter the common room of the Valleywood Inn.
    The innkeeper is happy to let you stay in one of the rooms for a small fee.
    He also lets you know that recently some barrels of ale have gone missing from the basement
    if you are willing to investigate.
    """)

    print("\n\n\n")

    print("""
    1 - Rest at the Inn
    2 - Go to the basement
    3 - Go to the Town Hall
    4 - Go to the General Store
    5 - Leave town
    """)

    user_input = input()
    while (user_input != '1' and user_input != '2' and user_input != '3' and user_input != '4' and user_input != '5' and user_input != 'm'):
        print('Please select from the available options:')
        user_input = input()

    if user_input == '1':
        print('You rest at the Inn and wake up to a brand new day with your body feeling restored.')
        playerCharacter.set_current_hp(playerCharacter.get_hit_points())
        inn(playerCharacter)
    elif user_input == '2':
        print('You walk down the stairs to the basement.')
        basement(playerCharacter)
    elif user_input == '3':
        print('You exit the inn and head to the Town Hall.')
        townHall(playerCharacter)
    elif user_input == '4':
        print('You exit the inn and head to the General Store.')
        generalStore(playerCharacter)
    elif user_input == '5':
        print('You exit the inn and head to the outskirts of town.')
        outskirts(playerCharacter)
    elif user_input == 'm':
        manual.print_manual()
        inn(playerCharacter)
    else:
        print('problem with input')
        quit()

def townHall(playerCharacter):
    print("""
    The town hall is a large building that doesn't seem too busy.
    There is a notice board listing a reward for information or the retreival of
    a shipment of general goods that is long overdue. Most recent information
    refers to an abandoned wagon outside of town.
    """)

    print("\n\n\n")

    print("""
    1 - Leave town
    2 - Go to the inn
    3 - Go to the general store
    """)

    user_input = input()
    while (user_input != '1' and user_input != '2' and user_input != '3' and user_input != 'm'):
        print('Please select from the available options:')
        user_input = input()

    if user_input == '1':
        print('You exit the Town Hall and head to the ouskirts of town.')
        outskirts(playerCharacter)
    elif user_input == '2':
        print('You exit the Town Hall and head to the inn.')
        inn(playerCharacter)
    elif user_input == '3':
        print('You exit the Town Hall and head to the General Store')
        generalStore(playerCharacter)
    elif user_input == 'm':
        manual.print_manual()
        townHall(playerCharacter)
    else:
        print('problem with input')
        quit()

def generalStore(playerCharacter):
    print("""
    You enter the general store.
    This is where you would be able to buy items if the developer
    had implemented a money/item/inventory system.
    Maybe one day.
    """)

    print("\n\n\n")

    print("""
    1 - Go to the inn
    2 - Go to the Town Hall
    3 - Leave town
    """)

    user_input = input()
    while (user_input != '1' and user_input != '2' and user_input != '3' and user_input != 'm'):
        print('Please select from the available options:')
        user_input = input()

    if user_input == '1':
        print('You exit the store and head to the inn.')
        inn(playerCharacter)
    elif user_input == '2':
        print('You exit the store and head to the Town Hall.')
        townHall(playerCharacter)
    elif user_input == '3':
        print('You exit the store and head to the outskirts of town.')
        outskirts(playerCharacter)
    elif user_input == 'm':
        manual.print_manual()
        generalStore(playerCharacter)
    else:
        print('problem with input')
        quit()

def basement(playerCharacter):
    print("""
    You enter the basement and catch a small kobold trying to drag a
    barrel of ale through a hole in the wall and into a small tunnel!
    """)

    print("\n\n\n")

    print("""
    1 - Fight!
    2 - Try to convince the kobold to leave the ale.
    3 - Not your problem. Head back upstairs.
    """)

    Kobold = character.Monster(5, 12, -2, -1, 2, -1, -2, -1, "Kobold")

    user_input = input()
    while (user_input != '1' and user_input != '2' and user_input != '3' and user_input != 'm'):
        print('Please select from the available options:')
        user_input = input()

    if user_input == '1':
        print("You attack the kobold!")
        #fight method here with playerCharacter and Kobold
        fight(playerCharacter, Kobold)
        print("After defeating the kobold you return upstairs and inform the inkeeper of what happened.")
        inn(playerCharacter)
    elif user_input == '2':
        dc = 15
        playerRoll = rollDice('1d20') + playerCharacter.get_charisma()
        if playerRoll >= dc:
            print("The kobold drops the all and scurries off into his tunnel. You head back upstairs to tell the inkeeper what happened.")
            inn(playerCharacter)
        else:
            print("The kobold ignores your attempts at rehabilitation.")
            basement(playerCharacter)
    elif user_input == '3':
        print("You head back up the stairs to the common room.")
        inn(playerCharacter)
    elif user_input == 'm':
        manual.print_manual()
        basement(playerCharacter)
    else:
        print('problem with input')
        quit()

def outskirts(playerCharacter):
    print("""
    You approach the outskirts of town.
    Behind you, you can see the small outlines of the village inn, Town Hall, and General Store.
    Ahead of you, you notice an abandoned wagon in the distance.
    """)

    print("\n\n\n")

    print("""
    1 - Go to the inn
    2 - Go to the Town Hall
    3 - Go to the General Store
    4 - (Future content) Go to the abandoned wagon
    """)

    user_input = input()
    while (user_input != '1' and user_input != '2' and user_input != '3' and user_input != '4' and user_input != 'm'):
        print('Please select from the available options:')
        user_input = input()

    if user_input == '1':
        inn(playerCharacter)
    elif user_input == '2':
        townHall(playerCharacter)
    elif user_input == '3':
        generalStore(playerCharacter)
    elif user_input == '4':
        print('You have reached the end of the demo! Thanks for playing.')
    elif user_input == 'm':
        manual.print_manual()
        arrival(playerCharacter)
    else:
        print('problem with input')
        quit()

def wagon(playerCharacter):
    print("""
    Description Here
    """)

    print("\n\n\n")

    print("""
    1 - 
    2 - 
    3 - 
    """)

    user_input = input()
    while (user_input != '1' and user_input != '2' and user_input != '3' and user_input != 'm'):
        print('Please select from the available options:')
        user_input = input()

    if user_input == '1':
        pass
    elif user_input == '2':
        pass
    elif user_input == '3':
        pass
    elif user_input == 'm':
        manual.print_manual()
        arrival(playerCharacter)
    else:
        print('problem with input')
        quit()

def woods(playerCharacter):
    print("""
    Description Here
    """)

    print("\n\n\n")

    print("""
    1 - 
    2 - 
    3 - 
    """)

    user_input = input()
    while (user_input != '1' and user_input != '2' and user_input != '3' and user_input != 'm'):
        print('Please select from the available options:')
        user_input = input()

    if user_input == '1':
        pass
    elif user_input == '2':
        pass
    elif user_input == '3':
        pass
    elif user_input == 'm':
        manual.print_manual()
        arrival(playerCharacter)
    else:
        print('problem with input')
        quit()

def cave(playerCharacter):
    print("""
    Description Here
    """)

    print("\n\n\n")

    print("""
    1 - 
    2 - 
    3 - 
    """)

    user_input = input()
    while (user_input != '1' and user_input != '2' and user_input != '3' and user_input != 'm'):
        print('Please select from the available options:')
        user_input = input()

    if user_input == '1':
        pass
    elif user_input == '2':
        pass
    elif user_input == '3':
        pass
    elif user_input == 'm':
        manual.print_manual()
        arrival(playerCharacter)
    else:
        print('problem with input')
        quit()

def lair(playerCharacter):
    print("""
    Description Here
    """)

    print("\n\n\n")

    print("""
    1 - 
    2 - 
    3 - 
    """)

    user_input = input()
    while (user_input != '1' and user_input != '2' and user_input != '3' and user_input != 'm'):
        print('Please select from the available options:')
        user_input = input()

    if user_input == '1':
        pass
    elif user_input == '2':
        pass
    elif user_input == '3':
        pass
    elif user_input == 'm':
        manual.print_manual()
        arrival(playerCharacter)
    else:
        print('problem with input')
        quit()

def fight(playerCharacter, enemyCharacter):
    playerInitiative = rollDice('1d20') + playerCharacter.get_dexterity()
    enemyInitiative = rollDice('1d20') + enemyCharacter.get_dexterity()

    if enemyInitiative > playerInitiative:
        #extra initial enemy attack
        print('The ', enemyCharacter.get_name(), ' attacks!')
        attackRoll = rollDice('1d20') + 4
        if attackRoll >= playerCharacter.get_armor_class():
            #attack hits
            damageRoll = rollDice('1d4') + 2
            print('You take ', damageRoll, ' damage!')
            playerCharacter.set_current_hp(playerCharacter.get_current_hp() - damageRoll)
        else:
            #attack misses
            print('The attack misses!')
        print('You have ', playerCharacter.get_current_hp(), ' hit points remaining.')

    while (playerCharacter.get_current_hp() > 0 and enemyCharacter.get_current_hp() > 0):
        #player attacks
        print('Your turn to attack!')
        print('1 - Attack with weapon')
        if isinstance(playerCharacter, character.Warrior) and playerCharacter.get_surgeCount() > 0:
            print('2 - Use action surge')
        elif isinstance(playerCharacter, character.Wizard) and playerCharacter.get_spellslots() > 0:
            print('2 - Cast a spell attack')
        elif isinstance(playerCharacter, character.Rogue) and playerCharacter.get_hidden() == False:
            print('2 - Hide')
        elif isinstance(playerCharacter, character.Rogue) and playerCharacter.get_hidden() == True:
            print('2 - Use sneak attack')
        print('3 - Run away!')

        user_input = input()
        while user_input != '1' and user_input != '2' and user_input != '3':
            print('Please enter a valid input:')
            user_input = input()

        if user_input == '1':
            #weapon attack
            print('You attack with your weapon.')
            attackRoll = rollDice('1d20') + 2 + max(playerCharacter.get_strength(), playerCharacter.get_dexterity())

            if attackRoll > enemyCharacter.get_armor_class():
                #attack hits
                damageRoll = rollDice('1d8') + max(playerCharacter.get_strength(), playerCharacter.get_dexterity())
                print('You deal ', damageRoll, ' damage!')
                enemyCharacter.set_current_hp(enemyCharacter.get_current_hp() - damageRoll)
            else:
                #attack misses
                print('The attack misses!')

        elif user_input == '2':
            #class attack
            if isinstance(playerCharacter, character.Warrior):
                #action surge
                print('You surge with strength! Attack twice!')
                playerCharacter.set_surgeCount(playerCharacter.get_surgeCount() - 1)
                attackRoll = rollDice('1d20') + 2 + playerCharacter.get_strength()
                if attackRoll > enemyCharacter.get_armor_class():
                    damageRoll = rollDice('1d8') + playerCharacter.get_strength()
                    print('You deal ', damageRoll, ' damage!')
                    enemyCharacter.set_current_hp(enemyCharacter.get_current_hp() - damageRoll)
                else:
                    print('Your first attack misses')
                attackRoll = rollDice('1d20') + 2 + playerCharacter.get_strength()
                if attackRoll > enemyCharacter.get_armor_class():
                    damageRoll = rollDice('1d8') + playerCharacter.get_strength()
                    print('You deal ', damageRoll, ' damage!')
                    enemyCharacter.set_current_hp(enemyCharacter.get_current_hp() - damageRoll)
                else:
                    print('Your second attack misses')

            elif isinstance(playerCharacter, character.Wizard):
                #spell attack
                print('You case Magic Missile for a guaranteed hit!')
                playerCharacter.set_spellslots(playerCharacter.get_spellslots()-1)
                damageRoll = rollDice('3d4') + 3
                print('You deal ', damageRoll, 'damage!')
                enemyCharacter.set_current_hp(enemyCharacter.get_current_hp() - damageRoll)

            elif isinstance(playerCharacter, character.Rogue):
                if playerCharacter.get_hidden() == False:
                    #hide
                    stealthRoll = rollDice('1d20') + 2 + playerCharacter.get_dexterity()
                    perceptionRoll = rollDice('1d20') + enemyCharacter.get_wisdom()
                    if stealthRoll > perceptionRoll:
                        print("You successfully hide!")
                        playerCharacter.set_hidden(True)
                    else:
                        print("You fail to hide!")
                else:
                    #sneak attack
                    print("You use a sneak attack!")
                    playerCharacter.set_hidden(False)
                    attackRoll = max(rollDice('1d20'), rollDice('1d20')) + 2 + playerCharacter.get_dexterity()
                    if attackRoll > enemyCharacter.get_armor_class():
                        damageRoll = rollDice('1d8') + rollDice('1d6') + playerCharacter.get_dexterity()
                        print('You deal ', damageRoll, ' damage!')
                        enemyCharacter.set_current_hp(enemyCharacter.get_current_hp() - damageRoll)
                    else:
                        print('The attack misses!')

        elif user_input == '3':
            #run away
            print('You run away')
            return

        if enemyCharacter.get_current_hp() > 0:
            #enemy attacks
            print('The ', enemyCharacter.get_name(), ' attacks!')
            attackRoll = rollDice('1d20') + 4
            if attackRoll >= playerCharacter.get_armor_class():
                #attack hits
                damageRoll = rollDice('1d4') + 2
                print('You take ', damageRoll, ' damage!')
                playerCharacter.set_current_hp(playerCharacter.get_current_hp() - damageRoll)
            else:
                #attack misses
                print('The attack misses!')
            print('You have ', playerCharacter.get_current_hp(), ' hit points remaining.')

    if playerCharacter.get_current_hp() <= 0:
        print('You are dead. Thank you for playing')
        quit()
    
    if enemyCharacter.get_current_hp() <= 0:
        print('You are victorious!')
        return