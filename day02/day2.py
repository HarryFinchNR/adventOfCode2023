#Data import and clean
inputFile = open('day2input.txt')
lineArray = inputFile.readlines()
data = []
for item in lineArray:
	data.append(item.strip())

#Solution
redMax = 12
blueMax = 14
greenMax = 13

colorDict = {
	"red": 12,
	"green": 13,
	"blue": 14,
}

for i in range(len(data)):
	data[i] = data[i].replace('Game ','')
	data[i] = data[i].split(':')
	data[i][1] = data[i][1].replace(' ','')
	data[i][1] = data[i][1].split(';')
	for c in range(len(data[i][1])):
		data[i][1][c] = data[i][1][c].split(',')

##[ID, [[turn1],[turn2],...,[turn5]]]
powerTotal = 0
for i in range(len(data)):
	tempDict = {
	"red": 0,
	"green": 0,
	"blue": 0,
	}
	for c in range(len(data[i][1])):
		for e in range(len(data[i][1][c])):
			for key in colorDict.keys():
				if(key in data[i][1][c][e]):
					temp = ""
					for d in range(len(data[i][1][c][e])):
						if data[i][1][c][e][d].isnumeric():
							temp += data[i][1][c][e][d]
						else:
							break
					if(int(temp)>int(tempDict.get(key))):
						tempDict[key] = temp
	powerTotal += (int(tempDict.get("red"))*int(tempDict.get("blue"))*int(tempDict.get("green")))

print(powerTotal)

