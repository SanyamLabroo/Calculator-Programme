#Importing Modules
import os
import math
import time
from tqdm import tqdm
import pyttsx3
import speech_recognition as sr
import datetime


#For clearing the terminal
if __name__ == '__main__':
	clear = lambda: os.system('cls')

	clear()

#For loading screen
print("Making your Calculator ready to use...")
time.sleep(2)
print("This may take a while...")
for _ in tqdm(range(100),
        desc = "Loading your Calculator...",
        ascii = False, ncols =75):
    time.sleep(0.1)

print("Starting Calculator...")
time.sleep(2)
print("Here you GO...")
time.sleep(2)

clear()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)       #1 for female voice and 0 for male voice

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def wishMe():
	hour = int(datetime.datetime.now().hour)
	if hour>= 0 and hour<12:
		speak("Good Morning Sanyam !")

	elif hour>= 12 and hour<18:
		speak("Good Afternoon Sanyam !") 

	else:
		speak("Good Evening Sanyam !")

wishMe()

def commands():
    
    speak("I am your Virtual calculator.")
    speak("The operations which you can perform will be listed below.")
    
commands()

#Function to add two numbers
def add(num1, num2): 
	return num1 + num2 

# Function to subtract two numbers 
def subtract(num1, num2): 
	return num1 - num2 

# Function to multiply two numbers 
def multiply(num1, num2): 
	return num1 * num2 

# Function to divide two numbers 
def divide(num1, num2): 
	return num1 / num2 
    
# Python program to find LCM of two numbers

# Recursive function to return gcd of a and b
def gcd(num1,num2):
	if num1 == 0:
		return num2
	return gcd(num2 % num1, num1)

# Function to return LCM of two numbers
def lcm(num1,num2):
	return (num1 / gcd(num1,num2))* num2

#Function to return HCF of two numbers
def hcf(num1,num2): 
	if(num2==0): 
		return num1 
	else: 
		return hcf(num2,num1%num2) 

# Function to return factorial of a number
def factorial(n): 
	if n < 0: 
		return 0
	elif n == 0 or n == 1: 
		return 1
	else: 
		fact = 1
	while(n > 1): 
		fact *= n 
		n -= 1
	return fact

#Summary of the commands of the calculator
def summary():
    speak("Here is the breaf of the instructions:")
    
    speak("1st. Addition of two numbers")
    print("1. Addition of two numbers")
    
    speak("2nd. Subtraction of two numbers")
    print("2. Subtraction of two numbers")
    
    speak("3rd. Multiplication of two numbers")
    print("3. Multiplication of two numbers")
    
    speak("4th. Division of two numbers")
    print("4. Division of two numbers")
    
    speak("5th. LCM of two numbers")
    print("5. LCM of two numbers")
    
    speak("6th. HCF of two numbers")
    print("6. HCF of two numbers") 
    
    speak("7th. SquareRoot of a number")
    print("7. SquareRoot of a number") 
    
    speak("8th. Log value of a number")
    print("8. Log value of a number")
    
    speak("9th. Log with base 'user input' of a number")
    print("9. Log with base 'user input' of a number") 
    
    speak("10th. Square of a number")
    print("10. Square of a number")
    
    speak("11th. Cube of a number")
    print("11. Cube of a number")
    
    speak("12th. Fctorial of a number")
    print("12. Fctorial of a number")
    
    speak("13th. Exponent  of a number with base e")
    print("13. Exponent  of a number with base e")
    
    speak("14th. Power of a number")
    print("14. Power of a number") 
    

#Commands of the calculator
def instructions():
    print("The operations which you can perform are:")
    time.sleep(3)
    speak("1st. Addition of two numbers")
    print("1. Addition of two numbers")
    time.sleep(2)
    speak("2nd. Subtraction of two numbers")
    print("2. Subtraction of two numbers")
    time.sleep(2)
    speak("3rd. Multiplication of two numbers")
    print("3. Multiplication of two numbers")
    time.sleep(2)
    speak("4th. Division of two numbers")
    print("4. Division of two numbers")
    time.sleep(2)
    speak("5th. LCM of two numbers")
    print("5. LCM of two numbers")
    time.sleep(2)
    speak("6th. HCF of two numbers")
    print("6. HCF of two numbers") 
    time.sleep(2)
    speak("7th. SquareRoot of a number")
    print("7. SquareRoot of a number") 
    time.sleep(2)
    speak("8th. Log value of a number")
    print("8. Log value of a number")
    time.sleep(2)
    speak("9th. Log with base 'user input' of a number")
    print("9. Log with base 'user input' of a number") 
    time.sleep(2)
    speak("10th. Square of a number")
    print("10. Square of a number")
    time.sleep(2)
    speak("11th. Cube of a number")
    print("11. Cube of a number")
    time.sleep(2)
    speak("12th. Fctorial of a number")
    print("12. Fctorial of a number")
    time.sleep(2)
    speak("13. Exponent  of a number with base e")
    print("13. Exponent  of a number with base e")
    time.sleep(2)
    speak("14. Power of a number")
    print("14. Power of a number") 
    
instructions()          #For calling the instructions function

time.sleep(4)

#While loop to calculate again and again till user inputs the end statement
while True:
    
# Take input from the user for the commands
    try:
        select = int(input("Please select operations from 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14: "))

#If input is different from the commands then this will be executed
    except ValueError:
        print("Invalid Input!\nTry again...")
        try:
            select = int(input("Please select operations form 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14: "))
            
        except:
            speak("You have typed Invalid input multiple times...")
            #print("You have typed Invalid input multiple times...")
            time.sleep(0.1)
            speak("The program will be closed for now!")
            #print("The program will be closed for now!")
            time.sleep(0.1)
            speak("Please Try Again later...")
            #print("Please Try Again later...")
            time.sleep(0.1)
            speak("Sorry for your inconvenience.")
            #print("Sorry for your inconvenience.")
            time.sleep(0.1)
            break

    time.sleep(2)
    
#If conditions for selecting the commsnds and try except for if user inputs wrong command
    if select == 1:
        try:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            time.sleep(1)
            print("Sum of the given numbers is: ", add(num1, num2)) 
            
        except:
            print("Invalid Input!\nTry again...")
            try:
                num1 = int(input("Enter first number: "))
                num2 = int(input("Enter second number: "))
                time.sleep(1)
                print("Sum of the  given numbers is: ", add(num1, num2)) 
                
            except:
                speak("You have typed Invalid input multiple times...")
                #print("You have typed Invalid input multiple times...")
                time.sleep(0.1)
                speak("The program will be closed for now!")
                #print("The program will be closed for now!")
                time.sleep(0.1)
                speak("Please Try Again later...")
                #print("Please Try Again later...")
                time.sleep(0.1)
                speak("Sorry for your inconvenience.")
                #print("Sorry for your inconvenience.")
                time.sleep(0.1)
                break
            

    elif select == 2:
        try:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            time.sleep(1)
            print("Subtraction of the given numbers is: ", subtract(num1, num2)) 
            
        except:
            print("Invalid Input!\nTry again...")
            try:
                num1 = int(input("Enter first number: "))
                num2 = int(input("Enter second number: "))
                time.sleep(1)
                print("Subtraction of the  given numbers is: ", subtract(num1, num2)) 
                
            except:
                speak("You have typed Invalid input multiple times...")
                #print("You have typed Invalid input multiple times...")
                time.sleep(0.1)
                speak("The program will be closed for now!")
                #print("The program will be closed for now!")
                time.sleep(0.1)
                speak("Please Try Again later...")
                #print("Please Try Again later...")
                time.sleep(0.1)
                speak("Sorry for your inconvenience.")
                #print("Sorry for your inconvenience.")
                time.sleep(0.1)
                break
            
            
    elif select == 3: 
        try:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            time.sleep(1)
            print("Multiplication of the given numbers is: ", multiply(num1, num2)) 

        except:
            print("Invalid Input!\nTry again...")
            try:
                num1 = int(input("Enter first number: "))
                num2 = int(input("Enter second number: "))
                time.sleep(1)
                print("Multiplication of the given numbers is: ", multiply(num1, num2))
                
            except:
                speak("You have typed Invalid input multiple times...")
                #print("You have typed Invalid input multiple times...")
                time.sleep(0.1)
                speak("The program will be closed for now!")
                #print("The program will be closed for now!")
                time.sleep(0.1)
                speak("Please Try Again later...")
                #print("Please Try Again later...")
                time.sleep(0.1)
                speak("Sorry for your inconvenience.")
                #print("Sorry for your inconvenience.")
                time.sleep(0.1)
                break
            

    elif select == 4: 
        try:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            time.sleep(1)
            print("Division of the  given numbers is: ", divide(num1, num2)) 
            
        except:
            print("Invalid Input!\nTry again...")
            try:
                num1 = int(input("Enter first number: "))
                num2 = int(input("Enter second number: "))
                time.sleep(1)
                print("Division of the  given numbers is: ", divide(num1, num2))
                
            except:
                speak("You have typed Invalid input multiple times...")
                #print("You have typed Invalid input multiple times...")
                time.sleep(0.1)
                speak("The program will be closed for now!")
                #print("The program will be closed for now!")
                time.sleep(0.1)
                speak("Please Try Again later...")
                #print("Please Try Again later...")
                time.sleep(0.1)
                speak("Sorry for your inconvenience.")
                #print("Sorry for your inconvenience.")
                time.sleep(0.1)
                break
    
    
    elif select == 5:
        try:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            time.sleep(1)
            print("LCM of the  given numbers is: ", abs(lcm(num1, num2)))      #abs() for converting negative output to positive
            
        except:
            print("Invalid Input!\nTry again...")
            try:
                num1 = int(input("Enter first number: "))
                num2 = int(input("Enter second number: "))
                time.sleep(1)
                print("LCM of the  given numbers is:", abs(lcm(num1, num2)))
                
            except:
                speak("You have typed Invalid input multiple times...")
                #print("You have typed Invalid input multiple times...")
                time.sleep(0.1)
                speak("The program will be closed for now!")
                #print("The program will be closed for now!")
                time.sleep(0.1)
                speak("Please Try Again later...")
                #print("Please Try Again later...")
                time.sleep(0.1)
                speak("Sorry for your inconvenience.")
                #print("Sorry for your inconvenience.")
                time.sleep(0.1)
                break
            

    elif select == 6:
        try:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            time.sleep(1)
            print ("HCF of the  given numbers is: ",abs(hcf(num1,num2)))       
            
        except:
            print("Invalid Input!\nTry again...")
            try:
                num1 = int(input("Enter first number: "))
                num2 = int(input("Enter second number: "))
                time.sleep(1)
                print ("HCF of the given numbers is: ",abs(hcf(num1,num2)))
                
            except:
                speak("You have typed Invalid input multiple times...")
                #print("You have typed Invalid input multiple times...")
                time.sleep(0.1)
                speak("The program will be closed for now!")
                #print("The program will be closed for now!")
                time.sleep(0.1)
                speak("Please Try Again later...")
                #print("Please Try Again later...")
                time.sleep(0.1)
                speak("Sorry for your inconvenience.")
                #print("Sorry for your inconvenience.")
                time.sleep(0.1)
                break
            

    elif select == 7:
        try:
            num = int(input("Enter the value of Number to find square root of: "))
            x = math.sqrt(num)
            time.sleep(1)
            print("Square Root of {0} is = {1}".format(num,x))

        except:
            print("Invalid Input!\nTry again...")
            try:
                num = int(input("Enter the value of Number to find square root of: "))
                x = math.sqrt(num)
                time.sleep(1)
                print("Square Root of {0} is = {1}".format(num,x))
                
            except:
                speak("You have typed Invalid input multiple times...")
                #print("You have typed Invalid input multiple times...")
                time.sleep(0.1)
                speak("The program will be closed for now!")
                #print("The program will be closed for now!")
                time.sleep(0.1)
                speak("Please Try Again later...")
                #print("Please Try Again later...")
                time.sleep(0.1)
                speak("Sorry for your inconvenience.")
                #print("Sorry for your inconvenience.")
                time.sleep(0.1)
                break
            

    elif select == 8:
        try:
            Log = int(input("Enter the number whose log value is to be found: "))
            if Log < 0:
                time.sleep(1)
                print("log is not defined for negative numbers!\nTry again...")
                Log = int(input("Enter the number whose log value is to be found: "))
                time.sleep(1)
                print ("Natural logarithm of the given number is:",math.log(Log))
            
            else:
                print ("Natural logarithm of the given number is:",math.log(Log)) 
            
        except:
            print("Invalid Input!\nTry again...")
            try:
                Log = int(input("Enter the number whose log value is to be found: "))
                if Log < 0:
                    time.sleep(1)
                    print("log is not defined for negative numbers!\nTry again...")
                    Log = int(input("Enter the number whose log value is to be found: "))
                    time.sleep(1)
                    print ("Natural logarithm of the given number is:",math.log(Log))
                
                else:
                    print ("Natural logarithm of the given number is:",math.log(Log))
                    
            except:
                speak("You have typed Invalid input multiple times...")
                #print("You have typed Invalid input multiple times...")
                time.sleep(0.1)
                speak("The program will be closed for now!")
                #print("The program will be closed for now!")
                time.sleep(0.1)
                speak("Please Try Again later...")
                #print("Please Try Again later...")
                time.sleep(0.1)
                speak("Sorry for your inconvenience.")
                #print("Sorry for your inconvenience.")
                time.sleep(0.1)
                break


    elif select == 9:
        try:
            Lognum = int(input("Enter the number whose log value is to be found: "))
            Logbase = int(input("Enter the value of the base of the log: "))
            if Lognum < 0 or Logbase < 0:
                time.sleep(1)
                print("Log is not valid for negative values!\nTry again...")
                try:
                    Lognum = int(input("Enter the number whose log value is to be found: "))
                    Logbase = int(input("Enter the value of the base of the log: "))
                    time.sleep(1)
                    print ("Logarithm of the number with the given base is: ",math.log(Lognum,Logbase))
                
                except:
                    print("Invalid Input")
            else:
                print ("Logarithm of the number with the given base is: ",math.log(Lognum,Logbase))         #Log is not defined for negative values
            
        except:
            print("Invalid Input!\nTry again...")
            try:
                Lognum = int(input("Enter the number whose log value is to be found: "))
                Logbase = int(input("Enter the value of the base of the log: "))
                if Lognum < 0 or Logbase < 0:
                    time.sleep(1)
                    print("Log is not valid for negative values!\nTry again...")
                    try:
                        Lognum = int(input("Enter the number whose log value is to be found: "))
                        Logbase = int(input("Enter the value of the base of the log: "))
                        time.sleep(1)
                        print ("Logarithm of the number with the given base is: ",math.log(Lognum,Logbase))
                    
                    except:
                        speak("You have typed Invalid input multiple times...")
                        #print("You have typed Invalid input multiple times...")
                        time.sleep(0.1)
                        speak("The program will be closed for now!")
                        #print("The program will be closed for now!")
                        time.sleep(0.1)
                        speak("Please Try Again later...")
                        #print("Please Try Again later...")
                        time.sleep(0.1)
                        speak("Sorry for your inconvenience.")
                        #print("Sorry for your inconvenience.")
                        time.sleep(0.1)
                        break
                    
            except:
                speak("You have typed Invalid input multiple times...")
                #print("You have typed Invalid input multiple times...")
                time.sleep(0.1)
                speak("The program will be closed for now!")
                #print("The program will be closed for now!")
                time.sleep(0.1)
                speak("Please Try Again later...")
                #print("Please Try Again later...")
                time.sleep(0.1)
                speak("Sorry for your inconvenience.")
                #print("Sorry for your inconvenience.")
                time.sleep(0.1)
                break
                
            else:
                print ("Logarithm of the number with the given base is: ",math.log(Lognum,Logbase))

            
    elif select == 10:
        try:
            sqrnum = int(input("Enter the value of the number whose Square has to be found: "))
            square = sqrnum ** 2
            time.sleep(1)
            print("Square of {0} is = {1}".format(sqrnum,square))
            
        except:
            print("Invalid Input!\nTry again...")
            try:
                sqrnum = int(input("Enter the value of the number whose Square has to be found: "))
                square = sqrnum ** 2
                time.sleep(1)
                print("Square of {0} is = {1}".format(sqrnum,square))
                
            except:
                speak("You have typed Invalid input multiple times...")
                #print("You have typed Invalid input multiple times...")
                time.sleep(0.1)
                speak("The program will be closed for now!")
                #print("The program will be closed for now!")
                time.sleep(0.1)
                speak("Please Try Again later...")
                #print("Please Try Again later...")
                time.sleep(0.1)
                speak("Sorry for your inconvenience.")
                #print("Sorry for your inconvenience.")
                time.sleep(0.1)
                break
        
        
    elif select == 11:
        try:
            cubenum = int(input("Enter the value of the number whose cube has to be found: "))
            cube = cubenum * cubenum * cubenum
            time.sleep(1)
            print("Cube of {0} is = {1}".format(cubenum,cube))
            
        except:
            print("Invalid Input!\nTry again...")
            try:
                cubenum = int(input("Enter the value of the number whose cube has to be found: "))
                cube = cubenum * cubenum * cubenum
                time.sleep(1)
                print("Cube of {0} is = {1}".format(cubenum,cube))
                
            except:
                speak("You have typed Invalid input multiple times...")
                #print("You have typed Invalid input multiple times...")
                time.sleep(0.1)
                speak("The program will be closed for now!")
                #print("The program will be closed for now!")
                time.sleep(0.1)
                speak("Please Try Again later...")
                #print("Please Try Again later...")
                time.sleep(0.1)
                speak("Sorry for your inconvenience.")
                #print("Sorry for your inconvenience.")
                time.sleep(0.1)
                break

        
    elif select == 12:
        try:
            factnum = int(input("Enter the number whose factorial is to be found: "))
            if factnum < 0:
                time.sleep(1)
                print("Please Enter a positive value.")
                factnum = int(input("Enter the number whose factorial is to be found: "))
                time.sleep(1)
                print("Factorial of the given number is:",factorial(factnum))
                
            else:
                print("Factorial of the given number is:",factorial(factnum))

        except:
            print("Invalid Input!\nTry again...")
            try:
                factnum = int(input("Enter the number whose factorial is to be found: "))
                if factnum < 0:
                    time.sleep(1)
                    print("Please Enter a positive value.")
                    time.sleep(2)
                    factnum = int(input("Enter the number whose factorial is to be found: "))
                    time.sleep(1)
                    print("Factorial of the given number is:",factorial(factnum))

                else:
                    print("Factorial of the given number is:",factorial(factnum))
                    
            except:
                speak("You have typed Invalid input multiple times...")
                #print("You have typed Invalid input multiple times...")
                time.sleep(0.1)
                speak("The program will be closed for now!")
                #print("The program will be closed for now!")
                time.sleep(0.1)
                speak("Please Try Again later...")
                #print("Please Try Again later...")
                time.sleep(0.1)
                speak("Sorry for your inconvenience.")
                #print("Sorry for your inconvenience.")
                time.sleep(0.1)
                break

        
    elif select == 13:
        try:
            expnum = int(input("Enter the number whose exponent is to be found: "))
            time.sleep(1)
            print("Exponent of the given number with base e is:",math.exp(expnum))         #Exponent is defined for negative values also
            
        except:
            print("Invalid Input!\nTry again...")
            try:
                expnum = int(input("Enter the number whose exponent is to be found: "))
                time.sleep(1)
                print("Exponent of the given number with base e is:",math.exp(expnum))        #This is the Exponent of e with power 5.
                
            except:
                speak("You have typed Invalid input multiple times...")
                #print("You have typed Invalid input multiple times...")
                time.sleep(0.1)
                speak("The program will be closed for now!")
                #print("The program will be closed for now!")
                time.sleep(0.1)
                speak("Please Try Again later...")
                #print("Please Try Again later...")
                time.sleep(0.1)
                speak("Sorry for your inconvenience.")
                #print("Sorry for your inconvenience.")
                time.sleep(0.1)
                break

    
    elif select == 14:
        try:
            number = int(input("Please Enter any Positive Integer: "))
            exponent = int(input("Please Enter Exponent Value: "))
            power = 1
            
            for i in range(1, exponent + 1):
                power = power * number

            time.sleep(1)
            
            print("The Result of {0} Power {1} = {2}".format(number, exponent, power))
            
        except:
            print("Invalid Input!\nTry again...")
            try:
                number = int(input("Please Enter any Positive Integer: "))
                exponent = int(input("Please Enter Exponent Value: "))
                power = 1
            
                for i in range(1, exponent + 1):
                    power = power * number
    
                time.sleep(1)
                
                print("The Result of {0} Power {1} = {2}".format(number, exponent, power))
                
            except:
                speak("You have typed Invalid input multiple times...")
                #print("You have typed Invalid input multiple times...")
                time.sleep(0.1)
                speak("The program will be closed for now!")
                #print("The program will be closed for now!")
                time.sleep(0.1)
                speak("Please Try Again later...")
                #print("Please Try Again later...")
                time.sleep(0.1)
                speak("Sorry for your inconvenience.")
                #print("Sorry for your inconvenience.")
                time.sleep(0.1)
                break

    time.sleep(2)
    
    #For showing the commands again
    show = input("If you want to read the commands again please enter 'show commands'.If not press any key: ")
    
    if show == "show commands" or show == "Show commands" or show == "Show Commands" or show == "SHOW COMMANDS":
        summary()
    
    #To rerun the program or to calculate again
    
    rerun = input("Do you want to calculate again?\nPlease enter 'yes' or 'no': ").lower()
        
    if rerun == "yes" or rerun == " Yes" or rerun == "YES":
        continue
    
    if rerun == "no" or rerun == "No" or rerun == "NO":
        speak("Thank You!")
        print("Thank You...:)")
        time.sleep(1)
        break
        
    else:
        print("Invalid Input!")
        time.sleep(2)
        print("Please Try again...")
        time.sleep(2)
        
        rerun = input("Do you want to calculate again?\nPlease enter 'yes' or 'no': ").lower()
            
        if rerun == "yes" or rerun == " Yes" or rerun == "YES":
            continue
    
        if rerun == "no" or rerun == "No" or rerun == "NO":
            speak("Thank You!")
            print("Thank You...:)")
            time.sleep(1)
            break
        
        else:
            speak("You have typed Invalid input multiple times...")
            #print("You have typed Invalid input multiple times...")
            time.sleep(0.1)
            speak("The program will be closed for now!")
            #print("The program will be closed for now!")
            time.sleep(0.1)
            speak("Please Try Again later...")
            #print("Please Try Again later...")
            time.sleep(0.1)
            speak("Sorry for your inconvenience.")
            #print("Sorry for your inconvenience.")
            time.sleep(0.1)
            break
            

