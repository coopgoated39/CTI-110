# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# Expense Calculator 
#13 OCT 2023
#CTI-110 P2HW1 - Travel 
#Curtis Cooper
"""
GET budget
GET location
GET fuel
GET accomondation
GET food
CALCLATE expense
CALCULATE balance
SHOW header
SHOW location
SHOW fuel
SHOW accomondation 
SHOW food 
SHOW balance
"""
print('This program calculates and displays travel expenses')
#Ask user to enter their budget
Budget =  float(input('Enter Budget: '))
#Ask user to enter travel destination
Location = input('Enter your travel destination: ')
#Ask user for amount they will spend on gas
Fuel = float(input('How much do you think you will spend on Gas? '))
# Ask user for amount they will spend on accommodation
Accomondation = float(input('Approximately how much do you think you will need for accomodation/hotel:  '))
# Ask user for amount they will spend on food
Food = float(input('Last how much do you need for food? '))
#Add expenses
Expense = (Fuel+Accomondation+Food)
#Subtract expenses from budget
Balance = (Budget-Expense)
#Display results

print('------------------Travel Expenses----------------------------')  
print('Location:',Location)
print(f'Initial Budget: ${str(Budget)} \n')

print(f'Fuel: ${str(Fuel)}')
print(f'Accomondation: ${str(Accomondation)}')
print(f'Food: ${str(Food)} \n')

print(f'Remaining Balance:${str(Balance)}')
