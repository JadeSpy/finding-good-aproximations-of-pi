import math
import random

radius = 0.5
canvas = (0,1)


rectCounter = 0
circleCounter = 0

for i in range (1, 10000000000000):
	pointX = random.uniform(0, 1)
	pointY = random.uniform(0, 1)
	if(pointX>=radius and pointY>=radius):
		#point falls into the rectangle
		rectCounter+=1
	xDistance = 0.5-pointX
	yDistance = 0.5-pointY
	distance = math.sqrt(xDistance *xDistance+yDistance*yDistance)
	if(distance<radius):
		circleCounter+=1
	if(i%2000000==0):
		PI = circleCounter/rectCounter
		print(PI)
print(circleCounter/rectCounter)

