title = """
User Manual
Enter the number next to an item to read more about it.
"""

options = """
1 - Character Attributes
2 - Character Classes
3 - Return to Game
"""

def print_manual():
    print(title)
    print("\n\n\n")
    print(options)

    menu_input = input()
    while (menu_input != '1' and menu_input != '2' and menu_input != '3'):
        print("Please enter a number listed in the options:")
        menu_input = input()

    if menu_input == '1':
        print("character attribute info")
        print("Press enter to return to manual")
        input()
        print_manual()
    elif menu_input == '2':
        print('stuff goes here')
        print("Press enter to return to manual")
        input()
        print_manual()
    else:
        return