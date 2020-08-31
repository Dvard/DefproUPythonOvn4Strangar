def name_capitalizer(raw_name):
	separators = [' ', '-', '\n']

	result = []
	tmp = ''
	should_capitalize = False

	for char_index, char in enumerate(raw_name):
		if should_capitalize or char_index == 0 and char not in separators:
			tmp += char.upper()

			should_capitalize = False
		elif char in separators:
			should_capitalize = True

			result.append(tmp)
			if char == '-':
				result.append('-')

			tmp = ''
		else:
			tmp += char

	final_name = ''
	special_cases = ['Von', 'Sir']
	no_prefix_space = ['-']

	for part_index, part in enumerate(result):
		prefix = ' '

		if part_index == 0 or part in no_prefix_space:
			prefix = ''

		if part_index > 0:
			if result[part_index - 1] == '-':
				prefix = ''

		if part in special_cases:
			part = part.lower()

		final_name += prefix + part

	return final_name


first_name = input('First name: ')
surname = input('Last name: ')

first_name += '\n'
surname += '\n'
first_name = first_name.lower()
surname = surname.lower()

name = name_capitalizer(first_name) + ' ' + name_capitalizer(surname)

print(name)


