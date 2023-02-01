import os
from time import sleep
from menu import print_menu

menu_selection = print_menu()

if menu_selection == '1':
    #run character creator
    print("go to character creator")
    pass
elif menu_selection == '2':
    #run user manual
    print("go to user manual")
    pass
else:
    quit()