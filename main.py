"""Password Strength Checker & Generator
Author: Nourhen Abid
Description : 
Python program that evaluates password strength and generates secure passwords.
Includes pattern detection, uppercase/symbol checks, entropy calculation and a menu interface."""
import P1
#class main is for the creation of the interface 
class main:
    @staticmethod
    #method menu creates a menu with three choises and deals with each case seperately
    #even the case where the user enter an invalid number or completely something else like a letter or symbol
    def menu():
        while True:
            print("1. Enter your Password: ")
            print("2. Get a generated Password: ")
            print("3. Exit")
            try:
                action=int(input("enter a number between 1 and 3: "))
            #if the user enters something other than a number a valueerror is thrown 
            except ValueError as t:
                print(f"this error accures:{t}")
                
            else:
                if action==3 :
                    print("GOODBYE")
                    break
                elif action==1:
                    password = input("Enter a password: ")
                    strenthOfPassword= P1.User.checkPasswordStrengthOfUser(password)
                    print(strenthOfPassword)
                elif action==2:
                    print(P1.Computer.generator())   
                else: 
                    # in the case where the user enters a number that is out of the intervall[1,3]
                    print("invalid choice, Choose again!")
 
main.menu()
