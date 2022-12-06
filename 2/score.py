file = open("input.txt", "r")
lines = file.readlines()

score = 0

for line in lines:

	if line[0] == "A" and line[1] == "X":

		score += 2

	elif line[0] == "A" and line[1] == "X":
		
		score += 2