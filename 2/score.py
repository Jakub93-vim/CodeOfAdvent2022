file = open("input.txt", "r")
lines = file.readlines()

#A Rock, B Paper, C Scissors
#X Rock, Y Paper, Z Scissors
#score shape 1 ,2 , 3
#score play 0, 3, 6


#second round X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win

score = 0

for line in lines:

	if line[0] == "A" and line[2] == "X": # 0+3
		score += 3

	elif line[0] == "A" and line[2] == "Y": # 3+1
		
		score += 4

	elif line[0] == "A" and line[2] == "Z": # 6+2
		
		score += 8

	elif line[0] == "B" and line[2] == "X": # 0+1

		score += 1

	elif line[0] == "B" and line[2] == "Y": # 2+3
		
		score += 5

	elif line[0] == "B" and line[2] == "Z": # 6+3
		
		score += 9

	elif line[0] == "C" and line[2] == "X": # 0+2

		score += 2

	elif line[0] == "C" and line[2] == "Y": # 3+3
		
		score += 6

	elif line[0] == "C" and line[2] == "Z": #6+1
		
		score += 7

	print ('Score on the way', score)

print ('Final score is', score)