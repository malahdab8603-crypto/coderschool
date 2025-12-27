# grab input from user
# if input is x we quit the program
# if the input is anything else we continue to the program
# new function for checking erades
# A: 90 - 100
# B: 80 - 89
# C: 70 - 79
# D: 60 - 69
# F: 0 -59

def gradeCalculator(grade):
    if grade >= 90 and grade <= 100:
        print("A")
    elif grade >= 80 and grade <= 89:
        print("B")
    elif grade >= 70 and grade <= 79:
        print("C")
    elif grade >= 60 and grade <= 69:
        print("D")
    else:
        print("F")


while(input() != 'x'):
    x = int(input("Enter your grade: "))
    gradeCalculator(x)