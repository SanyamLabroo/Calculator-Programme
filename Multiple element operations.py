from functools import reduce
import time
import os
from itertools import chain, repeat

if __name__ == '__main__':
	clear = lambda: os.system('cls')

	clear()

operations = ["1. Multiple number addition",
                "2. Multiple number subtraction", 
                    "3. Multiple number multiplication", 
                        "4. Multiple number division"]

print("The operations which you can perform are as follows:")

for i in chain.from_iterable(repeat(operations, 1)):
    time.sleep(1)
    print(i)
    


def addition():
    
    list = []
    time.sleep(1)
    try:
        n = int(input("Enter number of elements: ")) 
        
        if n == 1:
            print("Enter more than one element")
            time.sleep(1)
            n = int(input("Enter number of elements: "))
        
    except ValueError:
        print("Please enter an integer value.")
        
        if n == 1:
            print("Enter more than one element.")
            time.sleep(1)
            n = int(input("Enter number of elements: "))
        
        time.sleep(1)
        try:
            n = int(input("Enter number of elements: "))
            
        except ValueError:
            print("You have typed invalid input again!....Please try again later.")
            time.sleep(2)
            exit()
            
    for i in range(0, n): 

        time.sleep(1)
        try:
            ele = int(input("Enter the values of elements: ")) 
            list.append(ele)
            
        except ValueError:
            print("Please enter an integer value.")
            time.sleep(1)
            try:
                ele = int(input("Enter the values of elements: "))
                
            except ValueError:
                print("You have typed invalid input again!....Please try again later.")
                time.sleep(2)
                exit()

    num = reduce(lambda x,y:x+y, list)

    print("Sum of the given numbers is:",num)


def subtraction():
    
    list = []
    time.sleep(1)
    try:
        n = int(input("Enter number of elements: ")) 
        
        if n == 1:
            print("Enter more than one element.")
            time.sleep(1)
            n = int(input("Enter number of elements: "))
        
    except ValueError:
        print("Please enter an integer value.")
        time.sleep(1)
        try:
            n = int(input("Enter number of elements: "))
            
            if n == 1:
                print("Enter more than one element.")
            
        except ValueError:
            print("You have typed invalid input again!....Please try again later.")
            time.sleep(2)
            exit()
        
        
    for i in range(0, n): 

        time.sleep(1)
        try:
            ele = int(input("Enter the values of elements: ")) 
            list.append(ele)
            
        except ValueError:
            print("Please enter an integer value.")
            time.sleep(1)
            try:
                ele = int(input("Enter the values of elements: "))
                
            except ValueError:
                print("You have typed invalid input again!....Please try again later.")
                time.sleep(2)
                exit()

    num = reduce(lambda x,y:x-y, list)
    print("Subtraction of the given numbers is:",num)


def multiplication():
    
    list = []
    time.sleep(1)
    try:
        n = int(input("Enter number of elements: ")) 
        
        if n == 1:
            print("Enter more than one element.")
            time.sleep(1)
            n = int(input("Enter number of elements: "))
    
    except ValueError:
        print("Please enter an integer value.")
        time.sleep(1)
        try:
            n = int(input("Enter number of elements: "))
            
            if n == 1:
                print("Enter more than one element.")
            
        except ValueError:
            print("You have typed invalid input again!....Please try again later.")
            time.sleep(2)
            exit()
        
    for i in range(0, n): 

        time.sleep(1)
        try:
            ele = int(input("Enter the values of elements: ")) 
            list.append(ele)
            
        except ValueError:
            print("You have typed invalid input again!....Please try again later.")
            time.sleep(2)
            exit()

    num = reduce(lambda x,y:x*y, list)
    print("Multiplication of the given numbers is:",num)

def division():
    
    list = []
    time.sleep(1)
    try:
        n = int(input("Enter number of elements: ")) 
        
        if n == 1:
            print("Enter more than one element.")
            time.sleep(1)
            n = int(input("Enter number of elements: "))
        
    except ValueError:
        print("Please enter an integer value.")
        time.sleep(1)
        try:
            n = int(input("Enter number of elements: "))
            
            if n == 1:
                print("Enter more than one element.")
            
        except ValueError:
            print("You have typed invalid input again!....Please try again later.")
            time.sleep(2)
            exit()
        
    for i in range(0, n): 
        
        time.sleep(1)
        try:
            ele = int(input("Enter the values of elements: ")) 
            list.append(ele)
            
        except ValueError:
            print("You have typed invalid input again!....Please try again later.")
            time.sleep(2)
            exit()

    num = reduce(lambda x,y:x/y, list)
    print("Division of the given nubers is:",num)
    

while True:
    
    time.sleep(1)
    try:
        user_input = int(input("Enter command: "))
        
    except ValueError:
        print("Invalid Input\nTry again!")
        time.sleep(1)
        continue

    if user_input == 1:
    
        addition()
    
    
    elif user_input == 2:
    
        subtraction()
    

    elif user_input == 3:
    
        multiplication()
    
    
    elif user_input == 4:
    
        division()
        
    
    else:
        print("Invalid input...\nTry again...")
        continue
    
    time.sleep(2)
    
    rerun = input("Do you want to calculate again?\nPlease enter 'yes' or 'no': ")
    
    if rerun == 'yes':
        continue
    
    elif rerun == 'no':
        print("Thank You!")
        time.sleep(1)
        break
    
    else:
        print("Invalid input...\nTry again!!")
        rerun = input("Do you want to calculate again?\nPlease enter 'yes' or 'no': ")
        
        if rerun == 'yes' or rerun == 'YES' or rerun == 'Yes':
            continue
        
        elif rerun == 'no' or rerun == 'NO' or rerun == 'No':
            print("Thank You!")
            time.sleep(1)
            break
        
        else:
            print('You have entered invalid input again!\nPlease try again later.')
            time.sleep(2)
            break