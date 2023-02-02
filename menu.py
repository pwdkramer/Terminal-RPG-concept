title = """
 __        __         _    _             
 \ \      / /__  _ __| | _(_)_ __   __ _ 
  \ \ /\ / / _ \| '__| |/ / | '_ \ / _` |
   \ V  V / (_) | |  |   <| | | | | (_| |
  __\_/\_/_\___/|_|  |_|\_\_|_| |_|\__, |
 |_   _(_) |_| | ___               |___/ 
   | | | | __| |/ _ \                    
   | | | | |_| |  __/                    
   |_| |_|\__|_|\___|                                                             
"""

options="""
1 - Create a Character
2 - View User Manual
3 - Exit Game
"""

def print_menu():
    print(title)
    print("\n\n\n\n")
    print(options)

    menu_input = input()
    while (menu_input != '1' and menu_input != '2' and menu_input != '3'):
        print("Please enter the number 1, 2, or 3:")
        menu_input = input()

    if menu_input == '1':
        #run character creator
        print("go to character creator")
    elif menu_input == '2':
        #run user manual
        print("go to user manual")
    else:
        print("Thanks for playing!")
        quit()