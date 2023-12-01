#26 November 2023
#CTI-110 P5HW - Math Quiz
#Curtis Cooper
"""
Get user input
Evaluate input
Call function 
Function evaluates input
Displays results
"""
#import module
import random
#define addition funtion
def addition():
    
    a = random.randint (0, 20) 
    
    b = random.randint (0, 20) 
    
    count = 0
    
    right = a + b 
    
    question = print(f"What is {a} + {b} ? ") 
    
    answer = int(input())
    
    count += 1
    
    if right == answer:
        
        print ("Congratulations !!! your answer is correct!") 
        
        print('Number of guesses: ', count)
        
        menu()
        
    while right != answer:
        
        if right < answer:
            
            print('Try again:', answer)
            
            print('Sorry guess is to high')
            
            print(f"What is {a} + {b} ? ")
            
            answer = int(input())
            
            count += 1
        
        elif right > answer:
            
            print('Try again:', answer)
            
            print('Sorry guess is to low')
            
            print(f"What is {a} + {b} ? ")
            
            answer = int(input())
            
            count += 1
            
        if right == answer:
            
            print ("Congratulations !!! your answer is correct!")
            
            print('Number of guesses: ', count)
            
            menu()
#define Subtraction funtion        
def subtraction():
    
    a = random.randint (0, 20) 
    
    b = random.randint (0, 20)
    
    count = 0
    
    right = a - b
    
    question = print(f'What is {a} - {b} ?')
    
    answer = int(input())
    
    count += 1
    
    if right == answer:
        
        print ("Congratulations !!! your answer correct!")
        
        print('Number of guesses: ', count)
        
        menu()
        
    while right != answer:
        
        if right < answer:
            
            print('Try again:', answer)
            
            print('Sorry guess is to high')
            
            print(f'What is {a} - {b} ?')
            
            answer = int(input())
            
            count += 1
    
        
        elif right > answer:
            
            print('Try again:', answer)
            
            print('Sorry guess is to low')
            
            print(f'What is {a} - {b} ?')
            
            answer = int(input())
            
            count += 1
            
        if right == answer:
            
            print ("Congratulations !!! your answer correct!") 
            
            print('Number of guesses: ', count)
        
            menu()
#Define exit funtion            
def exit():
    
    exit = print('Thank you for playing...', '\n', 'Bye !!')
    
    if choice == 3:
        exit
#Define menue function    
def menu():

    print()

    print('MAIN MENU')

    print('---------------------------')

    print('1. Add Random Numbers')
    
    print('2. Subtract Random Numbers') 
    
    print('3. Exit Game')
    
    choice = int(input('Please choose one of the menu options:'))
    
    if choice == 1: 
        addition()
    
    elif choice == 2: 
        subtraction()
    
    elif choice == 3: 
        exit()
    
    elif choice > 3 or choice < 1:
        
        print('Error !!!')
        
        menu()
    
#Display Menu         
print('Welcome to Math quiz')      

print()

print('MAIN MENU')

print('---------------------------')

print('1. Add Random Numbers')
    
print('2. Subtract Random Numbers') 
    
print('3. Exit Game') 
    
print()
#get User input
choice = int(input('Please choose one of the menu options:'))
#evaluate input    
if choice == 1: 
    addition() 
    
elif choice == 2: 
    subtraction() 
    
elif choice == 3: 
    exit()

elif choice > 3 or choice < 1:
    print('Error !!!')
    menu()
    
if __name__ == '__main__':
    ()
