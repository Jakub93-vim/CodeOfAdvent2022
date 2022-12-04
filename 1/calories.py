file = open("input.txt", "r")
lines = file.readlines()

calories = 0
ElfNum = 0


help(lines)

for line in lines:
	if line.strip():
		print ('space')
	else:
		print('num')