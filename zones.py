#Zone descriptions

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
    while (user_input != '1' and user_input != '2' and user_input != '3'):
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
    else:
        print('problem with input in arrival')
        quit()

def inn(playerCharacter):
    pass

def townHall(playerCharacter):
    pass

def generalStore(playerCharacter):
    pass

def basement(playerCharacter):
    pass

def outskirts(playerCharacter):
    pass

def wagon(playerCharacter):
    pass

def woods(playerCharacter):
    pass

def cave(playerCharacter):
    pass

def lair(playerCharacter):
    pass

