'''def without paremeters
def with parameters
return

syntax
def function_name():
def function_name(parameters):'''

# Functions without parameters
def hello():
    print('hello triumph')
#hello()

# Functions with parameters
'''def greetings(name, Age, gender, color='Black', status='single'):
    print('Hello', name, 'you are', Age, 'years old and', color, 'in complexion')
#greetings('Triumph', 12, 'white')

# return value and return statement
def addition(num1, num2):
    return num1 + num2
#print(addition(3,5))


# Weac grading
def waec_grade(score, subject):
    max_score = 100
    if score >= 70 and score <= max_score:
        return f'You had A in {subject}'
    elif score >= 60 and score < 70:
        return f'You had B in {subject}'
    elif score >=50 and score < 60:
        return f'You had C in {subject}'
    elif score >=45 and score < 50:
        return f'You had D in {subject}'
    else:
        return f'You had F in {subject}'
    

#grade = waec_grade(78, 'Mathematics')
#print(grade)

#Global Scope and Local Scope
Local variables can only be used within a function
Global variables can be used both within and outside of a function

global_variable =  26
def variable():
    local_variable = 15
    global local_x 
    local_x = 5
    print('The below variables are used within the function: ')
    print(local_variable,'is a local variable')
    print(global_variable, 'is a global variable')
    print(local_x, 'is a local variable that has been made global')

#variable()

#print()

print('The below variables are used outside the function: ')
print(global_variable, 'is a global variable')
print(local_x, 'is a local variable that has been made global')'''