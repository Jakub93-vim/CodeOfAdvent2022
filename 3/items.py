from string import ascii_uppercase
from string import ascii_lowercase

file = open("input.txt",'r')
lines = file.readlines()

BigLetters = {}
smallLetters = {}

for L, N in zip(ascii_uppercase, range(27,53)):

	BigLetters.update({L:N})

for l, N in zip(ascii_lowercase, range(1,28)):

	smallLetters.update({l:N})

for line in lines:

	First_Part = line[:len(line)//2]
	Second_Part = line[len(line)//2:]

	for x in First_Part:
		for y in Second_Part:

			if x == y:
				print ('The same letter here', x)

	print ( line, First_Part, Second_Part)

print (BigLetters)
print (smallLetters)