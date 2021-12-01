import re
import string

print("Password Checker")

def checker ():
    passwordF = input("Please input your password here: ")
    legendCount = len(passwordF)

    validPoint = 0
    capitalPoint = 0
    numberPoint = 0
    specialPoint = 0

    capital = string.ascii_uppercase
    number = re.split(r"\s", "0 1 2 3 4 5 6 7 8 9")
    specialCharacter = re.split(r"\s", "! # $ % & ' ( ) * + , - . / : ; < = > ? @ [ \ ] ^ _ ` ¿ ¬ « » ° • · ‘ ’ “ ” – — ")

    if legendCount >= 15:
        validPoint += 1
    else:
        validPoint += 0


    for q in passwordF:
        if q in capital:
            validPoint += 1
        else:
            validPoint += 0
            if q in number:
                validPoint += 1
            else:
                validPoint += 0
                if q in specialCharacter:
                    validPoint += 1
                else:
                    validPoint += 0

    if capitalPoint >= 1:
        validPoint += 1
    else:
        validPoint += 0

    if numberPoint >= 1:
        validPoint += 1
    else:
        validPoint += 0

    if specialPoint >= 1:
        validPoint += 1
    else:
        validPoint += 0
    

