inputFile = open('day1input.txt')
inputArray = inputFile.readlines()
inputFile.close()

numberWords = {
    "one": 1,
	"two": 2,
	"three": 3,
	"four": 4,
	"five": 5,
	"six": 6,
	"seven": 7,
	"eight": 8,
	"nine": 9,
}

digitArray = []
for line in inputArray:
    digits = []
    lineArray = [*line]
    for i in range(1, len(line)):
        for key in numberWords.keys():
            if key in ''.join(lineArray[:i]):
                digits.append(numberWords.get(key))
                break
        else:
            if(lineArray[i-1].isnumeric()):
            	digits.append(int(lineArray[i-1]))
            	break
            continue
        break

    for i in range(len(lineArray), 0, -1):
        for key in numberWords.keys():
            if key in ''.join(lineArray[i-1:]):
                digits.append(numberWords[key])
                break
        else:
            if lineArray[i-1].isnumeric():
                digits.append(int(lineArray[i-1]))
                break
            continue
        break
    digitArray.append(digits)

total = 0
for digits in digitArray:
    calibValue = f"{digits[0]}{digits[1]}"
    total += int(calibValue)

print(total)