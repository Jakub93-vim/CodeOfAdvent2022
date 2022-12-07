file = open("input.txt",'r')
lines = file.readlines()

for line in lines:

	First_Part = line[:len(line)//2]
	Second_Part = line[len(line)//2:]

	for x in First_Part:
		print (x, y)
		if x == y:
			print ('The same letter')

	print ( line, First_Part, Second_Part)