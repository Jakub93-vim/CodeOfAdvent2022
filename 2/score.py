file = open("input.txt", "r")
lines = file.readlines()

#A Rock, B Paper, C Scissors
#X Rock, Y Paper, Z Scissors
#score shape 1 ,2 , 3
#score play 0, 3, 6


score = 0

for line in lines:

	if line[0] == "A" and line[1] == "X":
		print ('A and X')
		score += 1

	elif line[0] == "A" and line[1] == "Y":
		
		score += 7

	elif line[0] == "A" and line[1] == "Z":
		
		score += 3

	elif line[0] == "B" and line[1] == "X":

		score += 2

	elif line[0] == "B" and line[1] == "Y":
		
		score += 5

	elif line[0] == "B" and line[1] == "Z":
		
		score += 8

	elif line[0] == "C" and line[1] == "X":

		score += 9

	elif line[0] == "C" and line[1] == "Y":
		
		score += 3

	elif line[0] == "C" and line[1] == "Z":
		
		score += 6

	#print ('Score on the way', score)

print ('Final score is', score)