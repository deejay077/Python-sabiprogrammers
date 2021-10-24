import random
import string
print('Welome to Dj\'s password generator')

length = int(input('\nChoose the length of your paswword '))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
number = string.digits
symbols = string.punctuation

valid_enteries = lower + upper + number + symbols

temp = random.sample(valid_enteries,length)

password = "".join(temp)

print(password)