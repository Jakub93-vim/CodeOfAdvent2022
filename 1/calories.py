file = open("input.txt", "r")
lines = file.readlines()

calories = 0
ElfNum = 1
MostCalories = 0

for line in lines:
	if line.strip():
		calories += int(line)
	else:

		if calories > MostCalories:
			MostCalories = calories
			print ('Most cal now', MostCalories, 'on Elf', ElfNum)

		print ('Elf number:', ElfNum, 'has', calories)
		ElfNum += 1
		calories = 0

print ('Winner', MostCalories)