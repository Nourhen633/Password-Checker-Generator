"""Password Strength Checker & Generator
Author: Nourhen Abid
Description : 
Python program that evaluates password strength and generates secure passwords.
Includes pattern detection, uppercase/symbol checks, and a menu interface."""
import random 
import string
import math
"""The User class contains the Password validation logic.
It checks wether the user´s password contains weak sequences like "aaa" or "123" 
wether it includes Uppercases and symbols
and its length to get its grade of strength """
class User:
    #checkRepitition makes sure that there are no weak patterns in the password
    def checkRepetition(password):
        a: str="strong"
        if password.lower()=="password": 
            a="weak"
        for i in range (len(password)-2):
            ch1, ch2, ch3 = password[i], password[i+1], password[i+2]
            if ch1==ch2==ch3 or (ch1.isdigit() and ch2.isdigit() and ch3.isdigit() and int(ch1)+1==int(ch2) and int(ch2)+1==int(ch3)):
                a="weak" 
        return a 
    #this method checks the presence of at least one uppercase and one Symbol   
    def includesUppercaseAndSymbol(password):
        hasUppercase: bool= False
        hasSymbol: bool= False
        symbols = "!@#$%^&*()-_=+[]{};:,.<>?/|\\"
        for i in range(len(password)):
            ch= password[i]
            if "A"<=ch<="Z": hasUppercase=True
            if ch in symbols: hasSymbol=True
        return hasSymbol and hasUppercase 
    # this method checks the length of the password   

    def calculateEntropy (password):
        #s is the character_set_size
        s=0
        length= len(password)
        for i in password:
            if i.isupper() or i.islower() :
                s+=26
            if i.isdigit() :
                s+=10
            if i in string.punctuation:
                s+=32
        entropy = length* math.log2(s)        
        return entropy    


    def checkPasswordStrengthOfUser(password):
        e=User.calculateEntropy(password)
        if len(password)<8 or User.checkRepetition(password)=="weak" or e<40 : 
            return "weak Password : your Password must be longer than 8, has no repetitive cases and includes at least 1 Uppercase, 1 number and 1 Symbol!"
        elif len(password)>12 and User.includesUppercaseAndSymbol(password) and e>=60 :     
           return "strong Password : make it shorter!"
        else:
           return "medium Password!" 
"""The class Computer generates a strong password that has :
at least one Uppercase and symbol
with a length between 8 and 15
and with no weak sequences  """        
class Computer:
    @staticmethod
    #randomOfAllChars generates and returns one random character from all available ASCII letters, numbers and symbols 
    def randomOfAllChars ():
     all_chars= string.ascii_letters + string.punctuation + string.digits
     return random.choice(all_chars)
    @staticmethod
    #generator generates the whole password and makes sure that it is strong 
    def generator():
        g_password: str=""
        while True:
            g_password=""
            length= random.randint(8,16)
            for _ in range (length):
                g_password+=Computer.randomOfAllChars()
            if User.checkPasswordStrengthOfUser(g_password).startswith("strong") :  
                return g_password        