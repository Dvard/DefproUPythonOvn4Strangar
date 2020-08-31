text = input('Text: ')

to_count = ' '
counter = 0

for char in text:
	if char == to_count:
		counter += 1

print(f'Antalet "{to_count}" är: {counter}')
