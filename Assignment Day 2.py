#Write a Python program to remove the nth index character from a nonempty string.
String = 'Language'
index_remove = int(input("Which index would you like to remove?"))
string2 = String[:index_remove]+String[index_remove+1:]
print(string2)

#Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically)
Electronics = input('electronic types')
sort_electronics = Electronics.split(",")
sort_electronics2 = sorted(set(sort_electronics))
print(sort_electronics2)

#Write a Python program to print the following floating numbers upto 2 decimal places. 
x = round(3.1415, 2)
y = round(56.23879, 2)
print(x)
print(y)

#Write a Python program to count occurrences of a substring in a string
Redlady = 'The lady in red drove a red car with red painted wheels'
colour = 'red'
count =Redlady.count(colour)
print (count)

#Write a Python program to reverse a string
PROTEST = 'END SARS'
print(PROTEST[::-1])

#Write a Python program to swap comma and dot in a string
code = "77.990,17"
trans = code.maketrans
converted = code.translate(trans(',.','.,' ))
print(converted)

