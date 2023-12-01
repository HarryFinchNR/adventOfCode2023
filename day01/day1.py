inputFile = open('day1input.txt')
inputArray = inputFile.readlines()
inputFile.close()

numberArray = []
for item in inputArray:
	temp = []
	for char in item:
		if(char.isnumeric()):
			temp.append(char)
	numberArray.append(temp)

total = 0
for i in range(len(numberArray)):
	temp = "{0}{1}".format(numberArray[i][0],numberArray[i][len(numberArray[i])-1])
	total+=int(temp)

print(total)