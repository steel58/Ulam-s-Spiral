import math

#def variables
n = 5929 #any odd perfect square
dim = int(math.sqrt(n)) #sqrt used for a ton of stuff
spiral = [[" " for i in range(dim)] for k in range(dim)] #set up the graphic
travelDir = 0 #states which direction to go
counter = 1 #will be the number tested for 'prime-ness'
x = dim//2 #starts coordinates at the center of the matrix
y = dim//2 #starts coordinates at the center of the matrix

#def functions
def vectorMag():
	result = [0] #initializes array, needs minimum one value for the loop to work
	l = 1
	while result[-1] != dim:
		result += [l, l] #adds distance of every leg if n = 9 then ends as [1, 1, 2, 2, 3, 3]
		l += 1 #next couple of 'legs'
		
	return result[1:-1] #removes excess info
#tells how many number to put in a direction
	
def vectorDir():
	result = [] #sets up result array
	l = 0 #initial direction of right
	for i in vectorMag():
		result += [l % 4] #gets directions, 0-3, right, up, left, down respectively
		l += 1 #gets next direction
	return result
#tells direction values in anti-clockwise fashion
	
def isPrime(numberChecked):
	maxFactor = int(math.sqrt(numberChecked)) #since if a number is not prime all of its factors will be less than its square root you can cut down on the number of potential factors checked using this method
	if maxFactor == 1: #numbers 1-3
		if numberChecked == 1: #1 is not prime
			return False
		else: #2-3 is prime
			return True
	elif maxFactor > 1: #numbers > 3
		for i in range(2, maxFactor + 1):
			if numberChecked % i == 0: #if anything is evenly divisible by something other than 1 and itself is not prime
				return False
		return True
#Checks to see if x is prime

for i in range(len(vectorMag())):
	for k in range(vectorMag()[i]): #goes item by item in the magnitudes and repeats that many times
		if counter == 1: #makes the start point '0'
			spiral[y][x] = 0
		if isPrime(counter): #sets prime numbers to '#'
			spiral[y][x] = "*"
		if vectorDir()[i] == 0: #lines 53-60 interpres the direction vector as described earlier
			x += 1
		elif vectorDir()[i] == 1:
			y -= 1
		elif vectorDir()[i] == 2:
			x -= 1
		elif vectorDir()[i] == 3:
			y += 1
		counter += 1
#Places all humbers in the correct spots in the matrix

for row in spiral:
	for val in row:
		print (val, end = ' ')
	print()
#prints eveything in order and you can see the pattern
