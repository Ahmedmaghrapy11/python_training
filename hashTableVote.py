voted = {}

def checkVoter(name):
    if voted.get(name) == True:
        print("Kick him out")
    else:
        voted[name] = True
        print("Let him vote")

checkVoter("ahmad")
checkVoter("ahmad")
checkVoter("hesham")