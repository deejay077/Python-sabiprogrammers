# SLICING AND INDEXING
# python indexes from zero but counts from 1
name = 'Triumph-Ogeh'
print(name[3])
print(name[6])
print(name[-7]) #negative indexing stsrts from the end of a string

# slicing 
print(name[:])
print(name[:5])
print(name[2:8])
print(name[-10:-3])
print(name[:-3])
print(name[-6:])

sentence = '              Today is friday                 '
#print(len(sentence)) # len()

# STRING METHODS
'''print(sentence.index('y')) # index
# casing
print(sentence.lower())
print(sentence.upper())
print(sentence.title())
print(sentence.islower())
print(sentence.isupper())
print(sentence.startswith('T'))
print(sentence.endswith('z'))
# Alignment
print(sentence.center(40,'-'))
print(sentence.ljust(40,'='))
print(sentence.rjust(40,'*'))
# White space
print(sentence.strip())
print(sentence.lstrip())
print(sentence.rstrip())

spam = 'SpamSpamBaconSpamEggsSpamSpam'
print(spam.strip('amS'))

sentence_split = sentence.split()
print(sentence_split)
print("+".join(sentence_split))'''

