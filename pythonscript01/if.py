student_Mark = int(input("Enter the student Mark:   "))

if student_Mark >= 90:
    print('You scored A')
elif student_Mark >=80 <90:
    print('You scored  B')
elif student_Mark >=70 <80:
    print('You scored C')

elif student_Mark >=60 <70:
    print('You scored D')
elif student_Mark >=1 <60:
    print('You scored F')

else:
    print('Enter the right Scores')