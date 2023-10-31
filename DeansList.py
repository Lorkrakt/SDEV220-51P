#Student name: Cole Shane
#File name: DeansList.py
#This program will:
#ask for and accept a student's last name.
#quit processing student records if the last name entered is 'ZZZ'.
#ask for and accept a student's first name.
#ask for and accept the student's GPA as a float.
#test if the student's GPA is 3.5 or greater and, if so, print a message saying that the student has made the Dean's List.
#test if the student's GPA is 3.25 or greater and, if so, print a message saying that the studnet has made the Honor Roll.

while True:
    studentLastName = str(input("Please enter student's last name. Type ZZZ to exit: "))
    if studentLastName == 'ZZZ':
        break
    
    studentFirstName = input("Please enter student's first name: ")
    #studentFullName = studentFirstName + " " + studentLastName -testing before refactoring to f string
    studentGPA = float(input("Enter student GPA: "))
    if studentGPA >= 3.5:
        print(f"{studentFirstName} {studentLastName} has Dean's List!")
    elif studentGPA >= 3.25:
        print(f"{studentFirstName} {studentLastName} has made Honor Roll!")
    else:
        print(f"{studentFirstName} {studentLastName} is not elligible.")