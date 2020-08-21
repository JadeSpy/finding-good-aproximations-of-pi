import math
def PIHitBoxes(pointX, pointY):
	global rect
	global circle
	if(pointX>=0.5 and pointY>=0.5):
		rect+=1
	xDistance = 0.5-pointX
	yDistance = 0.5-pointY
	distance = math.sqrt(xDistance *xDistance+yDistance*yDistance)
	if(distance<0.5):
		circle+=1
def lastDigit(startDecimalPlaces):
	start = math.pow(10, startDecimalPlaces)
	lastDigit = 1/(start)
	lastDigitList = []
	for i in range(1, 10):
		lastDigitList.append(lastDigit*i)
	return(lastDigitList)
def otherDigits(startDecimalPlaces):
	start = math.pow(10, startDecimalPlaces)
	digit = 1/(start)
	digitList = []
	for i in range (0, 10):
		digitList.append(i*digit)

	return(digitList)


def recurseDigits(previousAmount, iteration, maximum, xValue):
	if(iteration<maximum):
		digitList = otherDigits(iteration)
		for digit in digitList:
			recurseDigits(previousAmount+digit,iteration+1,maximum,xValue)
	else:
		lastDigits = lastDigit(maximum)
		for digit in lastDigits:
			finalAmount = previousAmount+digit
			yValue = finalAmount

			PIHitBoxes(xValue, yValue)
def recurseDigits2D(previousAmount, iteration, maximum):
	global startingRecursionVariables
	if(iteration<maximum):
		digitList = otherDigits(iteration)
		for digit in digitList:
			recurseDigits2D(previousAmount+digit,iteration+1,maximum)
	else:
		lastDigits = lastDigit(maximum)
		for digit in lastDigits:
			finalAmount = previousAmount+digit
			recurseDigits(startingRecursionVariables[0],startingRecursionVariables[1],startingRecursionVariables[2], finalAmount)

def calculatePI():
	global rect
	global circle
	global numList
	global startingRecursionVariables
	numList = []
	circle = 0
	rect = 0
	places = 0
	while True:
		places+=1
		startingRecursionVariables = (0,1,places)
		recurseDigits2D(startingRecursionVariables[0],startingRecursionVariables[1],startingRecursionVariables[2])
		print("PI is: ", circle/rect)

calculatePI()


exit()







print(lastDigit(1))
#print(otherDigits(100))
def mainCalc(startDecimalPlaces):
	for i in range (1, startDecimalPlaces+1):
		if(i==startDecimalPlaces):
			lastDigit(i)
		else:
			digits = otherDigits(i)
			for val in digits:
				mainCalc( )