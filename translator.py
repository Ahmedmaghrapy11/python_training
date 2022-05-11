#program to translate any vowel letter(AEIOU)(aeiou) to 'z'

def translate(str):         #function that takes a string to translate it
    translation = ""
    for letter in str:
        if letter.lower() in "AEIOUaeiou":
            translation = translation + "z"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a word: ")))