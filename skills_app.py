# skills application

# import sql module
from cgitb import reset
from hashlib import new
import sqlite3

db = sqlite3.connect("app_database.db")   # create database and connection

cursor = db.cursor()        # setting up cursor

def save_close():
    """save and commit changes to the database"""
    db.commit()     # save(commit) changes
    db.close()    # close database
    print("Connection to database is closed.")

u_id = 1      # user id

##############################################################################################

# big message displayed to user when get input option
input_message = """
what do you want to do ?
"s" => show all skills.
"a" => add a new skill.
"d" => delete a skill.
"u" => update a skill.
"q" => quit the application.
choose option:
"""
# input option choice from user
user_input = input(input_message).strip().lower()

# commands list
commands_list = ["s", "a" , "d" , "u" , "q"]

# defining the methods

def show_all_skills():
    """getting all skills from database"""
    
    cursor.execute(f"select * from skills where user_id = '{u_id}'")
    results = cursor.fetchall()
    print(f"you have {len(results)} skills.")
    if len(results) > 0:
        print("Showing skills with progress: ")
    
    for row in results:
        print(f"Skill => {row[0]}, ", end = " ")
        print(f"Progress => {row[1]}%.")
    
    save_close()

#############################################################################################

def add_new_skill():
    """adding new skill"""
    
    skillName = input("Enter skill name: ").strip().capitalize()
    cursor.execute(f"select name from skills where name = '{skillName}' and user_id = '{u_id}'")
    results = cursor.fetchone()
    
    if results == None:     # skill does not exists in database
        progress = input("Enter progress of the entered skill: ").strip()
        cursor.execute(f"insert into skills(name, progress, user_id) values('{skillName}', '{progress}', '{u_id}')")
        print(f"{skillName} is added to your skills with progress {progress}.")
        save_close()
    
    else:       # skill is already found in the database and offer update option
        optionInput = input(f"{skillName} is already exists, you wanna update it: ")
        if optionInput == "y".lower():
            newProgress = input("Enter new skill progress of the entered skill: ").strip()
            cursor.execute(f"update skills set progress = '{newProgress}' where name = '{skillName}' and user_id = '{u_id}'")
            save_close()
        else:
            print("Application is closed.")

##############################################################################################

def delete_skill():
    """deleting existing skill"""

    skillName = input("Enter skill name: ").strip().capitalize()
    cursor.execute(f"delete from skills where name = '{skillName}' and user_id = '{u_id}'")
    save_close()
    print(f"{skillName} is deleted for user {u_id}")

##############################################################################################

def update_skill():
    """updating existing skill"""

    skillName = input("Enter skill name: ").strip().capitalize()
    newProgress = input("Enter new skill progress of the entered skill: ").strip()
    cursor.execute(f"update skills set progress = '{newProgress}' where name = '{skillName}' and user_id = '{u_id}'")
    save_close()
    print(f"{skillName} is updated with progress {newProgress}.")

##############################################################################################

# check if command exists in the list
if user_input in commands_list:
    print(f"command \"{user_input}\" is found!")
    
    if user_input == "s":
        show_all_skills()
    elif user_input == "a":
        add_new_skill()
    elif user_input == "d":
        delete_skill()
    elif user_input == "u":
        update_skill()
    else:
        print("Application is closed.")
        save_close()

else:
    print(f"sorry command \"{user_input}\" is not found")
