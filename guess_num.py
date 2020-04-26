import random
r = random.randint(1,100)
r = int(r)
count = 0
while True:
	count += 1 # count = count + 1
	g = input('Please guess a number from 1 to 100: ')
	g = int(g)
	if g == r:
		print('Yeah! You are correct!')
		print('This is the', count, 'time you guess.')
		break
	elif g < r:
		print('The number should be bigger!')
	elif g > r:
		print('The number should be smaller!')
	print('This is the', count, 'time you guess.')