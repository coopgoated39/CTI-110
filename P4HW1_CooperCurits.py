#CTI-110
#P4HW1 - Score List
#Curtis Cooper
#9 NOV 2023 
"""
GET amount of scores
GET scores
CALCULATE lowest score
SHOW list
CALCULATE average
SHOW lowest score
SHOW list 
SHOW Average 
SHOW grade
"""
student_scores = []
#Ask user to enter the amount of scores they want to enter
scores = int(input('How many scores would you like to enter?: '))

for num in range (1, scores + 1):
    print('Enter score #', num, ":", end=" " )
    #ask user to enter score
    score = int(input())
    
    while score < 0 or score > 100:
        print()
        print('Invalid score entered!!!!')
        print('Score should be between 0 and 100')
        print('Enter score #', num, 'again:', end=" ")
        
        score = int(input())
    student_scores.append(score)
    
print('------------------Results----------------------------') 
#calculate lowest score
print(f'{"Lowest score:" :<25}   {min(student_scores)}')
#display list
print(f'{"Modified List:"  :25}  {student_scores}')
#calculate average
print(f'{"Score average:"  :<25} {sum(student_scores)/ len(student_scores):.2f}')

avg = (sum(student_scores)/len(student_scores))

if avg >= 90:
    grade = 'A'

elif avg >= 80: 
    grade = 'B'
    
elif avg >=- 70:
    grade = 'C'
#display letter grade
print(f'{"Grade:"  :25}  {grade}')
print('------------------------------------------------------')