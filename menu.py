from diceRoll import rollDice

title = """
  ____        _           _       ______ _          _   
 |  _ \      | |         ( )     |  ____(_)        | |  
 | |_) | __ _| |__  _   _|/ ___  | |__   _ _ __ ___| |_ 
 |  _ < / _` | '_ \| | | | / __| |  __| | | '__/ __| __|
 | |_) | (_| | |_) | |_| | \__ \ | |    | | |  \__ \ |_ 
 |____/ \__,_|_.__/ \__, | |___/_|_|    |_|_|  |___/\__|
     /\      | |     __/ |     | |                      
    /  \   __| |_   |___/ _ __ | |_ _   _ _ __ ___      
   / /\ \ / _` \ \ / / _ \ '_ \| __| | | | '__/ _ \     
  / ____ \ (_| |\ V /  __/ | | | |_| |_| | | |  __/     
 /_/    \_\__,_| \_/ \___|_| |_|\__|\__,_|_|  \___|     
                                                        
                                                                                    
"""

options="""
1 - Create a Character
2 - View User Manual
3 - Test Dice Roller
4 - Exit Game
"""

def print_menu():
    print(title)
    print("\n\n\n\n")
    print(options)

    menu_input = input()
    while (menu_input != '1' and menu_input != '2' and menu_input != '3' and menu_input != '4'):
        print("Please enter the number 1, 2, or 3:")
        menu_input = input()

    if menu_input == '1':
        #run character creator
        print("go to character creator")
    elif menu_input == '2':
        #run user manual
        print("go to user manual")
    elif menu_input == '3':
        #test dice roller
        print("Simulate a dice roll. Enter [# of dice]d[# of sides on dice]. Example '2d6' rolls 2 6-sided dice.")
        userDice = input()
        print('You rolled a ',rollDice(userDice))
        print_menu()
    else:
        print("Thanks for playing!")
        quit()