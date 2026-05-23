import math 


def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

def square(num1, num2):
    return num1 ** num2 

def squareRoot(num1, num2):
    return num1 ** 0.5




function_calls = {
    1: add,
    2: sub,
    3: mul,
    4: div,
    5: square,
    6: squareRoot
}

# shape: id: [name, age, division]

# everyone age 40
dict = employee_data

def find_employees(dict):
    if 40 in dict.values():
        return dict.keys()



def parseInput(string):
    parts = string.split(" ")
    num1 = float(parts[0])
    num2 = float(parts[2])
    key = int(parts[1])
    
    print(num1)
    print(num2)
    print(f'key is: {key}')

   
    return function_calls[key](num1, num2)


### MAIN CODE RUNS ###

while 1:
    userString = input("1. +, 2. -, 3. *, 4. /. 5. ** Enter as follows (n (operator) m)")
    finalAnswer = parseInput(userString)
    print(f'The answer is {finalAnswer}')
    print(5 ** -1)







