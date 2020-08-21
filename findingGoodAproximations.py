import math
bestDistance = 1000
PI = math.pi
for i in range (1,1000000000):
	num1 = i*PI
	num2 = round(num1)
	distance = abs(num1-num2)
	if(distance<bestDistance):
		bestDistance = distance
		print(bestDistance,": fraction", num2, "/", i)
