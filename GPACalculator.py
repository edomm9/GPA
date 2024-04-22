import sys
student={'name':'null', 'age':'null', 'course':[], 'credits':[], 'grades':[], 'results':[]}
print("***Welcome to the Hub***")
student['name']=input("Enter your full name? ")
student['age']=input(f"{student['name']}, how old are you? ")
num_courses=int(input("How many courses are you taking? "))
if num_courses>0:
 while num_courses > 0:
    course=input("Course Name: ").upper()
    student['course'].append(course)
    credit=int(input(f"Enter the number of credits for {course}: "))
    student['credits'].append(credit)
    grade=input(f"Enter your grade for {course}: ")
    if grade.upper() == 'A':
        grade = 4.0
    elif grade.upper() == 'A-':
        grade = 3.75
    elif grade.upper() == 'B+':
        grade = 3.5
    elif grade.upper() == 'B':
        grade = 3.0
    elif grade.upper() == 'B-':
        grade = 2.75
    elif grade.upper() == 'C+':
        grade = 2.5
    elif grade.upper() == 'C':
        grade = 2.0
    elif grade.upper() == 'C-':
        grade = 1.75
    elif grade.upper() == 'D':
        grade = 1.0
    elif grade.upper() == 'F':
        grade = 0
    student['grades'].append(grade)
    student['results'].append(credit*grade)
    num_courses-=1
else:
    print("You're not taking any courses. Hope to see you soon!")
    sys.exit()
total_results = sum(student['results'])
total_credits = sum(student['credits'])

gpa = total_results / total_credits
print("**********************************")
print(f"Name: {student['name']}\nAge: {student['age']}")
print(f"Your GPA is {round(gpa,2)}")
print("Total credits for all courses:", total_credits)
print('***thank you for using the hub***')