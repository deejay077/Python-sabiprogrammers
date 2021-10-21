# built in pyhton modules
import random              # -- import every function in the module
import random as ran  
'''from random import *       # -- import every function in the module
from random import randint # -- import the randint function from the random module'''

fruits = ['banana','orange','apples','watermelon']
my_fruit = random.choice(fruits)
print(my_fruit)
      # or
print(ran.choice(fruits))


from math import sqrt
root = sqrt(64)
print(root)

import datetime
today = datetime.datetime.now()
print(datetime.date.weekday(today))
print(today)

print(dir(datetime)) # print all modules or functions in a module

from function import waec_grade
grade = waec_grade(79,'English')
print(grade)

import function
print(function.addition(3,8))
