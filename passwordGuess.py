tries = 4
mainPassword = "ahmad@11112000"
inputPassword = input("Enter your password: ")
while inputPassword != mainPassword:
    tries -= 1
    print(f"Wrong password!, {'last' if tries == 0 else tries} chances left")
    inputPassword = input("Enter your password: ")
    if tries == 0:
        print("Trying is over!")
        break
else:
    print("Correct password!")