# CTI-110
# P4HW2 
# Curtis Cooper
# 10 Nov 2023
"""
GET name
GET nummber of hours worked
GET pay rate
CALCLATE overtime hours
CALCULATE regular pay
CALCULATE overtime pay
CALCULATE gross pay
SHOW hours worked
SHOW pay rate
SHOW overtime hours
SHOW overtime pay 
SHOW regular hours pay 
SHOW gross pay
"""
employee = input("Enter employee's name or Done to terminate: ")

overtime = 0

reg_hours = 0

gross = 0 

count = 0

while employee != 'Done':
    
    num_hours = float(input("How many hours did "  +employee+ " work? "))
    
    pay_rate = float(input("What is " +employee+ " pay rate? "))
    
    print()
    
    count += 1
    
    if num_hours <= 40:
        reg_pay = pay_rate * num_hours 
        gross_pay = reg_pay + over_time_pay
        over_time_hours = 0
        over_time_pay = 0
        overtime = overtime + over_time_pay
        reg_hours = reg_hours + reg_pay
        
    else:
        over_time_hours = num_hours - 40
        reg_pay = pay_rate * 40
        over_time_pay = (pay_rate + (pay_rate / 2)) * over_time_hours
        gross_pay = reg_pay + over_time_pay
        gross = gross + gross_pay
        overtime = overtime + over_time_pay
        reg_hours = reg_hours + reg_pay
    
    print('\n')
     
    print('Employee name:', employee)
    
    print('\n')
    
    print(f'Hours worked     Pay rate     OverTime     OverTime Pay     RegHour Pay     Gross Pay')
    print('-----------------------------------------------------------------------------------------')
    print(f'{num_hours:.1f} {pay_rate:16.1f} {over_time_hours:12.1f} {over_time_pay:15.2f} {reg_pay:15.2f} {gross_pay:16.2f}')
    print('\n')
    
    employee = input("Enter employee's name or Done to terminate: ")
    

print('\n')

print('Total number of employees entered:', count)
print(f'Total amount paid for overtime: ${overtime:.2f}')
print(f'Total amount paid for regular hours: ${reg_hours:.2f}')
print(f'Total amount paid for gross: ${gross:.2f}')