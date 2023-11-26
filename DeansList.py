#Student name: Cole Shane
#File name: DeansList.py
#This program will:
#ask for and accept a student's last name.
#quit processing student records if the last name entered is 'ZZZ'.
#ask for and accept a student's first name.
#ask for and accept the student's GPA as a float.
#test if the student's GPA is 3.5 or greater and, if so, print a message saying that the student has made the Dean's List.
#test if the student's GPA is 3.25 or greater and, if so, print a message saying that the studnet has made the Honor Roll.

#removes the magic numbers and predefines them
deans = 3.5
honor = 3.25

print("Welcome to the GPA Awards Program!") #pleasant greeting

studentLastName = input("Please enter student's last name. Type ZZZ to exit: ") #prompts for last name

while studentLastName.upper() != 'ZZZ': #checks for exiting condition
    studentFirstName = input("Please enter student's first name: ") #receive input for student name

    studentGPA = float(input("Enter student GPA: ")) #receive input for student grade and conver to float
    
    if studentGPA >= deans:
        print(f"{studentFirstName} {studentLastName} has made the Dean's List!") #concatenate first/last name and print if Dean's list
    elif studentGPA >= honor:
        print(f"{studentFirstName} {studentLastName} has made Honor Roll!") #concatenane first/last and print if honor roll
    else:
        print(f"{studentFirstName} {studentLastName} is not eligible.") #concatenate first/last and print if not eligible

    studentLastName = input("Please enter another student's last name. Type ZZZ to exit: ") #repeat loop and prompt again for a student name

print("Thank you for using the GPA Awards Program!") #pleasant departure
