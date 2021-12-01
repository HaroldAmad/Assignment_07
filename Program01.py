import re

print("Character Checker")

def counter ():
    sentenceF = input("Please input your sentence here: ")
    wordCount = len(sentenceF.split(" "))

    vowelsCount = 0
    consonantsCount = 0

    vowels =  re.split(r"\s", "a e i o u")
    consonants = re.split(r"\s", "b c d f g h j k l m n p q r s t v w x y z")
    
