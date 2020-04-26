import random
r = random.randint(1,100)
r = int(r)
while True:
	g = input('Please guess a number from 1 to 100: ')
	g = int(g)
	if g == r:
		print('Yeah! You are correct!')
		break
	elif g < r:
		print('The number should be bigger!')
	elif g > r:
		print('The number should be smaller!')
		