height = 25

result = ''
for i in range(1, height + 1):
	n_spaces = height - i
	spaces = ' ' * n_spaces

	if i == 1:
		stars = '*'
	else:
		stars = '*' * (i + i-1)

	print(spaces + stars + spaces)
