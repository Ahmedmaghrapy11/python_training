# cleaning word from duplicate chars in "WWWoooorrrldd"
# print(x[1:])
def cleanWord(word):
    if len(word) == 1:
        return word
    print(f"word at the start of function:{word}")
    if word[0] == word[1]:
        print(f"word before condition:{word}")              # if first two chars are equal
        return cleanWord(word[1:])  #WWoooorrrldd      #apply cleanWord() from index[1] to the end and neglect first char
    print(f"word before return:{word}")
    return word[0] + cleanWord(word[1:])    #gather the chars of the word and return "World"

print(cleanWord("WWWoooorrrldd"))