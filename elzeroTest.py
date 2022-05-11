# myName = "ahmad khalid"
# myAge = 20
# myJob = "MEDICAL SOFTWARE ENGINEER"
# myRank = 10.0

# print("my name is %s" % myName)
# print("my name is %s, I am %d years old" %(myName,myAge))
# print("my name is %s, I am %d years old, I am a %s in egypt." %(myName,myAge,myJob))
# print("my name is {:s}, I am {:d} years old, I am a {:s} in egypt and my rank is : {:.2f}" .format(myName,myAge,myJob,myRank))
# print(f"my name is {myName}, I am {myAge}, I am {myJob}, myrank is {myRank}")
# longString = "hello, my name is ahmad, I am medical software student at fcih."
# print("message is : %.23s" %longString)

#Rearrange variables in formatting
# x , y , z = 10 , 20 , 30
# print("hello {:f} {:d} {:.2f}".format(x,y,z))
# print("hello {2:f} {0:d} {1:.2f}".format(x,y,z))
# print("hello {1:f} {0:d} {2:.2f}".format(x,y,z))
# print("hello {0:f} {2:d} {1:.2f}".format(x,y,z))

#the new new way formatting text
# myName = "ahmad"
# myAge = 20
# print(f"I'm {myName} and I'm {myAge} years old.")

# x , y , z = 5 , 2.5 , 7 + 9j
# print(int(y))
# print(float(x))
# print(complex(x))
# print(complex(y))

# def sum(arr):
#     total = 0
#     for x in arr:
#         total += x
#     return total
# print(sum([2,4,6,8]))

# myList = ["one" , "two" , "one" , 1 , 100.6 , True]
# print(myList)
# print(myList[1])
# print(myList[1:4])
# print(myList[-1])
# print(myList[-3])

# myFriends = ["hussien" , "youssif" ,"tharwat"]
# myOldFriends = ["omar" , "ibrahim" , "ezzat"]
# print(myFriends)
# myFriends.append("said")
# print(myFriends)
# myFriends.append("ziad")
# print(myFriends)
# myFriends.append(myOldFriends)
# print(myFriends)
# print(myFriends[-1])
# print(myFriends[-1] [1])

# a = [1,2,3]
# b = ["ahmad" , "mahmoud" , "ziad"]
# a.extend(b)
# print(a)
# a.remove("mahmoud")
# print(a)

# x = [5,10,2,5,3,100,55,5,400]
# print(x)
# x.sort(reverse=True)
# print(x)
#y = x.copy()
# print(x)
# print(y)
# print(x.count(5))
# print(x.index(5))
# help("keywords")

#sets
# a = {1,2,3,4,5}
# a.add(8)
# print(a)

#dictionary
# user = {
#     "name" : "ahmad",
#     "age" : 21,
#     "country" : "egypt",
#     "job" : "fullstack web developer",
#     "skills" : ["html" , "css" , "js" , "python"]
# }

# print(user)

# print(user["name"])
# print(user["job"])

# print(user.get("name"))
# print(user.get("job"))

# print(user.keys())
# print(user.values())

# two-dimensional dictionary
# languages ={
#     "one" : {
#         "name" : "html",
#         "progress" : "100%"
#     },
#     "two" : {
#         "name" : "css",
#         "progress" : "40%"
#     },
#     "three" : {
#         "name" : "js",
#         "progress" : "60%"
#     }
# }
# print(languages)
# print(languages["one"])
# print(languages["three"]["name"])
# print(len(languages))
# print(len(languages["two"]))

#user input

# firstName = input("Enter your first name: ")
# middleName = input("Enter your middle name: ")
# lastName = input("Enter you last name: ")

# firstName = firstName.strip().capitalize()
# middleName = middleName.strip().capitalize()
# lastName = lastName.strip().capitalize()

# print(f"hello {firstName} {middleName:.1s}. {lastName} nice to see you!")

# name = input("Enter your full name: ").strip().capitalize()
# email = input("Enter your professianl email: ").strip()
# userName = email[:email.index("@")]
# website = email[email.index("@") + 1:]

# print(f"Hello {name}, your professional email is {email}, \n your username is {userName} and your website is {website}")

# age = int(input("Enter your age: "))

# months = age * 12
# weeks = months * 4
# days = age * 365
# hours = days * 24
# minutes = hours * 60
# seconds = minutes * 60

# print("you lived: ")
# print(f"{months} months")
# print(f"{weeks:,} weeks")
# print(f"{days:,} days")
# print(f"{hours:,} hours")
# print(f"{minutes:,} minutes")
# print(f"{seconds:,} seconds")

# movieRate = 18
# age = 16

# print("movie is not good for you" if age < movieRate else "movie is good for you")

# age = input("Enter your age: ").strip()
# unit = input("Enter the unit you want your age to be calculated in [months, weeks or days]: ").strip().lower()

# months = int(age) * 12
# weeks = months * 4
# days = int(age) * 365

# if unit == "months":
#     print("you choosed months.")
#     print(f"your lived {months:,} months!")
# elif unit == "weeks":
#     print("you choosed weeks.")
#     print(f"your lived {weeks:,} weeks!")
# elif unit == "days":
#     print("you choosed days.")
#     print(f"your lived {days:,} days!")
# else:
#     print("undefined unit!")

# a = 1
# while a < 10:
#     print(a)
#     a = a + 1
# print("loop is done!")

# range = range(1,100)
# for n in range:
#     print(n)

# for loop on dictionary
# mySkills = {
#     "html" : "90%",
#     "css" : "80%",
#     "js" : "70%"
# }
# for key in mySkills:
#     print(f"My progress in {key} is {mySkills.get(key)}")

# people = ["khaled" , "ahmad" , "hesham" , "fatma"]
# skills = ["html".upper(), "css".upper(), "js".upper()]
# for person in people:
#     print(person)
#     for skill in skills:
#         print(f"-{skill}")

# nested for loop on dictionary
# people = {
#     "khaled" : {
#         "html" : "100%",
#         "css" : "100%",
#         "js" : "100%"
#     },
#     "ahmad" : {
#         "html" : "90%",
#         "css" : "70%",
#         "js" : "95%"
#     },
#     "hesham" : {
#         "html" : "80%",
#         "css" : "60%",
#         "js" : "70%"
#     },
#     "fatma": {
#         "html" : "100%",
#         "css" : "100%",
#         "js" : "100%"
#     }
# }

# for name in people:
#     print(f"Skills and progress for {name} is:")
#     for skill in people[name]:
#         print(f"{skill} -> {people[name][skill]}")

# continue, break, pass

# numbers = [1,2,5,7,9,10,13,16,21]
# for n in numbers:
#     if n == 10:
#         continue
#     print(n)

# mySkills = {
#     "HTML" : "80%",
#     "CSS" : "75%",
#     "JS" : "90%"
# }
# print(mySkills.items())

# for skill_key , skill_progress in mySkills.items():
#     print(f"{skill_key} => {skill_progress}")

# myUltimateSkills = {
#     "HTML" : {
#         "main" : "65%",
#         "pugJS" : "75%"
#     },
#     "CSS" : {
#         "main" : "60%",
#         "sass" : "70%"
#     }
# }

# for main_key, main_value in myUltimateSkills.items():
#     print(f"{main_key} progress is: ")
#     for child_key, child_value in main_value.items():
#         print(f"- {child_key} => {child_value}")

# def sayHello(*people):
#     for name in people:
#         print(f"Hello {name}")

# sayHello("ahmad" , "hesham" , "khalid" , "fatma")

# def show_details(name , *skills):
#     print(type(skills))
#     print(f"Hello {name} your skills is: ")
#     for skill in skills:
#         print(f"{skill}")

# show_details("ahmad", "html" , "css" , "js")

# mySkills ={
#     "html" : "80%",
#     "css" : "70%",
#     "js" : "75%"
#     }

# def show_skills(**skills):
#     print(type(skills))
#     for skill, value in skills.items():
#         print(f"{skill} => {value}")

# show_skills(**mySkills)

# mySkills ={
#     "html" : "80%",
#     "css" : "70%",
#     "js" : "75%"
#     }

# myTuple = ("python" , "java" , "c++")

# def show_skills(name, *skills, **skillsWithProgress):
#     print(f"Hello {name} \n your skills without progress are:")
#     for skill in skills:
#         print(f"- {skill}")
#     print("your skills with progress:")
#     for skill_key , skill_value in mySkills.items():
#         print(f"{skill_key} => {skill_value}")

# show_skills("ahmad", *myTuple, **mySkills)

# lambda function and anonymous function
# hello = lambda name, age : f"Hello {name} your age is {age}"
# print(hello("ahmad", 21))
# print(type(hello))

# file handling
# file = open(r"C:\Users\Maghrapy\Documents\files\ahmad.txt" , "r")
# import os
# print(os.getcwd())      # get working directory function
# print(os.path.dirname(os.path.abspath(__file__)))    # return the directory name of the file path
# os.chdir(os.path.dirname(os.path.abspath(__file__)))
# print()

# file = open(r"C:\Users\Maghrapy\Documents\files\ahmad.txt" , "r")
# print(file)
# print(file.name)
# print(file.mode)
# print(file.encoding)
# print(file.read())
# print(file.readline())
# print(file.readlines())
# file.close()

# myFile = open(r"C:\Users\Maghrapy\Documents\files\khaled.txt" , "w")
# myFile.write("Hello dad, I really miss you, I love you!")

# myFile = open(r"C:\Users\Maghrapy\Documents\files\fun.txt","w")
# myFile.write("Elzero Web School\n" * 1000)

# myList = ["ahmad\n" , "khaled\n" , "hesham\n" , "fatma\n"]
# myFile = open(r"C:\Users\Maghrapy\Documents\files\ahmad.txt","a")
# myFile.write("WoW!")

# map function using predefined function
# myList = ["ahmad" , "hesham" , "fatma"]
# def formatText(name):
#     return f"- {name} -"

# myFormatedData = map(formatText , myList)
# print(myFormatedData)

#map function using lambda function
# myList = ["ahmad" , "hesham" , "fatma"]
# myFormatedData = map((lambda name : f"- {name} -" ), myList)
# print(myFormatedData)

# filter function
# myList = [1, 20, 3 ,40 ,50 , 0, 0, 0]
# def checkNum(num):
#     return num > 10
# myResult = filter(checkNum, myList)
# for n in myResult:
#     print(n)

# modules
# from random import random, randrange, randint
# print(f"random float number: {random()}")
# print(f"random int number: {randint(100,300)}")
# print(f"random float number: {randrange(10,100)}")

# #datetime module
# import datetime
# print(datetime.datetime.now())
# print("*" * 50)
# # print current year
# print(datetime.datetime.now().year)
# print("*" * 50)
# # print current month
# print(datetime.datetime.now().month)
# print("*" * 50)
# # print current day
# print(datetime.datetime.now().day)
# print("*" * 50)
# # print start and end date
# print(datetime.datetime.min)
# print(datetime.datetime.max)
# print("*" * 50)
# print the current time
# print(datetime.datetime.now().time())
# # print current time hour
# print(datetime.datetime.now().time().hour)
# # print current time minute
# print(datetime.datetime.now().time().minute)
# # print current time second
# print(datetime.datetime.now().time().second)
# # print start and end of time
# print(datetime.time.min)
# print(datetime.time.max)
# # print specific date
# print(datetime.datetime(2000,11,11))

# # formatting date and time
# import datetime
# myBirthDay = datetime.datetime(2000,11,11)
# print(myBirthDay)
# print(myBirthDay.strftime("%a"))
# print(myBirthDay.strftime("%A"))
# print(myBirthDay.strftime("%b"))
# print(myBirthDay.strftime("%B"))

# iterable VS iterator
# myIterable = "ahmad"
# myIterator = iter(myIterable)
# print(next(myIterator))
# print(next(myIterator))
# print(next(myIterator))
# print(next(myIterator))
# print(next(myIterator))
# print(next(myIterator))

# generator
# def myGenerator():
#     yield 1
#     yield 2
#     yield 3
#     yield 4
# myGen = myGenerator()
# print(next(myGen))
# print(next(myGen))
# print(next(myGen))
# print(next(myGen))

# decorators
# def myDecorator(func):
#     def nestedFunc():
#         print("before")
#         func()
#         print("after")
#     return nestedFunc

# @myDecorator        # sugar sintax => right way
# def sayHello():
#     print("Hello from function!")

# sayHello()
# afterDecorator = myDecorator(sayHello)    =>  wrong way

# afterDecorator()

# decorators with parameters
# def myDecorator(func):
#     def nestedFunc(num1 , num2):
#         if num1 < 0 or num2 < 0:
#             print("beware! one of the numbers is less than zero.")
#         func(num1,num2)
#     return nestedFunc

# def myDecoratorTwo(func):
#     def nestedFuncTwo(num1 , num2):
#         print("message from decorator two!")
#         func(num1,num2)
#     return nestedFuncTwo

# from time import time
# def speedTest(func):
#     def wrapper():
#         start = time()
#         func()
#         end = time()
#         print(f"the function running time equals: {end - start}")
#     return wrapper

# @speedTest
# def bigLoop():
#     for number in range(1 , 20000):
#         print(number)        

# bigLoop()
# @myDecorator
# @myDecoratorTwo
# def calculate(n1 , n2):
#     print(n1 + n2)
# calculate(20,10)

# list1 = [1 , 2 , 3 , 4 , 5]
# list2 = ["A" , "b" , "C"]
# tuple1 = ("man" , "woman" , "girl" , "boy")
# dict1 = {"name":"ahmad", "age" : 21 , "country":"Egypt"}

# for item1, item2, item3, item4 in zip(list1, list2 ,tuple1, dict1):
#     print("list 1 item =>", item1)
#     print("list 2 item =>", item2)
#     print("tuple 1 item =>", item3)
#     print("dict 1 key =>", item4,"dict 1 value => ", dict1[item4])

# image manipulation with pillow
# from PIL import Image

# open the image to deal with it
# myImage = Image.open(r"F:\Learning Projects\Web\ElzeroAssignment\imgs\css-assignment-5-8.png")

# show the image
# myImage.show()

# my cropped image
# myBox = (0, 0, 400, 400)
# myNewImage = myImage.crop(myBox)

# show the new image
# myNewImage.show()

# convert image mode
# myConverted = myImage.convert("L")
# myConverted.show()

# documentation
# def elzero_hello(name):
#     '''this is a function to say hello from elzero'''
#     print(f"Hello {name}")

# help(elzero_hello)

# exception handling => try, except, else & finally
# try:    # try the code and test errors
#      myAge = int(input("enter your age: "))
# except: # handle the errors if found
#     print("this is not integer!")
# else:   # if there is no integer
#     print("good, this is integer!")
# finally:    # work whatever happens
#     print("finally works whatever happens")

# try:
#     print(10/0)
#     print(x)
# except ZeroDivisionError:
#     print("can not divide!")
# except NameError:
#     print("variable is not defined")

# try reading a file from the user
# the_file = None
# the_tries = 5
# while the_tries > 0:
#     try:    #try to open the file
#         print("please! enter the file name with the absolute path: ")
#         print(f"you have {the_tries} left...")
#         print(r"Example: C:\Users\Maghrapy\Documents\files\file.extension")
#         file_name_and_path =input("file name and path: ").strip()
#         the_file = open(file_name_and_path , 'r')
#         print(the_file.read())
#         break
#     except FileNotFoundError:
#         print("file is not found!")
#         the_tries -= 1
#     except:
#         print("error happens!")
#     finally:
#         if the_file is not None:
#             the_file.close()
#             print("file is closed!")
# else:
#     print("you are out of tries!")

# debugging
# myList =[1,2,3,4,5,6]

# myDict = {"name" : "ahmad", "age" : 21, "country" : "Egypt"}

# for num in myList:
#     print(num)

# for key,value in myDict.items():
#     print(f"key => {key} and value => {value}")

# def function_one():
#     print("hello from function")

# function_one()

# type hinting
# def say_hello(name) -> str:
#     print(f"hello {name}")

# regular expression training
# import re
# my_search = re.search("[A-Z]" , "OsamaElzero")
# print(my_search)
# print(my_search.span())

# is_email = re.search(r"^[A-z0-9\.]+@[A-z0-9]+\.(com|net)$" , "ahmad@11.com")

# if is_email:
#     print("this is a valid email")
# else:
#     print("this is not a valid email")

# import re
# email_input = input("Enter your email: ")
# search = re.findall(r"^[A-z0-9\.]+@[A-z0-9]+\.com|net$" , email_input)
# empty_list =[]
# if search != []:
#     empty_list.append(search)
# else:
#     print("invalid e-mail")

# for email in empty_list:
#     print(email)

# import re
# string_one = "I love python programming language"
# search_one = re.split(r"\s", string_one , 1)
# print(search_one)

# # char replacement
# my_string = "I love python"
# print(re.sub(r"\s", "-", my_string, 1))

# OOP
# class Member:
#     def __init__ (self):
#         print("A new member has been added.")

# memberOne = Member()
# memberTwo = Member()
# memberThree = Member()

# print(memberThree.__class__)

# object & class attrubutes and methods
# class Member :

#     not_allowed_names = ["shit", "fuck" , "hell"]
#     users_num = 0

#     def __init__(self , first_name, middle_name , last_name , gender):
#         self.fname = first_name
#         self.mname = middle_name
#         self.lname = last_name
#         self.gender = gender
#         Member.users_num += 1
    
#     @staticmethod
#     def say_hello():
#         print("hello from class method")

#     @classmethod
#     def show_users_count(cls):
#         print(f"we have {cls.users_num} users in the system.")
    
#     def fullName(self):
#         if self.fname in Member.not_allowed_names:
#             raise ValueError("Name is not allowed!")
#         else:
#             return f"{self.fname} {self.mname} {self.lname}"
    
#     def name_with_title(self):
#         if self.gender == "male":
#             return f"Hello Mr {self.fname}"
#         elif self.gender == "female":
#             return f"Hello Miss {self.fname}"
#         else:
#             return f"Hello {self.fname}"
    
#     def get_all_info(self):
#         return f"Hello {self.name_with_title()} your full name is: {self.fullName()}"

#     def delete_user(self):
#         Member.users_num -=1
#         return f"user {self.fname} is deleted!"

# print(dir(Member))
# print(Member.users_num)

# memberOne = Member("ahmad" , "khalid" , "moussa" , "male")
# memberTwo = Member("khalid", "moussa" , "ibrahim" , "male")
# memberThree = Member("fatma" , "mohamed" , "gabr" , "female")
# memberFour = Member("shit" , "fuck" , "hell" , "female")

# print(Member.users_num)

# print(memberOne.fullName())
# print(Member.fullName(memberOne))       # the same as the above line.
# print(memberOne.name_with_title())
# print(memberOne.get_all_info())
# print(memberFour.delete_user())
# print(Member.users_num)
# Member.show_users_count()

# magic method
# class Skills:

#     def __init__(self) -> None:
#         self.skill = ["html" , "css" , "js"]

#     def __str__(self):
#         return f"this is my skills: {self.skill}"
    
#     def __len__(self):
#         return len(self.skill)

# profile = Skills()
# print(len(profile))
# profile.skill.append("python")
# profile.skill.append("mySQL")
# print(len(profile))
# myString = "ahmad"
# print(dir(myString.__class__))
# print(str.upper(myString))

# inheritance
# class Food:     # base class
    
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#         print(f"{self.name} is created from the base class and price is {self.price}.")
    
#     def eat(self):
#         print("eat method from the base class.")

# class Apple(Food):      #derived class

#     def __init__(self, name, price, amount):
#         self.amount = amount
#         # Food.__init__(self, name)     # create instance from base class => is equal to the next lin
#         super().__init__(name, price)
#         print(f"{self.name} is created from the derived class and price is {self.price} and amount is {self.amount}.")
    
#     def get_from_tree(self):
#         print("get from tree from derived class.")

#     # overridden method from Food class
#     def eat(self):
#         print("eat method from the base class.")

# # food_one = Food()
# food_two = Apple("pizza", 120, 2)

# # food_two.eat()

# multiple inheritance

# class BaseOne:
#     def __init__(self) -> None:
#         print("Base One")

# class BaseTwo:
#     def __init__(self):
#         print("Base Two")

# class Derived(BaseOne, BaseTwo):
#     pass

# polymorphism
# class A:
#     def do_something(self):
#         print("from class A")
#         raise NotImplementedError("Derived class must implement this method")

# class B(A):
#     def do_something(self):
#         print("from class B")

# class C(A):
#     def do_something(self):
#         print("from class C")

# encapsulation
# class MemberOne:
#     def __init__(self, name) -> None:
#         self.name = name    # public data

# one = MemberOne("ahmad")
# print(one.name)

# class MemberTwo:
#     def __init__(self, name) -> None:
#         self._name = name    # protected data

# one = MemberTwo("ahmad")
# print(one._name)

# class MemberTwo:
#     def __init__(self, name) -> None:
#         self.__name = name    # private data

#     def say_hello(self):
#         return f"hello{self.__name}"

#     def get_name(self):     # getter method
#         return self.__name

#     def set_name(self, new_name):   # setter method
#         self.__name = new_name

# one = MemberTwo("ahmad")
# print(one.say_hello())
# print(one._MemberTwo__name)     # to access private data from outside
# print(one.get_name())
# one.set_name('khalid')
# print(one.get_name())

# @property decorator
# class Member:
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age
    
#     def say_hello(self):
#         return f"Hello {self.name}"

#     @property
#     def age_in_days(self):
#         return self.age * 365

# one = Member("ahmad" , 21)
# print(one.name)
# print(one.age)
# print(one.age_in_days)

# Abstract classes
# from abc import ABCMeta , abstractmethod

# class Programming(metaclass = ABCMeta):
#     @abstractmethod
#     def has_oop(self):
#         pass

# class Python(Programming):
#     def has_oop(self):
#         return "yes"

# class Pascal(Programming):
#     def has_oop(self):
#         return "no"

# one = Python()
# two = Pascal()

# print(one.has_oop())
# print(two.has_oop())

# databases
# import sqlite3
# from sqlite3.dbapi2 import Cursor
#  create database and connect
# db = sqlite3.connect("app.db")
# # setting up the cursor
# cursor  = db.cursor()
# # create tables and fields
# cursor.execute("CREATE TABLE IF NOT EXISTS users (user_name text, user_id integer)")
# cursor.execute("CREATE TABLE IF NOT EXISTS skills (name text, progress integer, user_id integer)")
# # inserting data into database
# cursor.execute("INSERT INTO users(user_id, user_name) values(1,'ahmad')")
# cursor.execute("INSERT INTO users(user_id, user_name) values(2,'hesham')")
# cursor.execute("INSERT INTO users(user_id, user_name) values(3,'khalid')")
# # save changes made in the database
# db.commit()
# # close database
# db.close()
# my_list = ["ahmad", "sayed" , "mahmoud", "khalid", "hesham", "ibrahim", "osama"]
# db = sqlite3.connect("app2.db")
# cursor = db.cursor()
# cursor.execute("CREATE TABLE IF NOT EXISTS users (user_id integer, user_name text)")
# for key, name in enumerate(my_list):
#     cursor.execute(f"INSERT INTO users(user_id, user_name) values({key + 1},'{name}')")
# db.commit()
# db.close()

# db = sqlite3.connect("app_database.db")
# cursor = db.cursor()

# cursor.execute("CREATE TABLE IF NOT EXISTS users(user_id integer, name text)")
# cursor.execute("create table if not exists skills(name text, progress integer, user_id integer)")

# cursor.execute("insert into users(user_id, name) values(1 , 'ahmad')")
# cursor.execute("insert into users(user_id, name) values(2, 'hesham')")
# cursor.execute("insert into users(user_id, name) values(3, 'khalid')")

# fetch data from database
# cursor.execute("select * from users")

# print(cursor.fetchall())

# db.commit()
# db.close()

# database update and delete
# import sqlite3

# db = sqlite3.connect("app_database.db")

# cursor = db.cursor()
# # updating data in the database
# cursor.execute("update users set name = 'hussein' where user_id = 1")
# cursor.execute("update users set name = 'sa3eed' where user_id = 2")
# cursor.execute("update users set name = 'youssef' where user_id = 3")

# # deleting records from database
# cursor.execute("delete from users where user_id = 2")

# cursor.execute("select * from users")

# print(cursor.fetchone())
# print(cursor.fetchone())
# print(cursor.fetchone())
# print(cursor.fetchone())

# avoiding sql injection for data security
# import sqlite3
# db = sqlite3.connect("app_database.db")
# cursor = db.cursor()
# my_tuple = ("javascript", 65, 1)
# # inserting data into database
# cursor.execute("insert into skills values(?, ?, ?)", my_tuple)
# db.commit()
# db.close()

# timeit module
# import timeit

# print(dir(timeit))

# print(timeit.timeit("'ahmad*10000'"))
# print(timeit.timeit("name = 'ahmad' ; name *1000"))

# print(timeit.repeat(stmt="random.randint(0,50)" , setup="import random", repeat=4))
# print(type(print(timeit.repeat(stmt="random.randint(0,50)" , setup="import random", repeat=4))))

# adding logging to the code
# import logging

# # print(dir(logging))

# logging.basicConfig(filename="my_app.log" , filemode="a", format="%(asctime) | %(name)s | %(levelname) | %(message)", datefmt = "%d %B %Y , %H : %M : %S")
# my_logger = logging.getLogger("ahmad")
# logging.critical("this is critical message")

# testing using unittest module
# import unittest

# assert 3 * 8 == 25, "should be 24"

# def testCaseOne():
#     assert 5 * 10 == 50, "should be 50"

# def testCaseTwo():
#     assert 10 * 10 == 100, "should be 100"

# if __name__ == "__main__":
#     testCaseOne()
#     testCaseTwo()
#     print("all tests are passed successfully!")

# class myTestCase(unittest.TestCase):
    
#     def testOne(self):
#         self.assertTrue(100 > 100, "should be true")
    
#     def testTwo(self):
#         self.assertEqual(100+100, 200, "should be 200")

#     def testTree(self):
#         self.assertGreater(100, 50, "should be true")

# if __name__ == "__main__":
#     unittest.main()

# generating random serial number
import string
import random

# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# print(string.digits)

# def make_serial(count):
    
#     allChars = string.ascii_letters + string.digits
    
#     charCount = len(allChars)
#     serial_list = []

#     while count > 0:
        
#         randomIndex = random.randint(0 , charCount - 1)
#         randomChar = allChars[randomIndex]
#         serial_list.append(randomChar)

#         count = count - 1

#     print("".join(serial_list))

# make_serial(30)