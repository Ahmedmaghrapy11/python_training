# list of admins
from os import stat


admins = ["Ahmed" , "Osama" , "Sameh" , "Manal" , "Rahma" , "Mohamed" , "Enas"]

# login
name = input("Enter your name: ").strip().capitalize()

# check if name is in admins list
if name in admins: 
    print(f"Hello {name}, Welcome back!")
    option = input("Delete or Update your name?").strip().lower()
    if option == "update" or option == 'u':          # update option chosen by the user
        newName = input("Enter your new name: ")
        admins[admins.index(name)] = newName
        print("Name is updated!")
        print(admins)
    elif option == "delete" or option == 'd':        # delete option chosen by the user
        admins.remove(name)
        print("Name is deleted!")
        print(admins)
    else:                           # wrong option chosen by the user
        print("Undefined option!\nPlease choose update(u) or delete(d) option.")
else:
    status = input("You are not admin,\nDo you want to be an admin ? Y/N ").strip().capitalize()
    if status == "Yes" or status == 'Y':
        admins.append(name)
        print("You are added as an admin")
        print(admins)
    else:
        print("You are not added as an admin.\nFuck off!")