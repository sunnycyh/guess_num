import random
end = input('Please enter the biggest number: ')
start = input('Please enter the smallest number: ')
end = int(end)
start = int(start)

r = random.randint(start,end)
r = int(r)
count = 0
while True:
	count += 1 # count = count + 1
	g = input('Please guess a number: ')
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